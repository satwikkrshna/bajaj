import requests

url = 'http://10.0.0.61:5000/bfhl'  # Replace with your Flask app's URL
data = {
    "data": ["M", "1", "334", "4", "B", "Z", "a"]
}

response = requests.post(url, json=data)
print(response.json())