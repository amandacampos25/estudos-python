#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep

computador = randint(0,5) #faz o computador sortear o numero
print('-=-' * 25)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar qual é!')
print('-=-' * 25)
jogador = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(3)
if jogador == computador:
    print('Parabens! Você me venceu!')
else:
    print('Eu ganhei! Pensei no número {} e não no número {}'.format(computador, jogador))