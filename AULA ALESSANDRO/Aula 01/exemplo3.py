# EXEMPLO 3
print('EXEMPLO 3: algoritmo em python que leia a quantidade de dinheiro e exiba na tela em: dolar, euro e libra esterlina.') 
print()
# ENTRADA
montante = float(input('Qual será o montante analisado(Em reais)? '))
dolar = montante * 4.97
print(f'Seu montante em dolar é igual a: {dolar: .2f}')
euro = montante * 5.39
print(f'Seu montante em euro é igual a: {euro: .2f}')
libra = montante * 6.28
print(f'Seu montante em Libra esterlina é igual a: {libra: .2f}')
