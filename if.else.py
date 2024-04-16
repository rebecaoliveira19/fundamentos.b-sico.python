number =  int(input('Qual e o numero? '))
more = int(input('Qual e o numero?   '))

if number > more:
    print('Este número e superior')
elif more > number:
    print('Este número e maior')
else:
    print('Fim')

#exemplo estrutura de controle
nome = str(input('Qual é seu nome?  '))
if nome == 'Eleonor':   #condição simples estutura usando apenas if 
    print('Que nome bonito')
elif nome == 'pedro' or nome == 'maria': # usando elif condição composta
    print('Seu nome e bem popular no Brasil')
elif nome in 'Ana':
    print('Seu nome e bonito e feminino')
else: # else e opcional se voce quiser usar ou não usar
    print(f'Tenha um bom dia, {nome}!')


# 1- escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
# calcule o valor da prestação mensal sabendo que ela não pode axceder 30% do salario emprestimo será negado
    
valor_casa = float(input('Qual e o valor da casa?   '))
salario =    float(input('Qual e o seu salario?   '))
parcelas = int(input('Quantos anos vai pagar?  '))

calcular = valor_casa / (parcelas*12)
verificar = salario * 30 / 100

if salario <= verificar:
    print('O emprestimo pode ser concedido')
else:
    print('O emprestimo Negado!')

# 2- Escreva um programa que leia um numero inteiro qualquer e peça para usuario escolher qual será a base da conversão:
    # -1 para binário
    # -2 para octal
    # -3 para hexadecimal

print('Qual conversão voce gostaria 1[binario] ou 2[octal] 3[hexadecimal] digita um número')
number = int(input('resposta: '))

if number == 1:
    print(bin(number))
elif number == 2:
    print(oct(number))
elif number == 3:
    print(hex(number))


# escreva um programa que leia dois numeros inteiros e compare-os mostrantando na tela uma mensagem 
    # - 0 primeiro valor é maior 
    # 0 segundo valor é maior
    # não existe valor maior, os dois são iguais

n1 = int(input(':'))
n2 = int(input(':'))

if n1 > n2:
    print(f'O primeiro valor e maior {n1} do que o segundo {n2}')
elif n2 > n1:
    print(f'O segundo valor e maior {n2} do que {n1}')
elif n1 == n2:
    print(f'Os valores são iguais {n1} e {n2}')


# faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade
    # se ele ainda vai se alistar ao serviço militar.
    # se e a hora de se alistar
    # se ja passou do tempo do alistamento
    # seu programa tambem devera mostrar o tempo que falta ou que passou do prazo

from datetime import datetime

ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = datetime.now().year
idade = ano_atual - ano_nascimento

if idade < 18:
    tempo_falta = 18 - idade
    print(f"Você ainda vai se alistar ao serviço militar. Faltam {tempo_falta} anos.")
elif idade == 18:
    print("É hora de se alistar ao serviço militar.")
else:
    tempo_passou = idade - 18
    print(f"Você já passou do tempo do alistamento. Passaram-se {tempo_passou} anos.")



#cria um programa que leia duas notas de um aluno e calcula sua media. mostrando uma mmensagem no final de acordo com a media atingida
# media abaixo de 5.0 reprovado
# media entre 5.0 e 6.9 recuperação
# media 7.0 ou superior aprovado


n1 = float(input(':'))
n2 = float(input(':'))

media = (n1 + n2) / 2

if media <= 5:
    print('reprovado')
elif media >= 5 or media >= 6:
    print('Recuperação')
elif media > 7:
    print('Aprovado')

# A confedaração nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostra sua categoria de acordo com a idade:
    
#ate 9 anos:mirim
#ate 14 anos: infantil
    #ate 19 anos: junior
    #ate 20 anos: senior
    #acima master

ano = int(input('Ano que voce nasceu?   '))
data = ano - 2024

if data <= 9:
    print('Mirim')
elif data <= 14:
    print('infantil')
elif data <= 19:
    print('junior')
elif data <= 20:
    print('senior')
elif data >= 30:
    print('master')

#Elaboracrie um programa que faça o computador jogar jokenpo com voce
pedra = input('')
papel = input('')
tisoura = input()




# escreva um programa que faça computador pensar em um numero inteiro entre 0 e 5 e peça para o usuario tentar descobrir qual foi o numero escolhido pelo computador.
#o programa devera escrever na tela se o usuario venceu ou perdeu
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

