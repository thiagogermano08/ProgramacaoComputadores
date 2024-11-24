#(Valor: 10 pontos) O número de dias decorridos entre duas datas é importante em uma infinidade de
#situações da vida cotidiana. Faça um programa que recebe inicialmente dois valores (dia inicial e mês
#inicial), depois mais dois valores (dia final, mês final), ao final deve indicar quantos dias se passaram entre
#as datas (considere que o ano não é bissexto).

#xemplos:
#o 02 de 05 até 03 de 05 - 1 dia
#o 27 de 04 até 03 de 05 - 6 dias
#o 03 de 02 até 03 de 05 - 79 dias

#Não esqueça de verificar se a data inicial é menor ou igual à data final.

#Dica: conte o número de dias até cada uma das datas e subtraia esses números.

dia_inicial = int(input('digite seu dia inicial'))
mes_inicial = int(input('digite seu mês inicial'))
dia_final = int(input('digite seu ultimo dia'))
mes_final  = int(input('digite seu último mês'))

if mes_final == mes_inicial:
    soma_de_dias = dia_final - dia_inicial
else:
    soma_de_dias = ((mes_final - mes_inicial) * 30) - (dia_final - dia_inicial)
   
    print (f'um total de: {soma_de_dias} dias')