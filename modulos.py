#import math
#num = float(input('Pedir um valor:  '))
#print('O valor digitado foi {} e a sua porção inteira e {}'.format(num, num))

num = float(input('Pedir um valor: '))
print('O valor digitado foi {} e a sua porção'.format(num, int(num)))


#Catetos e Hipotenusa

co = float(input('Comprimento do Cateteto Oposto: '))
ca = float(input('Comprimento do Cateteto Adverso: '))
h1 = (co ** 2 + ca ** 2) ** 1/2
print(f'O resultado do cateto oposto {co} e o resultado cateto adversente {ca} final {h1}')

#usando import
from math import hypot

co = float(input('Comprimento do Cateteto Oposto: '))
ca = float(input('Comprimento do Cateteto Adverso: '))

h1 = hypot(co, ca)

print(f'O resultado do cateto oposto {co} e o resultado cateto adversente {ca} final {h1}')


# import seno, cosseno e tangente
import math
angulo = float(input(': '))
seno = math.sin(math.radians(angulo))
print(f'O angulo de {angulo} tem seno de {seno:.2f}')
conseno = math.cos(math.radians(angulo))
print(f'O angulo de {angulo} tem consseno de {conseno:.2f} ')
tangente = math.tan(math.radians(angulo))
print(f'O angulo {angulo} tem tangente de {tangente:.2f}')

#com import
from random import choice
n1 = str(input('Primeiro aluno:  '))
n2 = str(input('Segundo aluno:  '))
n3 = str(input('Terceiro aluno:  '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]

escolhido = choice(lista)
print(f'O aluno escolhido foi {escolhido}')


#sorteando uma ordem aleatorio e embaralhar

from random import shuffle
name1 = str(input('Name: '))
name2 = str(input('Name: '))
name3 = str(input('Name: '))
name4 = str(input('Name: '))

listal = [name1, name2, name3, name4]
shuffle(listal)
print('A ordem de apresentação será ')
print(listal)

#tocando um arquivo  MP3 tocando musica no python
#import pygmy



# Manipulando texto manipulação cadeias de texto 
# fatiamento e pegar uma string e cortar join() frase[8] entre colcheites coloca o indice pra indicar

#Cria um programa que leia o nome completo de uma pessoa e mostra:
#O nome com todas as letras maiusculas.
#o nome com todos minusculas
# quantas letras ao todos (sem considerar )
#Quantas letras tem o primeiro nome

nome = str(input('Qual e o seu nome? '))
print(nome.upper())
print(nome.lower())
print(nome.strip())
print(len(nome[:6]))

#Faça um program que leia um numero de 0 a 9999 e mostra na tela cada um dos digitos separados
#digita um numero 1834
#unidade 4
#dezena 3
#centena : 8
# milhar 1

number = int(input('Digita um numero:   '))

unidade = number // 1 % 10
dezena = number // 10 % 10
centena = number // 100 % 10
milhar = number // 1000 % 10

print(f'Unidade: {unidade} \n {dezena} \n {centena} \n {milhar}')

#Cria um programa que lea o nome da cidade e diga se ela começa ou nao com a letra são
cidade = str(input('Qual e o nome da cidade?  '))
if 'são' in cidade:
    print(f'O nome da cidade tem "são" {cidade}')

#Cria um programa que leia o nome de uma pessoa e diga se ela tem silva no nome
pessoa = str(input('Seu nome:   '))

if'silva' in pessoa:
    print(f'Seu nome tem silva no nome {pessoa}')

# Faça um programa que leia uma frase pelo teclado e mostra:
#quantas vezes aparece a letra 'r'
#em que posição ela aparece a primeira vez
#em que posição ela aparece a uktima vez

frase = str(input('Via teclado:   '))

print(frase.count('r'))
print(frase.find('r'))
print(frase.find('r', 1))

#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro nome e o ultimo0 nome separadamente
# ana maria souza
#ana
#souza

souza = str(input('Nome completo:   '))
no = souza.split()
print(no[0])
print(no[len(no)-1])





