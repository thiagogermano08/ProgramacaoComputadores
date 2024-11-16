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

def dias_ate_data(dia, mes):

    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dias_anteriores = sum(dias_por_mes[:mes-1])
    dias_totais = dias_anteriores + dia
    return dias_totais

dia_inicial = int(input('Dia inicial: '))
mes_inicial = int(input('Mês inicial: '))
dia_final = int(input('Dia final: '))
mes_final = int(input('Mês final: '))

if (mes_inicial < mes_final) or (mes_inicial == mes_final and dia_inicial <= dia_final):
    dias_inicial = dias_ate_data (dia_inicial, mes_inicial)
    dias_final = dias_ate_data (dia_final, mes_final)

    dias_decorridos = dias_final - dias_inicial

    print(f'Quantidade de dias entre as datas: {dias_decorridos} dias')
else:
    print(f'A data inicial deve ser anterior ou igual à data final.')  