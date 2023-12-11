'''Faça um Programa que verifique se uma letra digitada é vogal ou consoante. Usando apenas:
o If e else
o If, else e operadores lógicos
o If e elif'''

letra = str(input("digite uma letra \n "))
vogal = False
print("exemplo 1 \n")

if letra.lower() in 'aeiou':
    print('é uma voga\n')
else:
    print("é uma consoante\n")

print("exemplo 2 \n ")

if letra.lower() in 'aeiou':
    vogal = True
if vogal == True:
    print("é uma vogal\n")
else:
    print('é uma consoante\n')

print("exemplo 3 \n")

if letra.lower() in 'aeiou':
    print('é uma vogal')
elif letra.lower() in 'qwrtypsdfghjklçzxcvbnm':
    print('é uma consoante')


