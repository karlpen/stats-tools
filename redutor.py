# calcular o redutor da matriz de segurança

meta = 0.75

observado = 0.49

if observado >= meta:
    redutor = 0
else:
    redutor = (meta-observado) * 2

print (f"A meta era {meta}, a observação foi {observado}, e o redutor é {redutor}.")


