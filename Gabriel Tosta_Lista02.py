print('----------------------01----------------------')
n = int(input('\nDigite um número:\n'))
n1 = int(input('Digite outro número:\n'))
print("""\n***OPERAÇÕES MATEMÁTICAS***\n
1 - Somar\n
2 - Subtrair\n
3 - Multiplicar\n
4 - Dividir\n
5 - Sair\n""")
o = int(input('Escolha o que você quer fazer com os dois números digitados:\n'))
while o == 1 or o == 2 or o == 3 or o == 4 or o == 5:
    match o:
        case 1:
            soma = n+n1
            print(f'O resultado da soma entre {n} e {n1} é: {soma}')
        case 2:
            sub = n-n1
            print(f'O resultado da subtração entre {n} e {n1} é: {sub}')
        case 3:
            mult = n*n1
            print(f'O resultado da multiplicação entre {n} e {n1} é: {mult}')
        case 4:
            div = n/n1
            print(f'O resultado da divisão entre {n} e {n1} é: {div}')
        case 5:
            print('Você saiu!')
            break
        case _:
            print('Opção inválida, tente novamente:')
print('\nNenhuma operação foi selecionada!')
print('----------------------02----------------------')
n1 = int(input('\nDigite um valor inteiro:\n'))
n2 = int(input('Digite outro valor inteiro:\n'))
soma = 0
for i in range(n1,n2):
    if i % 2 != 0:
        continue
    else:
        soma += i
print(f'\nA soma dos números pares entre {n1} e {n2} é {soma}')
print('----------------------03----------------------')
n = float(input('\nDigite suas notas para calcular a média entre elas. (Digite "-1" para encerrar):\n'))
soma = 0
i = 0
while n != -1:
    soma += n
    i += 1
    n = float(input('Digite outra nota:\n'))
media = soma / i
print(f'A média das notas digitadas foi de: {media}')
print('----------------------04----------------------')
n = float(input('\nA seguir o programa solicitará 10 números, digite:\n'))
positivo = 0
negativo = 0
nulo = 0
for i in range(0,10):
    if n < 0:
        negativo += 1
        print(f'\n{n} é negativo!')
    elif n == 0:
        nulo += 1
        print(f'\n{n} é nulo!')
    else:
        positivo += 1
        print(f'\n{n} é positivo!')
    n = float(input('\nDigite outro número:\n'))
print(f"""\nO total de números positivos digitado foi de: {positivo}.\n
\nO total de números negativos digitado foi de: {negativo}.\n
\nE o total de números nulos digitado foi de: {nulo}.\n
\nPrograma encerrado!""")

print('----------------------05----------------------')
n = float(input('\nDigite um número:\n'))
print("""\n---/MENU DE CÁLCULOS/---
\n1 - Calcular Potência\n
2 - Calcular Raiz Quadrada\n
3 - Sair\n""")
o = int(input('Qual operação você deseja realizar?:\n'))
while o == 1 or o == 2 or o == 3:
    match o:
        case 1:
            p = int(input(f'\nÀ que número você deseja elevar {n}?:\n'))
            potencia = n ** p
            print(f'\n{n} elevado à {p} é {potencia}!\n')
        case 2:
            raiz = n ** 0.5
            print(f'A raiz quadrada de {n} é {raiz}!\n')
        case 3:
            print('\nPrograma encerrado!')
            break
        case _:
            print('Número inválido digitado, tente novamente!\n')
print('----------------------06----------------------')
n = int(input('Digite um número inteiro:\n'))
while True:
    for i in range(1,11):
        print(f'{n} x {i} = {n*i}')
    d = int(input('\nVocê deseja ver a tabuada de outro número? (1 - Sim / 0 - Não):\n'))
    match d:
        case 0:
            print('Programa encerrado!')
            break
        case 1:
            n = int(input('\nDigite o número que você deseja para ver sua tabuada:\n'))
print('----------------------07----------------------')
n = int(input('\nDigite um número inteiro:\n'))
soma = 0
for i in range(1,n+1):
    if i % 3 == 0:
        soma += i
    else:
        continue
print(f'\nA soma dos números múltiplos de 3, até o número {n} foi de: {soma}!\n')
print('----------------------08----------------------')
n = int(input('\nDigite um número inteiro e positivo:\n'))
impar = 0
par = 0
n_processar = n
if n == 0:
    par += 1
else:
    while n_processar > 0:
       d = n_processar % 10
       if d % 2 == 0:
           par += 1
       else:
           impar += 1
       n_processar //= 10
print(f"""\nNo número {n} 
\nA quantidade de dígitos pares foi {par}.
\nE a quantidade de dígitos ímpares foi {impar}.""")
print('----------------------09----------------------')
i = 1
senha = 1234
while i <=3:
    n = int(input('\nAdivinhe a senha (Dica: Tem 4 Dígitos):\n'))
    if n != senha:
        i += 1
        if i <= 3:
            print('\nSenha incorreta, tente novamente.\n')
    else:
        print('\nSenha correta, acesso permitido!\n')
        break
if i > 3:
    print('\nTentativas excedidas, acesso negado!')
print('----------------------10----------------------')
opção = 0
valor = 0
while opção != 5:
    print("""\n-=-=-MENU DOS CÁLCULOS-=-=-\n
1 - Adicionar ao valor total\n
2 - Subtrair do valor total\n
3 - Mostrar total\n
4 - Zerar total\n
5 - Sair\n""")
    n = int(input('Selecione uma operação:\n'))
    match n:
        case 1:
            soma = float(input('Quanto você deseja adicionar?:\n'))
            valor += soma
            print(f'\n-=-=-{soma} foi adicionado ao valor total-=-=-')
        case 2:
            sub = float(input('Quato você deseja subtrair?:\n'))
            valor -= sub
            print(f'\n-=-=-{sub} foi subtraído do valor total.-=-=-')
        case 3:
            print(f'\n-=-=-O valor total é {valor}-=-=-')
        case 4:
            valor = 0
            print('\n-=-=-O valor total foi zerado.-=-=-')
        case 5:
            print('\n-=-=-Programa encerrado!-=-=-')
            break
        case _:
            print('\nOpção inválida, tente novamente.')

