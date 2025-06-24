print('x-'*5 , '01' , 'x-'*5)

n = str(input('\nDigite uma palavra:\n'))

print(f'O comprimeto da palavra (string) é: {len(n)}\n')

print('x-'*5 , '02' , 'x-'*5)

n = str(input('\nDigite uma palavra:\n'))
print(f'A primeira letra da palavra digitada é: {n[0]}, e a última letra é: {n[-1]}')

print('x-'*5 , '03' , 'x-'*5)

n = str(input('\nDigite uma palavra:\n'))
print(f'Os caracteres digitados nas posições pares são: {n[::2]}')

print('x-'*5 , '04' , 'x-'*5)

n = str(input('\nDigite uma palavra/frase, vou verificar se ela é um palíndromo:\n')).strip().lower().replace(' ', '')

string_contrário = n[::-1]

if n == string_contrário:
    print(f'\n{n} é um palíndromo!\n')
else:
    print(f'\n{n} não é um palíndromo!\n')

print('x-'*5 , '05' , 'x-'*5)

n = str(input('\nDigite uma palavra que contenha a letra "A":\n')).upper().replace('A', 'O')
print(f'\nSubstituí todas as letras "A" por letras "O", e ficou: {n}\n')

print('x-'*5 , '06' , 'x-'*5)

n1 = 'A minha comida favorita é '
n2 = str(input('\nDigite sua comida favorita:\n'))
soma = n1 + n2
print(soma)

print('x-'*5 , '07' , 'x-'*5)

n = str(input('\nDigite uma palavra:\n')).lower()
invertida = n[::-1]
print(f'\nPalvra digitada: {n}, palavra digitada invertida: {invertida}\n')

print('x-'*5 , '08' , 'x-'*5)

n = str(input('\nDigite uma palavra, vou contar quantas vezes a letra "O" aparece:\n')).lower()
i = n.count('o')
print(f'A letra "O" apareceu {i} vezes!')

print('x-'*5 , '09' , 'x-'*5)

n = str(input('\nDigite uma palavra que comece com "J" e termine com "E":\n')).upper()
começo = "J"
final = "E"
if n.startswith(começo) & n.endswith(final):
    print(f'\n{n} começa com "J" e termina com "E"!\n')
elif n.startswith(começo):
    print(f'\n{n} começa com "J" mas não termina com "E"!\n')
elif n.endswith(final):
    print(f'\n{n} não começa com "J" mas termina com "E"!\n')
else:
    print(f'\n{n} não começa com "J" e nem termina com "E"!\n')

print('x-'*5 , '10' , 'x-'*5)

n = str(input('\nDigite uma frase ou um título:\n'))
primeiras = n.title()
print(f'\nA frase/titulo digitado foi: "{n}", capitalizando as primeiras letras de cada palavra fica: "{primeiras}"!\n')