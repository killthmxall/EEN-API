import base64

#PRIMERO EJECUTAR ESTE CÓDIGO
codificar = b"""c5ad678ac8ea4f9ca0775da8f779a1e1:G5CK^fvP0WqiQNhP[f38"""

print(base64.b64encode(codificar))

#DECODIFICAR LO ANTERIOR
decode = b'YzVhZDY3OGFjOGVhNGY5Y2EwNzc1ZGE4Zjc3OWExZTE6RzVDS15mdlAwV3FpUU5oUFtmMzg='

print(base64.b64decode(decode))