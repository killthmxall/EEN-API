import requests

url = "https://auth.eagleeyenetworks.com/oauth2/token"
data = {
  "grant_type": "authorization_code",
  "scope": "vms.all",
  "code": "ApZPutf1zNMQcGd7wcZW5jrVC_eigIAaNORFkCKzQVWbJA_dRuBF6p7xkebmgdOUbd5OV_-CS8_B0R6xVDa4qUFvwlTwUOkx3sfxl13anNheC-k0ScQeUCH2rB1BaQSJ",
  "redirect_uri": "http://localhost:4200"
}
headers = {
    "accept": "application/json",
    "content-type": "application/x-www-form-urlencoded"
}
response = requests.post(
  url,
  headers=headers,
  auth=(
    'c5ad678ac8ea4f9ca0775da8f779a1e1',
    'G5CK^fvP0WqiQNhP[f38'
  ),
  data=data
)

print(response.text)