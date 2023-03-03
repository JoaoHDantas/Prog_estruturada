s = int(input('Salario: '))
a = float(input('Aumento: '))
aumento = (a/100) * s
#print(a)
print(f'Seu salario foi aumentado em {a}%\nAgora você receberá {aumento:.2f}R$ de aumento\nSeu salario agora será {s+aumento}')