#escreva um programa que leia a velocidad e de um carro 
    # se ultrapassar 80 km/h mostre uma mensagem dizendo que ele foi multado 
    # a miulta vai custar rs 7,00 por cada km acima do limite

carro = float(input('Velocidade do carro:  '))
if carro > 80:
    print('Voce foi multado! ultrapassou do limite ')
    multa = (carro-80) * 7
    print('Você não vai pagar a multa ')


# cria um programa que leia o numero qualquer e mostra se ele e par ou impar
number = int(input('Digita um numero:  '))

if number % 2 == 0:
    print('Ele e par')
else:
    print('Ele e impar')



# desenvolve um programa que pergunta a distancia de uma viagem em km calcule o preco da passagem  cobrado
# rs 0,50 por km para viagens de ate 200km e 0,45 para viagens mais longas.

distancia = float(input('Qual e a distancia?  '))
print(f'Você esta prestes a começar uma viagem de {distancia}km')

if distancia  <= 200:
    preco =  distancia * 0.50
else:
    preco = distancia  * 0.47
print(f'E o preço da sua passagem será de R${preco:.2f}')

# faça um programa que leia ano qualquer e mostra ele e bissexto
from datetime import date
ano = int(input(':'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} e BISSEXTO')
else:
    print(f'O ano {ano} não é bissexto')


# faça um programa que leia tres numeros que leia qual e o maior e menor 
n1 = int(input(':'))
n2 = int(input(':'))
n3 = int(input(':'))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
#maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3


# Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento
# para salarios superiores rs 1.250,00 calcule um aumento de 20%
#para inferiores ou iguais e aumento e de 15%

salario = float(input('Qual e o seu salario?   '))

if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print(f'Quem ganhava R${salario} passa a ganhar R$ {novo} agora')

# desenvolve um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou não formar um triangulo
# principio math 


print('Analisador de triângulos')
r1 = float(input(':'))
r2 = float(input(':'))
r3 = float(input(':'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(' Os segmentos acima PODEM Formar um triângulo')
else:
    print('Os segmentos Não podem formar um Triângulo ')



# desenvolva uma logica que leia o peso e altura deuma pessoa. Calcule seu IMC e mostra o seu status de acordo 
    #abaixo de 18.5  abaixo do peso calcular o IMC
    #entre 18.5 e 25: peso ideal
    #25 ate 30 sobrepeso
    #30 ate 40 obsidade 
    # acima e 40 obsidade morbida


#calcule IMC
peso = float(input('Qual e o seu peso?    '))
altura = float(input('Qual e a sua altura?  '))

imc = peso/(altura**2)

#calcule IMC
if imc < 18.5:
    print('abaixo do peso')
elif 18 <= imc < 25:
    print('peso ideal ')
elif 25 <= imc < 30:
    print('sobrepeso')
elif 30 <= imc < 40:
    print('obsidade')
elif imc >= 40:
    print('Obsidade morbida')
else:
    print(' fim')

# Elabora um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento
    # á avista a dinheiro/cheque 10% desconto
    #  á vista no cartão 5% de desconto
    #em até 2x no cartão preço normal
    # 3x ou mais no cartão 20% de juros 
# entrada de dados 
produto = float(input('Quanto que custa?  '))
print('Formas de pagamentos')
print('[ 1 ] á vista a dinheiro/cheque')
print('[ 2 ] á vista no cartão 5% de desconto')
print('[ 3 ] 2x  no cartão')
print('[ 4 ] 3x ou mais no cartão')
res = input('Qual é a opção?')

#condição de pagamento
if res == '1':
    total = produto - (produto * 10/100)
    print(f'Você escolheu opção 1 dinheiro/cheque R${total}')
elif res == '2':
    total = produto - (produto * 5/100)
    print(f'Você escolheu opção 2 a vista no cartão R${total}')
elif res == '3':
    total = produto 
    parcela = total /2
    print(f'Você escolheu opção 3 será parcelado em 2x de R${parcela:.2f}')
elif res == '4':
    total = produto + (produto * 20 / 100)
    more = int(input('Quantas parcelas?   '))
    cela = total / more
    print(f'Você escolheu opção 4 sua compra será parcelada  de  {more} o total vai ser R${cela}')
else:
    total = 0
    print('Opção inválida tenta novamente')
    print(f'Sua compra de R${produto:.2f} vai custar o R$ {total:.2f} ')













