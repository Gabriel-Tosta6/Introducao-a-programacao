print('--------------------------01--------------------------')

n = int(input('Digite um número:\n'))
while n > 0:

    if n < 5:
        print('É menor que 5!')
    elif n == 5:
        print('É igual a 5!')
    else:
        print('É maior que 5!')
    n = int(input('Digite um número:\n'))
print('Número negativo detectado. Acabou!')

print('--------------------------02--------------------------')

i = int(input('Digite sua idade:\n'))
criança = 0
homi = 0
idoso = 0
while i > 0 and i <120:
    if i <= 18:
        criança += 1
    elif i > 19 and i <=60:
        homi += 1
    elif i > 60:
        idoso += 1
    i = int(input('Digite sua idade:\n'))
print(f"""O total de crianças é de {criança}. 
O de adultos é de {homi}. 
E de idosos é {idoso}!""")

print('--------------------------03--------------------------')

from math import inf
maior = -inf
while True:
    n = int(input('Digite um número inteiro:\n'))
    if n > maior:
        maior = n
    if n == -100:
        break
print(f'O maior número é {maior}!')

print('--------------------------04--------------------------')

i = 0
soma = 0
n = float(input('Digite um número:\n'))
while n != 0:
    i += 1
    soma += n
    n = float(input('Digite um número:\n'))
media = soma / i
print(f'{i} números foram digitados e a média deles é: {media:.2f}')

print('--------------------------05--------------------------')

n = int(input('Digite um número inteiro:\n'))
i = 0
print("Par  Ímpar")
while i < n:
    par = ""
    ímpar = ""
    if i % 2 == 0:
        par = str(i)
    else:
        ímpar = str(i)
    print(f"{par}    {ímpar}")
    i += 1

print('--------------------------06--------------------------')

n = float(input('Digite um número entre 12 e 20:\n'))
while n < 12 or n > 20:
        n = float(input('O número digitado não está entre 12 e 20, tente novamente:\n'))
print(f'O número digitado foi {n:.2f}')

print('--------------------------07--------------------------')

while True:
    n = float(input('Digite um número positivo:\n'))
    if n <= 0:
        print('O número digitado não é positivo, tente novamente.\n')
        continue
    else:
        print(f'\nA seguir você vai ver a sequência fibonacci até o primeiro número maior que {n}:\n')

        a,b = 0,1
        while a <= n:
            print(a, end=" -> ")
            a,b = b, a + b
        print(f'{a} (Primeiro número maior que {n})!')
        con = input('\nDeseja ver outra sequência? (s/n): ').lower()
        if con != 's':
            break
print('Acabou!')

print('--------------------------08--------------------------')

soma = 0
n = int(input('Digite um número inteiro ímpar:\n'))
while n % 2 != 0:
    soma += n
    n = int(input('Digite outro número:\n'))
if soma > 0:
    dif = soma - n
    print(f"""A soma dos números ímpares digitados é: {soma}.
O número par digitado foi {n}.
E a diferença entre os numeros ímpares e o número par é: {dif}.""")
else:
    print('\nNenhum número ímpar foi digitado antes do par.')

print('--------------------------09--------------------------')

soma = 0
n = int(input('Digite um número inteiro:\n'))
while True:
    soma += n
    if soma % 7 == 0:
        print(f'{soma} é divisível por 7!')
        break
    n = int(input('Digite outro número inteiro:\n'))

print('--------------------------10--------------------------')
# Esse código solicita números inteiros ao usuário com repetição e soma apenas os valores pares, ignora os ímpares, até que a soma dos números pares digitados atinja ou ultrapasse 100.

n = int(input('Digite um número inteiro:\n'))
soma = 0
i = 0
maior = 0
while soma < 100:
    if n % 2 == 0:
        i += 1
        soma += n
        print(f'-> Par! Soma atual: {soma}')
        if n > maior:
            maior = n
    else:
        print('-> Ímpar! Ignorado.')
    if soma < 100:
        n = int(input('Digite outro número inteiro:\n'))
print ('RESULTADO:\n')
print(f"""Soma total: {soma}
Números pares digitados: {i}
Maior número par: {maior}""")