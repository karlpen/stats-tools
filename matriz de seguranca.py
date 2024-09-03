# script para definir o valor corrigido da matriz de segurança
# baseado na distância entre o observado no indicador e a meta do indicador
# quanto mais distante da meta, menor o valor
# quando a distância for maior ou igual a 50%, o valor é zero
# quando alcançar a meta, o valor é igual ao peso original na matriz

# informar abaixo o resultado do indicador EM PERCENTUAL
resultado_indicador = 35
# informar abaixo a meta do indicador EM PERCENTUAL
meta_indicador = 75
# peso original do indicador
peso_original = 2

if ( resultado_indicador >= meta_indicador ):
    valor = peso_original
    distancia = 0
    redutor = 0
else:
    # calcula proporção resultado/meta
    prop_indicador = resultado_indicador/meta_indicador

    # calcula distância proporção para meta
    distancia = (1- prop_indicador)
    if distancia >= 0.5:
        valor = 0
        redutor = 1
    else:
        redutor = distancia * 2
        valor = peso_original * (1- redutor)

print ("resultado indicador", resultado_indicador)
print ("meta indicador", meta_indicador)
print ("peso original", peso_original)
print ("distancia", distancia)
print ("redutor", redutor)
print ("valor corrigido", valor)




