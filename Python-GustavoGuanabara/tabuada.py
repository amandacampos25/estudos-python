#Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
#num = int (input('Digite um número para ver a tabuada: '))
#for c in range(1, 11):
#    print('{} x {:2} = {}'.format(num, c, num*c))

while True:
    num = int (input('Digite um número para ver a tabuada: '))
    if num < 0:
        break
    print('-'*30)
    for c in range(1, 11):
        print(f'{num} x {c} = {num*c}')
    print('-'*30)

print('Você digitou um número negativo. Programa encerrado!')