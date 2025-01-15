import request

url = "http://localhost:2222/user/f81378df5c014d29828e41c4e64f7d48/"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzY4NjUxMTM5LCJpYXQiOjE3MzI2NTExMzksImp0aSI6IjljZjc1MmEzYWI2MTQxZmZiYmEzYmY3N2FlZTVhOTc1IiwidXNlcl9pZCI6MTAxfQ.X6HfNQHrs549WBjQpC_Ar3QpaXt03GS8HRxRUzC3Zro"  # Include this if authentication is required
}
data = {
    "username": "ekc"  # New username
}

response = request.patch(url, json=data, headers=headers)

if response.status_code == 200:
    print("Update successful:", response.json())
else:
    print("Failed to update:", response.status_code, response.text)
