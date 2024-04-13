#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

while True:
    nome = input('Qual e o seu nome? ')
    if len(nome) > 4:
        break
    else:
        print('Nome deve ter mais que 4 caracteres')

while True:
    idade = int(input('Qual e a sua idade? '))
    if idade >= 0 and idade <= 150:
        break
    else:
        print('Idade deve estar entre 0 e 150')
while True:
    salario = float(input('Qual e o seu salário? '))
    if salario > 0:
        break
    else:
        print(f'Seu salario e {salario}')
while True:
    sexo = input('Qual e o seu sexo? ')
    if sexo == 'f' or sexo == 'm':
        break
    else:
        print(f'O seu sexo e {sexo}')

while True:
    estado_civil = input('Qual e o seu estado civil? ')
    if estado_civil =='s' or estado_civil == 'c' or estado_civil == 'v' or estado_civil == 'd':
        break
    else:
        print(f'O seu estado civil e {estado_civil}')


#1-Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.


nota = int(input('Nota? '))

while (0,10):
    if nota > 10:
        print('Nota e inválida')
    elif nota < 10:
        print('Nota válida')
    break
print('Fim')

#2-Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
#mostrando uma mensagem de erro e voltando a pedir as informações

usuario = input('Qual e o seu nome? ')
senha = input('Qua e a sua senha? ')

while True:
    if usuario == senha:
        print('Sua senha não pode ser o seu nome!')
    elif usuario != senha:
        print('Sua senha foi liberada!')
    break
print('Fim da verificação')


#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de 
#B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
#Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

pop_a = int(input('Qual a população do país A? '))
pop_b = int(input('Qual a população do país B? '))

while True:
    if pop_a > pop_b:
        print('A população do país A ultrapassa a população do país B')
        break
print('fim')
#Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.

for i in range(1,21):
    print(i)



from random import randint 
from time import sleep # faz o programa pusar para pensar 
computer = randint(0, 5) #faz o computador pensar 
print('-----'*20)
print('Vou pensar em um numero 0 e 5. Tenta adivinhar....')
print('-----'*20)
jogador = int(input('Em que numero ele pensei? '))
sleep(3) #tempo para o programa pensar vc pode colocar qualquer número
if jogador == computer:
    print('Parabens! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no numero {} e não no {}'.format(computer, jogador))


while True:
    jogador = int(input('Qual nùmero?  '))
    computer = randint(0, 11)
    if computer == jogador:
        print('Você venceu o jogo')
        break
    else:
        print('TENTA NOVAMENTE')
print('FIM')
