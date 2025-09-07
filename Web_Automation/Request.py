import requests
Base_URL = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(Base_URL)
data=response.json()
# Print details for each post in the response
# for post in data:
# 	print("ID", post['id'])
# 	print("Title", post['title'])
# 	print("UserID", post['userId'])
# 	print("---")

# print(data.title)
# print(data.userId)
# print(data.body)
for post in data:
    print('name' ,data['name'])
    print('Username' ,data['Username'])
