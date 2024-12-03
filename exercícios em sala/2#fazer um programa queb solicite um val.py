2#fazer um programa queb solicite um valor inteiro positivio e (N) e imprima os N primeiros elementos da sequência de fibonacci
import sys 

n = int(input('digite seu numero'))

if n <=0:
    sys,exit ('informe n positivo')

anterior, atual = 0, 1
contador =0 

while contador <=n:
 
    print (atual,end=';')
anterior , atual = atual, = atual+anterior 
contador +=1