
#Exercício 01
#Sem input
v_global = 10
def funcao(numero):
    print(f'{numero} multiplicado por {v_global} é: {numero*v_global}')
funcao(5)

#Com input
v_global = 2
def funcao(numero):
    i = int(input('Digite um número inteiro:\n'))
    print(f'{i} multiplicado por {numero} é: {i*numero}')
funcao(v_global)

#Exercício 02
def funcao():
    n1 = input('Digite um número:\n')
    print(f'Número armazenado na função {n1}')
funcao()

#Exercício 03
carros = ['Jetta','Golf','Palio','Celta']
carrinho = 'Hot Wheels'
def funcao(carros):
    carros[2] = carrinho
    print(carros)
funcao(carros)
print(carros)

