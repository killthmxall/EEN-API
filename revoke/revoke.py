import requests

url = "https://auth.eagleeyenetworks.com/oauth2/revoke"

data = {
    'token': '<token value>'
}
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Basic <clientid:clientsecret>.base64()'
}

response = requests.post(
    url,
    headers = headers,
    auth = ('CLIENT_ID', 'CLIENT_SECRET'),
    data = data
)

print(response.text)