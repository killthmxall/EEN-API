import requests

url = "https://auth.eagleeyenetworks.com/oauth2/token"
data = {
  "grant_type": "authorization_code",
  "scope": "vms.all",
  "code": "P9ka6AXvIZNId9tVpUOV-RYSZxwleazh2kaGOEF9SKZaK7RBdRiNFGUKDq-6pIwe8PYwytOLORL62Pveb15nXAf6TLBYEGMJOJoIQbLO_rJjxmDaWTle9zLT6yKe0QyA",
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