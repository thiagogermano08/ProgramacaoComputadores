#Uma família fez uma viagem de carro e quer detalhes sobre o desempenho do veículo.
#Faça um programa que pergunta: o momento inicial da partida (hora e minuto), o momento de chegada
#(hora e minuto), o número de segundos parados para descanso, o número de litros de combustível gasto
#(em l), o preço do litro de combustível (em R$) e a distância percorrida (em Km);
#Após receber os dados, o programa informa dados típicos de um computador de bordo:


partidah = float(input('momento inicial da partida (em hora)'))
partidam = float(input('momento inicial da partida (em minuto)'))
chegadah = float(input('momento de chegada(em hora)'))
chegadam = float(input('momento de chegada(en minutos)'))
litros_gastos = float(input('número de litros de combustível gasto(em l)'))
preço_por_L = float(input('preço do litro de combustível (em R$)'))
distância_percorrida = float(input('distância percorrida (em Km)'))
tempo_de_descanso = float(input('o número de segundos parados para descanso'))

#a) o tempo de viagem (em segundos)
tempo_final_partida_s = ((partidah * 60) + partidam) * 60
tempo_final_chegada_s = ((chegadah * 60) + chegadam) * 60
tempo_da_viagem = (tempo_final_chegada_s - tempo_final_partida_s) + tempo_de_descanso

#b) a velocidade média (Km/h) global e a velocidade média em movimento (Km/h)
tempo_de_viagem_global = distância_percorrida / (tempo_da_viagem/ 60) / 60
velocidade_media = distância_percorrida / (tempo_da_viagem / 60) / 60 

#c) o custo da viagem com combustível (em R$)
custo_de_viagem = preço_por_L * litros_gastos 

#d) o desempenho do carro (em Km/l, l/h e R$/Km).



