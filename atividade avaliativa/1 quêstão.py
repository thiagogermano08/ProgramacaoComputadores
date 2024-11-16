#Faça um programa que aceita um número de até 4 dígitos (0 a 9999) e exiba a soma dos seus algarismos.
...
numero = int(input('digite seu número até 9999:'))

if numero > 9999 or numero < 0:
    input('erro! insira outro numero.') 
else:
    M = numero // 1000
    numero = numero % 1000

    C = numero // 100
    numero =  numero % 100

    D = numero // 10
    numero = numero  % 10

    U = int(numero - D*10)

soma = M + C + D + U
print (f'o resultado da soma será: {soma}')