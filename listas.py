#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('Python', 'Java', 'Figma', 'css', 'klotin', 'mobile',
            'computer', 'androind', 'phone', 'ios', 'learn')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos:', end='')
for letra in palavras:
    if letra.lower() in 'aeiou':
        print(letra, end='')


#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lista = []
lista.append(int(input('Digita um numero:  ')))
lista.append(int(input('Digita um numero:  ')))
lista.append(int(input('Digita um numero:  ')))
lista.append(int(input('Digita um numero:  ')))
lista.append(int(input('Digita um numero:  ')))
print(f'Voce digitou os valores {lista}')
print(f'O maior valor foi {max(lista)} na opção {lista.count(max(lista))}')
print(f'O menor valor foi {min(lista)} na opçao {lista.count(min(lista))}')
print(lista)


# #Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
num = []

while True:
    # a entrada de dado que o usuario vai digitar
    entrada = int(input('Digita um número:   '))
    # checar se o numero esta na lista 
    if entrada not in num:
        num.append(entrada)
        print('Adicionado com sucesso.....')
    else:
        print('O valor já exists. Não adicionado....')

    # perguntar para o usuario se ele quer continuar ou parar 
        continuar = input('Você quer continuar? [S/N]')
    
    # check the user if they want to continue
        if continuar in 'Ss':
            print('Continua...')
        elif continuar in 'Nn':
            print('Finalizou')
            break
        else:
            print('Invalido, digita novamente S ou N ')
# print the unique numbers in ascending order
print(sorted(num))
