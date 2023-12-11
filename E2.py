'''Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F -
Feminino, M - Masculino, Sexo Inválido.'''

letra = str(input("Digite uma letra para informar o sexo, F para feminino e M para masculino"))

letra = letra.lower()


if letra == 'f':
    print("Sexo Feminino")
elif letra == 'm':
    print("Sexo masculino")
else:
    print("Sexo inválido")

