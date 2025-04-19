import json
import boto3

ec2 = boto3.client("ec2", region_name="ap-south-1")

URL_SG_MAPPING = {
    "jenkins1.com": "sg-0e24a50ccdc5eb523",
    "jenkins2.com": "sg-0358da714bb47c666",
    "jenkins3.com": "sg-0ca957137f6802b37"
}

def lambda_handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))
        username = body.get("username", "Unknown User")
        ip = body.get("ip", "Unknown IP").strip()
        url = body.get("url", "").strip().lower()

        print(f"Received request: User: {username}, IP: {ip}, URL: {url}")

        # Prevent whitelisting 0.0.0.0/0 for security reasons
        if ip == "0.0.0.0" or ip == "0.0.0.0/0":
            return {
                "statusCode": 400,
                "body": json.dumps({"reply": "❌ Security Concern: Whitelisting '0.0.0.0/0' is not allowed!"})
            }

        if not url or url not in URL_SG_MAPPING:
            return {
                "statusCode": 400,
                "body": json.dumps({"reply": f"❌ No Security Group found for URL: {url}"})
            }

        security_group_id = URL_SG_MAPPING[url]

        # Ensure IP is in CIDR format
        if "/" not in ip:
            ip = f"{ip}/32"

        # Fetch existing security group rules
        sg_details = ec2.describe_security_groups(GroupIds=[security_group_id])
        existing_rules = sg_details["SecurityGroups"][0].get("IpPermissions", [])

        existing_rule = None
        for rule in existing_rules:
            if rule["FromPort"] == 8080 and rule["IpProtocol"] == "tcp":
                for ip_range in rule.get("IpRanges", []):
                    if ip_range.get("Description") == username:
                        existing_rule = ip_range
                        break

        # If username exists, update the rule by revoking the old IP and adding the new one
        if existing_rule:
            old_ip = existing_rule["CidrIp"]
            print(f"Updating rule: Removing {old_ip} and adding {ip} for {username}")

            # Revoke old IP
            ec2.revoke_security_group_ingress(
                GroupId=security_group_id,
                IpPermissions=[{
                    "IpProtocol": "tcp",
                    "FromPort": 8080,
                    "ToPort": 8080,
                    "IpRanges": [{"CidrIp": old_ip}]
                }]
            )

        # Add new IP rule
        ec2.authorize_security_group_ingress(
            GroupId=security_group_id,
            IpPermissions=[{
                "IpProtocol": "tcp",
                "FromPort": 8080,
                "ToPort": 8080,
                "IpRanges": [{"CidrIp": ip, "Description": username}]
            }]
        )

        message = f"Perfect!\n{username}, your IP {ip} has been whitelisted in {url}'s SG!"
        return {"statusCode": 200, "body": json.dumps({"reply": message})}

    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"reply": f"❌ Error: {str(e)}"})}
