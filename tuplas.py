#variavei compostas
#Tupla, listas e dicionario
# Tupla ela e imutavel: não pode alterar a variavel

lache = ('Hambuguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')
        #(   0     ,   1   ,    2   ,   3)

for cont in range(0, len(lache)):
    print(lache[cont])     # cobrir os numeros
print('SEGUNDO RODADA')

for comida in lache:
    print(f'Eu vou comer alguma coisa {comida}')
print('EU COMI MUITA COISA')
print(sorted(lache))          #sorted em ordem



#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.


#usuario = int(input('Digita um numero entre 0 ate 20:  '))
tupla = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
#user = int(input('entre 0 ate 20:  '))

while True:
    user = int(input('entre 0 ate 20: '))
    if 0 <= user <= 20:
        break
    print('TENTA NOVAMENTE')
print(f'Voce digitou o numero {tupla[user]}')

#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
        randint(1, 10), randint(1, 10),)

print('O numeros sorteados são:')
for n in numeros:
    print(f'{n}',end=' ')

print(f'\nQual foi o maior valor {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')


