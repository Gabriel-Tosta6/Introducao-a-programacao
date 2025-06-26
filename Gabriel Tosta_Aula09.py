ps = "banana"
i = 0
w = input('Tente adivinhar qual a palavra secreta. Dica (É amarela). Digite uma palavra:\n').strip().lower()
while True:
    w = input('Ops, não é essa, tente novamente:\n').strip().lower()
    i += 1
    if w == ps:
        print('Você acertou!!!')
        break
    if w != ps and i >= 3:
        print('Acabaram usas tentativas :(')
        break

print('---------------------------------------')

n = int(input('Digite um número inteiro e positivo:\n'))
maior = 0
menor = 0
while True:

    if n < 0:
        print('O número digitado é negativo, programa encerrado!')
        break
    elif n > 5:
        print(f'\n{n} é maior que 5!')
        maior += 1
    else:
        print(f'{n} é menor que 5!')
        menor += 1
    
    n = int(input('Digite outro número inteiro e positivo:\n'))
print('---------------------------------------')

for i in range (1,100):
    print(i)
    if i == 25:
        break


for i in range(0,51):
    if i % 3 == 0 or i % 4 == 0:
        continue
print(i)

print('---------------------------------------')

n1 = int(input('Digite um número inteiro:\n'))
n2 = int(input('Digite outro número inteiro:\n'))

print("""Menu de opções:\n
Escolha uma operação\n
1 - Somar\n
2 - Subtrair\n
3 - Multiplicar\n
4 - Dividir\n""")

o = int(input('Escolha o número da operação desejada:\n'))

match o:
        case 1:
            print(f'O resultado da soma do número {n1} com o número {n2} é: {n1+n2}')
        case 2:
            print(f'O resultado da subtração do número {n1} com o número {n2} é: {n1-n2}')
        case 3:
            print(f'O resultado da multiplicação do número {n1} com o número {n2} é: {n1*n2}')
        case 4:
            print(f'O resultado da divisão do número {n1} com o número {n2} é: {n1/n2}')
        case _:
            print('Operação inválida!')

print('---------------------------------------')

saldo = 5000.00
while True:
    print("""---MENU DO BANCO---\n
1 - Ver saldo\n
2 - Depositar\n
3 - Sacar\n
4 - Sair\n""")
    n = int(input('Qual operação você deseja realizar?:\n'))
    match n:
        case 1:
            print(f'Seu saldo é de: R${saldo}\n')
        case 2:
            deposito = float(input('Quanto você deseja depositar?:\n'))
            print('Deposito realizado!')
            saldo += deposito
        case 3:
            saque = float(input('Quanto você deseja sacar?:\n'))
            print('Saque realizado!')
            saldo -= saque
        case 4:
            print('Você saiu!')
            break