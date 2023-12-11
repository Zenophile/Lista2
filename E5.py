'''Faça um Programa que leia três números e mostre-os em ordem decrescente. Usando apenas:
o If e else
o If, else e operadores lógicos
o If e elif'''

n1 = int(input("Digite o primeiro número"))
n2 = int(input("Digite o segundo número"))
n3 = int(input("Digite o terceiro número"))

print("Primeiro exemplo \n")
if n1 >= n2 and n1 >= n3:
    if 2 >= n3:
        print(n1, n2, n3)
    else:
        print(n1, n2, n3)
else:
    if n2 >= n1 and n2 >= n3:
        if n1 >= n3:
            print(n2,n1,n3)
        else:
            print(n2,n3,n1)
    else:
        if n1 >= n2:
            print(n3,n1,n2)
        else:
            print(n3,n2,n1)

print("\nsegundo exemplo \n")


if n1 >= n2 and n1 >= n3:
    if n2 >= n3:
        print(n1,n2,n3)
    else:
        print(n1,n3,n2)
if n2 >= n1 and n2 >= n3:
    if n1 >= n3:
        print(n2, n1, n3)
    else:
        print(n2, n3, n1)
if n3 >= n1 and n3 >= n2:
    if n1 >= n2:
        print(n3,n1,n2)
    else:
        print(n3,n2,n1)


print("\nterceiro  exemplo \n")


if n1 >= n2 and n1 >= n3:
    if n2 >= n3:
        print(n1,n2,n3)
    else:
        print(n1,n3,n2)
elif n2 >= n1 and n2 >= n3:
    if n1 >= n3:
        print(n2, n1, n3)
    else:
        print(n2, n3, n1)
elif n3 >= n1 and n3 >= n2:
    if n1 >= n2:
        print(n3,n1,n2)
    else:
        print(n3,n2,n1)
