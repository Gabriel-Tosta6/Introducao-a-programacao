# Exercício 01
print('-----------------01-----------------')

idade = input('Qual a sua idade?:\n')

if idade.lstrip('-').isnumeric():
    idade = int(idade)
    if idade < 0:
        print('Sua idade não pode ser negativa!')
    elif idade >= 18:
        print('Você é maior de idade!')
    else:
        print('Você é menor de idade!')
else:
    print('Sua idade tem que ser composta por números inteiros!')

print('-----------------02-----------------')

# Exercício 02
print('Digite dois números inteiros, vou descobrir qual é o maior!')

n1 = input('Digite o primeiro número:\n')
n2 = input('Digite o segundo número:\n')

if n1.isnumeric() and n2.isnumeric():
    n1 = int(n1)
    n2 = int(n2)
    if n1 > n2:
        print(f'O número maior é: {n1}')
    elif n1 == n2:
        print('Os números são iguais!')
    else:
        print(f'O número maior é: {n2}')
else:
    print('Erro, você não digitou números inteiros!')

print('-----------------03-----------------')
   
# Exercício 03
n = input('Digite um número qualquer, e vou dizer se é par ou ímpar:\n')

if n.isnumeric():
    n = int(n)
    if n % 2 == 0:
        print(f'{n} é par!')
    else:
        print(f'{n} é ímpar!')
else:
    print('Você não digitou um número inteiro!')

print('-----------------04-----------------')

# Exercício 04
print('Digite três números, vou descobrir qual é o menor!')
n1 = input('Digite o primeiro número:\n')
n2 = input('Digite o segundo número:\n')
n3 = input('Digite o terceiro e último número:\n')

if n1.isnumeric() and n2.isnumeric() and n3.isnumeric():
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
    
    if n1 == n2 == n3:
        print('Os números são iguais!')
    else:
        menor = n1
        if n2 < menor:
            menor = n2
        if n3 < menor:
            menor = n3
        print(f'O menor número é: {menor}')
else:
    print('Todos os valores devem ser números inteiros!')

print('-----------------05-----------------')

# Exercício 05
from datetime import datetime

nome = input('Qual seu nome?:\n')
hora = datetime.now()
hora2 = hora.strftime('%H:%M')

if not nome.replace(" ", "").isalpha():
    print('\nSeu nome tem que ser formado apenas por letras do alfabeto, mas...')

print(f'\nAgora são {hora2}!\n')

if 6 <= hora.hour < 12:
    print(f'Bom dia, {nome}!')
elif 12 <= hora.hour < 18:
    print(f'Boa tarde, {nome}!')
elif 18 <= hora.hour < 24:
    print(f'Boa noite, {nome}!')
else:
    print(f'É madrugada, vai dormir, {nome}!')

print('-----------------06-----------------')

# Exercício 06
nota = input('Digite uma nota de 0 a 10 e eu vou te dizer como você se saiu:\n')

if nota.replace(".", "").isnumeric():
    nota = float(nota)
    if nota < 0 or nota > 10:
        print('Nota inválida!')
    elif nota <= 4:
        print('Sua nota foi ruim :(')
    elif nota <= 6:
        print('Sua nota foi regular :|')
    elif nota <= 8:
        print('Sua nota foi boa :)')
    else:
        print('Sua nota foi excelente xD')
else:
    print('A nota deve ser um valor numérico!')

print('-----------------07-----------------')

# Exercício 07
s_b = input('Digite o seu salário bruto, vou calcular o desconto do INSS:\n')

if s_b.replace(".", "").isnumeric():
    s_b = float(s_b)
    if s_b <= 0:
        print('Erro, o salário não pode ser negativo ou zero!')
    else:
        s_l = s_b - (s_b*0.11)
        print(f'Seu salário com os descontos do INSS é de: R${s_l}!')
else:
    print('O salário deve ser um valor numérico!')

print('-----------------08-----------------')

