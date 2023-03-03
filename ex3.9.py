#print('Digite dia, hora, minutos e segundos pra converter apara segundos')
#dia = int(input('Digite o dia: '))
#hora = int(input('Digite a hora: '))
#min = int(input('Digite os minutos: '))
#sec = int(input('Digite os segundos: '))
#print(f'Em segundos, Dias: {dia*86400}, Horas: {hora*3600} minutos: {min*60}, Segundos: {sec}')
#print(f'Seu resultado foi: {dia*86400+hora*3600+min*60+sec}')

print('Digite dia, hora, minutos e segundos pra converter apara segundos')
dia = int(input('Digite a quantidade de dias: '))
while True:
    hora = int(input('Digite as horas:'))
    if hora < 24:
      break
    else:
        print('Digite um numero menor que 24')
while True:
    min = int(input('Digite os minutos:'))
    if min < 60:
        break
    else:
        print('Digite um numero menor que 60')
while True:
    sec = int(input('Digite os segundos: '))
    if sec < 60:
        break
    else:
        print('Digite um numero menor que 60')
print(f'Dias em sec: {dia*86400}, Horas em sec: {hora*3600} minutos em sec: {min*60}, Segundos: {sec}')
print(f'Seu resultado foi: [{dia*86400+hora*3600+min*60+sec}]')