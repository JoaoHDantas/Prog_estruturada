m = int(input('Preço da mercadoria: '))
d = float(input('Desconto: '))
porcento = (d/100)*m
print(f'Seu desconto foi de {porcento}% Agora você irá pagar {m-porcento}R$ Na sua mercadoria')