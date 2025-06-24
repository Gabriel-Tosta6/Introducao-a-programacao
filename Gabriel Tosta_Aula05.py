#01 - Valor Cúbico

n1 = int(input('Digite um número: \n'))
n2 = int(input('Digite mais um número: \n'))
n3 = int(input('Digite outro número: \n'))
n4 = int(input('Digite um último número: \n'))

cúbico = (n1*2*3) + (n2**3) + (n3**3) + (n4**3)

print('O valor cúbido dos números digitados é: ', cúbico)

print('-----------------------------------------')

#02 - Área Retângulo

base = float(input('Digite a base do retângulo: \n'))
altura = float(input('Digite a altura do retângulo: \n'))
área = base*altura

print(f'A área do retângulo é: {área:.2f}')

print('-----------------------------------------')

#03 - Compra e Troco

v_compra = float(input('Qual o valor da compra?: \n'))
v_pago = float(input('Qual o valor que você entregou?: \n'))
troco = v_pago - v_compra

print(f'O seu troco é: R${troco:.2f}')

print('-----------------------------------------')

#04 - Circunferência

raio = float(input('Qual o raio da circunferência?: \n'))

pi = 3.14159
c_esfera = 2 * pi * raio
área = pi * (raio**2)
volume = ((3/4) * pi * raio**3 )

print(f'A circunferência da esfera é: {c_esfera:.2f}')

print(f'A área da esfera é: {área:.2f}m²')

print(f'O volume da esfera é: {volume:.2f}m³')

print('-----------------------------------------')

#05 - Calculo de Ângulos

a1 = float(input('Digite o primeiro ângulo do triângulo: \n'))
a2 = float(input('Digite o segundo ângulo do triângulo: \n'))
a3 = 180 - (a1 + a2)

print(f'O terceiro ângulo do triângulo é: {a3:.2f}°')

print('-----------------------------------------')

#06 - Cálculo de Salário

salário = float(input('Qual o seu salário atual?: \n'))
novo_salário = ((15/100) * salário) + salário 

print(f'Seu novo salário é: R${novo_salário:.2f}')

print('-----------------------------------------')

#07 - Conversor de Temperatura

grau = float(input('Digite a temperatura em Celsius: \n'))
F = 180 * (grau + 32) / 100

print(f'A temperatura em Farenheit é:{F} F°')

print('-----------------------------------------')

#08# - Conversor de pés (sla)

pé = float(input('Digite uma medida em pés: \n'))

polegada = pé * 12
jarda = pé / 3
milha = pé / (1760*3)

print(f'A medida em polegadas é: {polegada:.2f}')
print(f'A medida em jardas é: {jarda:.2f}')
print(f'A medida em milhas é: {milha:.2f}')

print('-----------------------------------------')

#09 - Descobridor dos Segundos (Esse nome ficou top)

h = int(input('Quantas horas se passaram desde a meia noite?: \n'))
m = int(input('Quantos minutos se passaram desde a meia noite?: \n'))

s_h = h * 3600
s_m = m * 60
s_t = s_h + s_m

print(f'Seu dia teve {s_t:.2f} segundos.')

print('-----------------------------------------')

#10 - Linha de Crédito

salário = float(input('Informe o seu salário: \n'))
prestação = (30 / 100) * salário

print(f'O valor máximo de prestação que você pode pagar é: R${prestação:.2f}')

#Fim