#5. (Valor: 15 pontos) Em um estacionamento, as tarifas são as seguintes (cumulativas):

#• Até duas horas: R$ 8,00/hora ou fração;
#• Entre três e quatro horas: R$ 5,00/hora ou fração;
#• Horas seguintes: R$ 3,00/hora ou fração.
#• Depois de 12h, o custo passa a ser fixo: R$ 30,00

#Faça um programa que leia o número de minutos que um veículo permaneceu no estacionamento e exiba
# valor a ser pago pelo responsável.

#omo exemplo, considere que o carro ficou 310 minutos no estacionamento; deve pagar: R$ 16,00 (pelas
#duas primeiras horas) + R$ 10,00 (pela terceira e quarta horas) + R$ 6,00 (pela quinta hora e fração da
#sexta hora): total de R$ 32,00

minutos = int(input('tempo de estacionamento (EM MINUTOS):'))
#transformar minutos em horas
hora = (minutos + 59) // 60
  
valor_total = 0
#aqui considerando o valor de "hora" como base em todos.  
if hora <=2:
    valor_total = hora * 2
elif hora <= 4:
    valor_total = (2 * 8) + (hora - 2) * 5
elif hora <= 12:
    valor_total = 2 * 8 + 2 * 5 + (hora - 4) * 3
else:
    valor_total = 30

print (f' seu débito será de:{valor_total:.2f}')