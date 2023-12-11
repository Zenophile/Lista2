'''Faça um Programa que leia três números e mostre o maior e o menor deles. Usando apenas:
o If e else
o If, else e operadores lógicos
o If e elif'''

n1 = int(input("Digite o Primeiro número"))
n2 = int(input("Digite o Segundo número"))
n3 = int(input("Digite o Terceiro número\n"))




print('método 2')

maior = n1 if n1 > n2 and n1 > n3 else (n2 if n2 > n3 else n3)
menor = n1 if n1 < n2 and n1 < n3 else (n2 if n2 < n3 else n3)

print(maior)
print(menor)
