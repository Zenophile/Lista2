'''Faça um Programa que peça para entrar com um ano com 4 dígitos e determine se o mesmo é ou não
bissexto. Obs.: identificar as regras para um ano ser ou não bissexto na internet. Faça três versões usando
apenas:'''

ano = int(input("digite um ano de 4 dígitos\n"))
bissexto = False
print("Primeiro exemplo \n")
if ano % 4 == 0:
    print("esse é um ano bissexto")
else:
    print("Não é um ano bissexto")
print("\nSegundo exemplo \n")
if ano % 4 == 0:
    bissexto = True


if bissexto:
    print("esse é um ano bissexto")
else:
    print("Não é um ano bissexto")

print("\nTerceiro exemplo \n")
if ano % 4 == 0:
    print("esse é um ano bissexto")
elif (ano % 4 > 0):
    print("Não é um ano bissexto")
