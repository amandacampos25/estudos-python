#Faça um programa que leia algo do teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela
palavra = input('Digite algo: ')

print('O tipo primitivo é: ', type(palavra))
print('É alfabético?: ', palavra.isalpha())
print('É númerico?: ', palavra.isnumeric())
print('Está em maiúsculo?: ', palavra.isupper())
print('Está em minúsculo?: ', palavra.islower())