# Exercício 08
n = input('Digite um número inteiro, vou adivinhar se ele é positivo, negativo ou zero!:\n')

if n.lstrip('-').isnumeric():
    n = int(n)
    if n == 0:
        print('Seu número é 0!')
    elif n < 0:
        print('Seu número é negativo!')
    else:
        print('Seu número é positivo!')
else:
    print('O valor deve ser um número inteiro!')

print('-----------------09-----------------')

# Exercício 09
n = input('Digite um número inteiro, vou analisar se ele é multiplo de 5 e de 7:\n')

if n.lstrip('-').isnumeric():
    n = int(n)
    if n % 5 == 0 and n % 7 == 0:
        print('Seu número é múltiplo de 5 e de 7!')
    elif n % 5 == 0:
        print('Seu número é múltiplo de 5, mas não de 7!')
    elif n % 7 == 0:
        print('Seu número é múltiplo de 7, mas não de 5!')
    else:
        print('Seu número não é multiplo de 5 e nem de 7!')
else:
    print('O valor deve ser um número inteiro!')

print('-----------------10-----------------')

# Exercício 10
i = input('Me diga a sua idade que eu vou te dizer sua faixa etária:\n')

if i.lstrip('-').isnumeric():
    i = int(i)
    if i < 0:
        print('Sua idade não pode ser negativa!')
    elif i <= 12: 
        print('Você é uma criança!')
    elif i <= 17:
        print('Você é um adolescente!')
    elif i <= 29:
        print('Você é um adulto jovem!')
    elif i <= 59:
        print('Você é um adulto!')
    else:
        print('Você é um idoso!')
else:
    print('A idade deve ser um número inteiro!')

print('-----------------11-----------------')

# Exercício 11
print('Informe suas notas, vou calcular a média delas e dizer se você foi aprovado ou não!\n')
n1 = input('Informe a primeira nota:\n')
n2 = input('Informe a segunda nota:\n')

if n1.replace(".", "").isnumeric() and n2.replace(".", "").isnumeric():
    n1 = float(n1)
    n2 = float(n2)
    m = (n1 + n2) / 2
    print(f'Sua média é: {m}\n')
    if m >= 6:
        print('Aprovado! :)')
    else:
        print('Reprovado! :(')
else:
    print('As notas devem ser valores numéricos!')

print('-----------------12-----------------')

# Exercício 12
nome = input('Qual o seu nome?:\n')

if not nome.replace(" ", "").isalpha():
    print('\nSeu nome tem que ser formado apenas por letras do alfabeto, mas vamos seguir.\n')
    
idade = input('Quantos anos você tem?:\n')

if idade.lstrip('-').isnumeric():
    idade = int(idade)
    if idade <= 0:
        print('A idade digitada é incorreta.')
    elif idade >= 18:
        print(f'{nome}, você pode dirigir!')
    else:
        print(f'{nome}, você não pode dirigir!')
else:
    print('A idade deve ser um número inteiro!')

print('-----------------13-----------------')

# Exercício 13
letra = input('Digite uma letra:\n').strip().upper()

if len(letra) == 1 and letra.isalpha():
    if letra in "AEIOU":
        print(f'"{letra}" é uma vogal!')
    else:
        print(f'"{letra}" é uma consoante!')
else:
    print('Caractere inválido!')

print('-----------------14-----------------')

# Exercício 14
print('Digite a seguir os três lados de um tiângulo para descobrir qual seu tipo!\n')

l = input('Digite o primeiro lado:\n')
l2 = input('Digite o segundo lado:\n')
l3 = input('Digite o terceiro lado:\n')

if l.replace(".", "").isnumeric() and l2.replace(".", "").isnumeric() and l3.replace(".", "").isnumeric():
    l = float(l)
    l2 = float(l2)
    l3 = float(l3)
    
    if (l + l2 > l3) and (l + l3 > l2) and (l2 + l3 > l):
        if l == l2 == l3:
            print('O triângulo é equilátero!')
        elif l == l2 or l == l3 or l2 == l3: 
            print('O triângulo é isósceles!')
        else:
            print('O triângulo é escaleno!')
    else:
        print('Esses lados não formam um triângulo válido!')
