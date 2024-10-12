import base64

'''
client_id = 'c5ad678ac8ea4f9ca0775da8f779a1e1'
client_secret = 'G5CK^fvP0WqiQNhP[f38'

# Combinar client_id y client_secret con un colon
credentials = f"{client_id}:{client_secret}"

# Codificar en Base64
encoded_credentials = base64.b64encode(credentials.encode()).decode()
print(encoded_credentials)
'''


import base64

client_id = 'c5ad678ac8ea4f9ca0775da8f779a1e1'
client_secret = 'G5CK^fvP0WqiQNhP[f38'

# Combinar client_id y client_secret con un colon
credential1 = "client_id"

credential2 = "client_secret"


# Codificar en Base64
client_id_encoded = base64.b64encode(credential1.encode()).decode()

client_secret_encoded = base64.b64encode(credential2.encode()).decode()

print("Client Id: " + client_id_encoded)

print("Client Secret: " + client_secret_encoded)

