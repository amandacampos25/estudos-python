from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('=-' * 15)
print('''Escolha uma opção:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int (input('Qual é a sua jogada?'))

print('=-' * 15)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
sleep(0.5)

print('=-' * 15)
print('O computador escolheu: {}'.format(itens[computador]))
print('O jogador escolheu: {}'.format(itens[jogador]))

if computador == 0: #computador jogou pedra
    if jogador == 0:
        print('Empatou!')
    elif jogador == 1:
        print('Jogador Ganhou!')
    elif jogador == 2:
        print('Computador Ganhou!')       

elif computador == 1: #computador jogou papel
    if jogador == 0:
        print('Computador Ganhou!')
    elif jogador == 1:
        print('Empatou!')
    elif jogador == 2:
        print('Jogador Ganhou!')

elif computador == 2: #computador jogou tesoura
    if jogador == 0:
        print('Jogador Ganhou!')
    elif jogador == 1:
        print('Computador Ganhou!')
    elif jogador == 2:
        print('Empatou!')

print('=-' * 15)