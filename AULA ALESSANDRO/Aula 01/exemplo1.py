# EXEMPLO 1
print('EXEMPLO: Escrever um algoritmo em Python que leia de um (1) aluno sua nota do 1º e 2º bimestre e exiba na tela sua média semestral.') 
print()
# ENTRADA
nota1 = float(input('Qual foi a sua nota no primeiro bimestre? '))
nota2 = float(input('E qual foi a sua nota no segundo bimestre? '))
# PROCESSAMENTO
media = (nota1+nota2) / 2
print()
# SAIDA
print(f'Sua média semestral foi de: {media} pontos')
