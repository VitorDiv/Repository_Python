#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

Letra = input('Digite uma letra, M ou F: ').upper()

if Letra == 'M':
    print('Masculino')
elif Letra == 'F':
    print('Feminino')
else:
    print('Sexo Inválido')
