'''
Faça um algoritmo para ler três números
 e imprimir a soma, média e produto dos números lidos.
'''
6
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

soma = n1 + n2 + n3
media = soma / 3
produto =  n1 * n2 * n3

print(f'{n1} + {n2} + {n3} = {soma}')
print(f'A média de {n1}, {n2} e {n3} = {media}')
print(f'{n1} x {n2} x {n3} = {produto}')

