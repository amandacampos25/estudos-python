#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = int(input('Digite um número: '))

# // remove números da direita
# % 10 pega o último dígito restante

u = num // 1 % 10 #unidade
d = num // 10 % 10 #dezena
c = num // 100 % 10 #centena
m = num // 1000 % 10 #milhar
print('Análisando o número {}'.format(num))
print('*' * 25)
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
print('*' * 25)