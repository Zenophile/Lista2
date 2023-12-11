 #1. Faça um Programa que peça dois números e imprima o maior deles.

numero1 = int(input("Digite o primeiro número  \n " ))
numero2 = int(input("Digite o segundo número \n " ))

if numero1 > numero2:
    print(numero1)
elif numero1 < numero2:
    print(numero2)
else:
    print("\nOs números são iguais.")
