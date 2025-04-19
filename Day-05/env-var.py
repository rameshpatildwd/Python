import os       #To read env vars

#set env var in CLI using - export password="Ramesh"

#To print pre set env var - call the name of env var
print(os.getenv("password"))
