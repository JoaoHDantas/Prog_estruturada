anos = int(input('Quantidade de anos fumando: '))
cigarros = int(input('Quantidade de cigarros por dia: '))
cigarros_dias =(anos*365)*cigarros
dias = cigarros_dias * 10
converter = dias/1440
print(f'Vai perder {converter:.0f} dias')
