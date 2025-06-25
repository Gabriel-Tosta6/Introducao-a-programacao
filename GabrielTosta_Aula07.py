print('-----------01-----------')

while True:
    numero = int(input('Digite um número:\n'))
    if numero == -999:
        print('Acabou!')
        break
    else:
        triplo = numero * 3
        print(f'O triplo de {numero} é {triplo}!')

print('-----------02-----------')
#usando for i in range

print('Números de 1 à 100:\n')

for i in range(1,101,1):
    print(i, end=' ')

print('\n-----------03-----------')
#usando while

print('Números de 100 à 1:\n')
i = 100

while i >= 1:
    print(i, end =' ')
    i -= 1

print('\n-----------04(extra)-----------')
    
i = 0

while True:

    n = int(input('Digite um número:\n'))

    if n <= 0:
        print('Acabou!')
        break
    else:
        i += 1

print(f'O total de números digitados foi {i}')

print('-----------05(extra)-----------')

i = 0
soma = 0

while True:

    n = int(input('Digite um número:\n'))

    if n <= 0:
        print('Acabou!')
        break
    else:
        soma += n
        i += 1 

if i > 0:
    media = soma / i
    print(f'A média dos números digitados é: {media}')
else:
    print('Nenhum número positivo foi digitado.')

print('-----------06-----------')

for i in range(2,601,2):
    print(i, end=' ')

print('\n-----------07-----------')

i = 0

while True:

    n = int(input('Digite um número:\n'))

    if n == 0:
        print('Acabou!')
        break
    elif n > 100 and n < 200:
        i += 1
print(f'A quantidade de números digitados entre 100 e 200 foi de: {i}')

print('-----------08-----------')


i = 0

print('Você entrou em um quiz de profissões! Para sair digite "Fim".')

while True:
    
    p = input('Digite sua profissão:\n').lower().strip()

    if p == 'fim':
        print('Acabou!')
        break

    elif p in ['dentista' , 'destinta']:
        i += 1

print(f'O número de dentistas digitados foi de: {i}') 

print('-----------09-----------')

chico = 1.50
juca = 1.10
anos = 0

while juca <= chico:
    juca += 0.03
    chico += 0.02
    anos += 1

print(f'Juca levou {anos} anos para ficar maior que Chico!')

print('-----------10-----------')

i = 0
print('A seguir você vai digitar 10 numeros e eu vou calcular o quadrado e a metade de cada um!\n')
while i < 10:
    n = int(input('Digite um número:\n'))

    q = n**2
    m = n/2

    print(f'O número digitado foi: {n}')
    print(f'O quadrado dele é: {q}')
    print(f'E a metade dele é: {m}\n')

    i += 1
print('Os 10 números foram digitados!')

print('-----------11-----------')

i = 1

while i < 21:

    p = i * 2.54

    print(f'{i} polegada(s) = {p:.2f} cm')

    i += 1

print('-----------12-----------')

soma = 0

for i in range(26,201,2):
    soma += i

print(f'A soma dos números pares entre 25 e 200 é {soma}!')

print('-----------13-----------')

i = 0

while i < 10:
    n = int(input('Digite um número:\n'))

    if n < 0:
        print('Numeros negativos não são aceitos! Tente novamente:')
    
    else:
        
        r = n**0.5
        print(f'A raiz quadrada de {n} é {r:.2f}')
        i += 1

print('-----------14-----------')


num = int(input('Digite um número:\n'))

soma = 0

for i in range(1,num + 1):
    if i % 5 == 0:
       soma += i
       
print(f'A soma dos números múltiplos de 5 de 1 até {num} é {soma}!')