else:
    print('Todos os lados devem ser valores numéricos!')

print('-----------------15-----------------')

# Exercício 15
num = input('Digite um número inteiro, vou dizer se é primo ou não:\n')

if num.lstrip('-').isnumeric():
    num = int(num)
    if num <= 1:
        print(f'{num} não é primo!')
    elif num == 2:
        print(f'{num} é primo!')
    elif num % 2 == 0:
        print(f'{num} não é primo!')
    else:
        primo = True
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                primo = False
                break
        if primo:
            print(f"{num} é primo!")
        else:
            print(f"{num} não é primo!")
else:
    print('O valor deve ser um número inteiro!')

print('-----------------16-----------------')

# Exercício 16
print('Vamos calcular seu Índice de Massa Corporal (IMC). Por favor, informe os dados abaixo:\n')

a = input('Qual a sua altura?(m):\n')
p = input('Qual o seu peso?(Kg):\n')

if a.replace(".", "").isnumeric() and p.replace(".", "").isnumeric():
    a = float(a)
    p = float(p)
    if a <= 0 or p <= 0:
        print('Altura e peso devem ser valores positivos!')
    else:
        imc = p / a**2
        if imc < 18.5:
            print('Abaixo do peso!')
        elif imc <= 24.9:
            print('Peso normal!')
        elif imc <= 29.9:
            print('Sobrepeso!')
        elif imc <= 34.9:
            print('Obesidade grau 1!')
        elif imc <= 39.9:
            print('Obesidade grau 2!')
        else:
            print('Obesidade grau 3!')
else:
    print('Altura e peso devem ser valores numéricos!')

print('-----------------17-----------------')

# Exercício 17
h = input('Que horas são agora?:\n')

if h.replace(".", "").isnumeric():
    h = float(h)
    if 0 <= h <= 5.99:
        print('Boa madrugada!')
    elif 6 <= h <= 11.99:
        print('Bom dia!')
    elif 12 <= h <= 17.99:
        print('Boa tarde!')
    elif 18 <= h <= 23.99:
        print('Boa noite!')
    else:
        print('Ops, ocorreu um erro!')
else:
    print('A hora deve ser um valor numérico!')

print('-----------------18-----------------')

# Exercício 18
n = input('Digite um número inteiro e eu vou te mostrar a tabuada dele:\n')

if n.lstrip('-').isnumeric():
    n = int(n)
    print(f"\nTabuada do {n}:\n")
    for i in range(1, 11):
        t = n * i
        print(f"{n} x {i} = {t}")
else:
    print('O valor deve ser um número inteiro!')

print('-----------------19-----------------')

# Exercício 19
n = input('Digite um número inteiro para analisarmos se é um palíndromo ou não:\n')

if n.lstrip('-').isnumeric():
    if n == n[::-1]:
        print(f"{n} é palíndromo!")
    else:
        print(f"{n} não é palíndromo.")
else:
    print('O valor deve ser um número inteiro!')

print('-----------------20-----------------')

# Exercício 20
print('Vamos descobrir se você pode votar\n')
n = input('Qual seu nome?:\n')
i = input('Qual a sua idade?:\n')

if not n.replace(" ", "").isalpha():
    print('Seu nome deve conter apenas letras, mas vamos continuar...\n')

if i.lstrip('-').isnumeric():
    i = int(i)
    if i < 0:
        print('Sua idade não pode ser negativa!')
    elif i >= 16:
        print(f'{n}, você pode votar!')
    else:
        print(f'{n}, você não pode votar!')
else:
    print('A idade deve ser um número inteiro!')

print('-----------------FIM-----------------')