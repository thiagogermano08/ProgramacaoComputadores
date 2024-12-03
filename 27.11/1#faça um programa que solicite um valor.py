1#faça um programa que solicite um valor e calcule seu fatorial 

import sys 
N = int(input('digite seu valor até 5:'))

if N < 0:
   sys.exit('informe n >=0')
if N == 0 or N == 1:
   sys.exit (f'{N} = 1')
fatorial = 1
contador = N


while contador < 1:
    fatorial *= contador 
    contador -= 1

    print (f'{N} = {fatorial}')