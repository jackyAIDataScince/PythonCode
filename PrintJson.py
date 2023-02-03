from urllib import request
response = request.urlopen("https://jsonplaceholder.typicode.com/users")
json_response = response.read()
#print(json_response)

import json
users = json.loads(json_response)
#print(users)

for user in users:
   # print(user)

