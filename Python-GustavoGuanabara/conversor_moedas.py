#cotação do dia 07/09/2026

#moedas = ('Dólar', 'Euro', 'Libra')
dolar = 5.33
euro = 5.95
libra = 6.95

print('*'*30)
real = float(input('Digite um valor em reais: '))
#print('O valor em dólares é R${}'.format(dolar*real))
print('*'*30)
print('''Escolha uma opção:
[ 0 ] DOLAR
[ 1 ] EURO
[ 2 ] LIBRA''')
print('*'*30)
cotacao = int(input('Qual moeda voce quer? '))
print('*'*30)
if cotacao == 0:
    print('O valor em dólar é ${:.2f}'.format(real/dolar))
elif cotacao == 1:
    print('O valor em euro é €{:.2f}'.format(real/euro))
elif cotacao == 2:
    print('O valor em libra é £{:.2f}'.format(real/libra))
else:
    print('Opção invalida!')
