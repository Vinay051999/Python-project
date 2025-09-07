import requests

Base_URL = "https://jsonplaceholder.typicode.com/posts"

data={
    'name': 'vinay',
    'Username': 'vinay123',
    'email': 'vinay@.com'
}
response = requests.post(Base_URL, data=data)

print(response.json())