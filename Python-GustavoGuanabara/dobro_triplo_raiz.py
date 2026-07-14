#crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada.

num = int (input('Digite um número: '))
print('Análisando o número {}'.format(num))
print('O dobro do número {} é {}, o triplo é {} e a raiz quadrada é {:.2f}'.format(num, (num*2), (num*3), (num**(1/2))))