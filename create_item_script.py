import requests

# replace X with your access token
access_token = 'X'

# read the contents of test.py file
with open('test.py') as f:
    data = f.read() 

# create a new item in the "items" collection
response = requests.post("https://api.example.com/items", json={},
         headers={'Authorization': 'Bearer {}'.format(access_token)},
         data=data)

# check if the operation was successful
if response.status_code == 201:
    print('Item created successfully')
else:
    print('Error creating item:', response.json())
