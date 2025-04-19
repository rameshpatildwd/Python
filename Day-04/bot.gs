function doPost(e) {
    var lambdaUrl = "https://9h4hdjw442.execute-api.ap-south-1.amazonaws.com/prod/Whitelist"; // Replace with actual API Gateway URL
    var cache = CacheService.getUserCache(); // Use cache to persist user responses
   
    try {
      var requestData = JSON.parse(e.postData.contents);
      var userMessage = requestData.message.text.trim();
      var userId = requestData.user.name;
      var userName = requestData.user.displayName || "User"; // ✅ Automatically capturing username
   
      // // Exit command
      // if (userMessage.toLowerCase() === "exit") {
      //   cache.remove(userId);
      //   return sendBotReply("✅ Restarted! Hi " + userName + ", let's start again. Please enter your IP address.");
      // }
   
      // Retrieve stored responses (if any)
      var storedData = cache.get(userId);
      var userResponses = storedData ? JSON.parse(storedData) : { step: 0 };
   
      if (userResponses.step === 0) {
        userResponses.username = userName; // ✅ Store username automatically
        userResponses.step = 1;
        cache.put(userId, JSON.stringify(userResponses), 300);
        return sendBotReply(`👋 Hi ${userName}! I am Cloud Ops Whitelisting Bot. I can help whitelist your IP for Jenkins & Test link access.\n\n➡️ Please enter your IP address.`);
      }
   
      else if (userResponses.step === 1) {
        if (!isValidIP(userMessage)) {  // ✅ Check if entered IP is valid
          return sendBotReply("Invalid IP format! Please enter a valid IPv4 address (e.g., 192.168.1.1).");
        }
        // ✅ Block 0.0.0.0 or 0.0.0.0/0
        if (userMessage === "0.0.0.0" || userMessage === "0.0.0.0/0") {
          return sendBotReply("Security Concern: Whitelisting '0.0.0.0/0' is not allowed!");
        }
   
        userResponses.ip = userMessage;
        userResponses.step = 2;
        cache.put(userId, JSON.stringify(userResponses), 300);
        return sendBotReply("Thanks! Now, enter the URL you would like to access.");
      }
   
      else if (userResponses.step === 2) {
        userResponses.url = userMessage;
   
        // Send collected data to AWS Lambda
        var payload = {
          "username": userResponses.username, // ✅ Username automatically included
          "ip": userResponses.ip,
          "url": userResponses.url
        };
   
        var options = {
          "method": "post",
          "contentType": "application/json",
          "payload": JSON.stringify(payload),
          "muteHttpExceptions": true // ✅ Prevents script failure on HTTP 400 errors
        };
   
        var lambdaResponse = UrlFetchApp.fetch(lambdaUrl, options);
        var responseJson = JSON.parse(lambdaResponse.getContentText());
        var botReply = responseJson.reply || "Something went wrong!";
   
        // Clear stored responses for the user
        cache.remove(userId);
        return sendBotReply(botReply);
      }
    } catch (error) {
      console.error("Error:", error.toString());
      return sendBotReply("An error occurred: " + error.toString());
    }
  }
   
  function sendBotReply(message) {
    return ContentService.createTextOutput(
      JSON.stringify({ "text": message })
    ).setMimeType(ContentService.MimeType.JSON);
  }
   
  // ✅ Function to Validate IPv4 Address
  function isValidIP(ip) {
    var ipPattern = /^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])(\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])){3}$/;
    return ipPattern.test(ip);
  }
  