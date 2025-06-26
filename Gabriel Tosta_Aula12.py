print('x-'*5 , '01' , 'x-'*5)

numeros_inteiros = []
for i in range(5):
    while True:
        try:
            n = int(input(f'\nDigite o {i+1}º número inteiro:\n'))
            numeros_inteiros.append(n)
            break
        except ValueError:
            print('Entrada inválida, tente novamente!')
print('\nNúmeros Digitados:\n')
print(f'{numeros_inteiros}\n')

print('x-'*5 , '02' , 'x-'*5)

numeros_reais = []
for i in range(10):
    while True:
        try:
            n = float(input(f'\nDigite o {i+1}º número real:\n'))
            numeros_reais.append(n)
            break
        except ValueError:
            print('Entrada inválida, tente novamente!')
print('\nNumeros digitados na ordem inversa:\n')
numeros_reais.reverse()
print(f'{numeros_reais}\n')


print('x-'*5 , '03' , 'x-'*5)

print('\nA seguir digite 4 notas, vou calcular a média entre elas!\n')
notas = []
for i in range(4):
    while True:
        try:
            n = float(input(f'\nDigite a {i+1}ª nota:\n'))
            notas.append(n)
            break
        except ValueError:
            print('\nEntrada inválida, tente novamente!\n')
print('\nNotas digitadas:\n')
print(notas)
print('\nMédia das notas digitadas:\n')
media = sum(notas) / len(notas)
print(f'{media}\n')

print('x-'*5 , '04' , 'x-'*5)

consoantes = []
print('\nA seguir, digite 10 letras, e eu vou dizer quais delas são consoantes!')

for i in range(10):
    while True:
        try:
            l = str(input(f'\nDigite a {i+1}ª letra:\n')).upper()
            if l == 'A' or l == 'E' or l == 'I' or l == 'O' or l == 'U':
                print(f'{l} não é consoante!')
            else:
                consoantes.append(l)
                
            break
        except ValueError:
            print('Entrada inválida, tente novamente!\n')
print(f'Foram lidas {len(consoantes)} consoantes, são elas:\n {consoantes}')

print('x-'*5 , '05' , 'x-'*5)

print('\nA seguir digite 20 números inteiros, vou separá-los nas categorias PAR e ÍMPAR!')
NUMEROS = []
PAR = []
ÍMPAR = []
for i in range(20):
    while True:
        try:
            n = int(input(f'\nDigite o {i+1}º número inteiro:\n'))
            NUMEROS.append(n)
            break
        except ValueError:
            print('Entrada inválida, tente novamente!')
for n in NUMEROS:
    if n % 2 == 0:
        PAR.append(n)
    else:
        ÍMPAR.append(n)

print('\nResultado:\n')
print(f'Pares: {PAR}')
print(f'\nÍmpares: {ÍMPAR}')
print(f'\nTotal: {NUMEROS}')

print('x-'*5 , '06' , 'x-'*5)

print('Esse programa foi desenvolvido para calcular a média de um atleta de salto a distância, a seguir informe o nome do atleta e a distância dos seus 5 saltos(Para encerrar o programa digite: "ENCERRAR"):\n')

while True:
    nome = str(input('Digite o nome do atleta(Ou pressione "ENTER" para encerrar):\n')).strip()
    if not nome:
        print('Programa encerrado!')
        break
    SALTOS = [] 

    print(f'Atleta: {nome}') 

    for i in range(5):
        while True:
            try:
                nsalto = ('Primeiro','Segundo','Terceiro','Quarto','Quinto')
                salto = float(input(f'{nsalto[i]} Salto: ')) 
                if salto >= 0:
                    SALTOS.append(salto)
                    break
                else:
                    print('A distância do saldo deve ser um valor positivo!')
            except ValueError:
                print('Entrada inválida, tente novamente!')
    if SALTOS:
        MEDIA = sum(SALTOS) / len(SALTOS)
    else:
        MEDIA = 0
    print('\nResultado final:')
    print(f'Atleta: {nome}') 
    formatar_salto = ' - '.join(([f"{s:.1f}" for s in SALTOS]))
    print(f'Saltos: {formatar_salto}') 
    print(f'Média dos saltos: {MEDIA:.1f}m')
    
    print('\n' + '='*40)

print('x-'*5 , '07.1' , 'x-'*5)

SISTEMAS = ['Nenhum','Windows Server','Unix','Linux','Netware','Mac OS','Outro']
VOTO = [0] * 7

print('\n"Qual o melhor sistema operacional para uso em servidores?"\n')
print('As possíveis respostas são:\n')
print("""1 - Windows Server
2 - Unix
3 - Linux
4 - Netware
5 - Mac OS
6 - Outro
0 - Sair\n""")

while True:
    try:
        voto_str = input('Selecione uma opção: ').strip() 
        voto = int(voto_str)
        
        if voto == 0:
            print('Programa encerrado!\n')
            break

        elif 1 <= voto <= 6:
            VOTO[voto] += 1
            print(f'Voto para "{SISTEMAS[voto]}" registrado com sucesso!\n')
        else:
            print('Voto inválido! Por favor, digite um número entre 1 e 6, ou 0 para encerrar.\n')

    except ValueError:
        print('\nEntrada inválida, tente novamente!\n')

TOTAL_VOTOS = sum(VOTO[1:])
MS = ""
MP = -1.0
MV = -1

if TOTAL_VOTOS == 0:
    print('Nenhum voto válido foi registrado!\n')
else:
    print('\n--- Resultado da Enquete ---')
    print('Sistema Operacional     Votos     %')
    print('-------------------     -----     ---')
    for i in range(1, len(SISTEMAS)):
        NOME_SISTEMAS = SISTEMAS[i]
        CONTAGEM_VOTOS = VOTO[i]
        percentual = (CONTAGEM_VOTOS / TOTAL_VOTOS) * 100 

        print(f"{NOME_SISTEMAS:<20} {CONTAGEM_VOTOS:>5} {percentual:>6.2f}%")

        if CONTAGEM_VOTOS > MV:
            MV = CONTAGEM_VOTOS
            MS = NOME_SISTEMAS
            MP = percentual
        elif CONTAGEM_VOTOS == MV:
            pass
    print('-------------------     -----     ---')
    print(f'Total de votos: {TOTAL_VOTOS}')

    print(f'\nO Sistema Operacional mais votado foi o {MS},')
    print(f'com {MV} votos, correspondendo a {MP:.2f}% do total.')

print('x-'*5 , '07.2' , 'x-'*5)

import random
import time
print('---Simulador de dados---')
print('Rolando 100 dados...')
time.sleep(1.5)
faces = [0]*7
lancamentos = 100
for _ in range(lancamentos):
    resultado = random.randint(1,6)
    faces[resultado] += 1
print('---Resultado---')
for face in range(1,7):
    vezes = faces[face]
    print(f'A face {face} apareceu {vezes} vezes.')
    

