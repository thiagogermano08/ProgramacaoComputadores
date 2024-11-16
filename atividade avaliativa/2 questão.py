#Faça um programa que solicite ao usuário um valor decimal positivo (esse valor
# corresponde ao valor de um saque em um terminal de caixa eletrônico) e que calcule a quantidade de
# cédulas de R$ 100,00, R$ 50,00, R$ 20,00, R$ 10,00, R$ 5,00 e R$ 2,00 e de moedas de R$ 1,00, R$
# 0,50, R$ 0,25, R$ 0,10, R$ 0,05 e R$ 0,01.

saque = float(input('quanto deseja sacar?'))
if saque <=0:
    print ('insira um saldo positivo')
else: 
    print('Cédulas:')
    notas100 =  int(saque // 100)
    saque %= 100
    notas50 =  int(saque // 50)
    saque %= 50
    notas20 =  int(saque // 20)
    saque %= 20 
    notas10 =  int(saque // 10) 
    saque %= 10
    notas5 =  int(saque // 5) 
    saque %= 5
    notas2 = int(saque // 2)
    saque %= 2
    notas1 = int(saque // 1)
    saque %= 1
    print('Moedas:')
    Moedas0_50 = int(saque // 0.50)
    saque %= 0.50
    Moedas0_25 = int(saque // 0.25) 
    saque %= 0.25
    Moedas0_10 = int(saque // 0.10)
    saque %= 0.10
    Moedas0_5 = int(saque // 0.5)
    saque %= 0.5
    Moedas0_1 = round(saque / 0.1) 

    if notas100 > 0:
        print(f"Cédulas de R$ 100: {notas100}")
    if notas50 > 0:
        print(f"Cédulas de R$ 50: {notas50}")
    if notas20 > 0:
        print(f"Cédulas de R$ 20: {notas20}")
    if notas10 > 0:
        print(f"Cédulas de R$ 10: {notas10}")
    if notas5 > 0:
        print(f"Cédulas de R$ 5: {notas5}")
    if notas2 > 0:
        print(f"Cédulas de R$ 2: {notas2}")
    if notas1 > 0:
        print(f"Moedas de R$ 1: {notas1}")
    if Moedas0_50 > 0:
        print(f"Moedas de R$ 0,50: {Moedas0_50}")
    if Moedas0_25 > 0:
        print(f"Moedas de R$ 0,25: {Moedas0_25}")
    if Moedas0_10 > 0:
        print(f"Moedas de R$ 0,10: {Moedas0_10}")
    if Moedas0_5 > 0:
        print(f"Moedas de R$ 0,05: {Moedas0_5}")
    if Moedas0_1 > 0:
        print(f"Moedas de R$ 0,01: {Moedas0_1}")


