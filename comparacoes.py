'''
Faça um algoritmo para ler dois números e
 imprimir o maior, o menor ou então
   dizer se são iguais.
'''

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 > n2 :
    print(f'{n1} é maior que {n2}')
elif n1 < n2:
    print(f'{n1} é menor que {n2}')
else:
    print(f'{n1} é igual {n2}')
