#Atividade 01
n1,n2 = input('Digite dois nomes:\n').split(',')
def funcao(fnome):
    print(f'Olá {fnome}, seja bem vindo!'  )
funcao(n1)
funcao(n2)

#Atividade 02
def funcao(região = 'Norte'):
    print(f'Eu moro na região {região}')
funcao('Sul')
funcao('Leste')
funcao('Oeste')
funcao()

#Atividade 03
def funcao(comida):
    for i in comida:
        print(i)
frutas = ['maça', 'goiaba', 'mexirica', 'uva']
funcao(frutas)

#Atividade 04
dicionario = {'nome1': input('Qual seu nome?:\n'),
            'nome2': input('Qual seu nome?:\n'),
            'nome3': input('Qual seu nome?:\n'),
            'cidade1': input('Qual cidade você mora?:\n'),
            'cidade2': input('Qual cidade você mora?:\n'),
            'cidade3': input('Qual cidade você mora?:\n')
            }
def funcao(nome,cidade):
    print(f'Olá {nome}. Em {cidade} faz 38°!')
funcao(nome = dicionario['nome1'],cidade = dicionario['cidade1'])
funcao(nome = dicionario['nome2'],cidade = dicionario['cidade2'])
funcao(nome = dicionario['nome3'],cidade = dicionario['cidade3'])

#Atividade 05
#Meu jeito:
n1,n2 = input('Digite dois números inteiros:\n').split(',')
numero1 = int(n1)
numero2 = int(n2)
def funcao():
    print(f'A soma de {numero1} com {numero2} é: {numero1 + numero2}')
funcao()

#Professor:
def soma(a,b):
    res = a + b
    return res
print(soma(10,20))
print(soma(5,500))
print(soma(150,30))

#Atividade 06
def cidades(*cid):
    print(cid)
cidades('Frutal' , 'Barretos' , 'Rio Preto')

print('x-x' * 10)

def cidades(*cid):
    print(cid[2])
cidades('Frutal' , 'Barretos' , 'Rio Preto')

print('x-x' * 10)

def cidades(*cid):
    for x in cid:
        print(x)
cidades('Frutal' , 'Barretos' , 'Rio Preto')

print('x-x' * 10)

def tri_recursao(i):
    if(i>0):
        resultado = i+tri_recursao(i-1)
        print(resultado)
        return resultado
    else:
        resultado = 0
        return resultado
print('\nRecursão não sei o que')
tri_recursao(6)


