dicionario_identicador = {'W':1, 'H':1/2, 'Q':1/4, 'E':1/8, 'S':1/16, 'T':1/32, 'X':1/64}

compasso = input("Digite os compassos separados por barras: (Ex.: HH/QQQQ)")

compasso = compasso.strip('/')

lista_compassos = compasso.split(sep = '/')


lista_tempo = []
quant = 0
compassoserrados = []

for compasso in lista_compassos:
  separar_identificador = list(compasso)
  for tempo in separar_identificador:
    lista_tempo.append(dicionario_identicador[tempo])
  if sum(lista_tempo) == 1:
    quant += 1
  else:
    compassoserrados.append(compasso)
  
  lista_tempo = []


print("Quntidade de corretos:",quant)
if len(compassoserrados) != 0:
  print("Incorretos:",compassoserrados)
