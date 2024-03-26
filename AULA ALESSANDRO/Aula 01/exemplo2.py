# EXEMPLO 2
print('EXEMPLO 2: Escrever um algoritmo em Pythom que leia a medida de uma barra em centímetros e exiba na tela seu comprimento em POLEGADAS E PÉS') 
print()
# ENTRADA
comprimento = float(input('MEDIDA DA BARRA (EM CENTÍMETROS): '))
comprimento = comprimento / 2.54
print('MEDIDA DA BARRA EM:')
print(f'EM POLEGADAS: {comprimento: .2f}')
comprimento = comprimento * 0.08
print(f'EM PÉS: {comprimento: .2f}')

