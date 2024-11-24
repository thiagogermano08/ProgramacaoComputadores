#6. (Valor: 20 pontos) Com base na nova legislação da Previdência Brasileira, regulamentada pela Lei
#omplementar nº 1354/2020 e pela Emenda à Constituição nº 49/2020, desenvolva um programa em
#Python que solicite as seguintes informações de uma pessoa:

#• Sexo da pessoa (masculino/feminino).
#• Data de nascimento da pessoa (no formato DD/MM/AAAA).
#• Data de início da contribuição previdenciária da pessoa (no formato DD/MM/AAAA).

#O programa deve então calcular e exibir a data em que a pessoa poderá se aposentar, considerando as
#seguintes regras:

#• Aposentadoria por Idade:
#o Homens podem se aposentar aos 65 anos de idade.
#o Mulheres podem se aposentar aos 62 anos de idade.
#o É necessário ter pelo menos 15 anos de contribuição.

# Aposentadoria por Tempo de Contribuição:
#o Homens podem se aposentar após 35 anos de contribuição.
#o Mulheres podem se aposentar após 30 anos de contribuição.

#Implemente o programa em Python para calcular a data de aposentadoria e exibi-la como resultado.

#Dica: Utilize as bibliotecas datetime e dateutil.

from datetime import datetime 
from dateutil.relativedelta import relativedelta 

def calcular_data_aposentadoria(sexo, data_nascimento, data_inicio_contribuição):
#lembrar que strptine é para coverter a data e hora em um objeto
    data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")

    data_inicio = datetime.strptime(data_inicio_contribuição, "%d/%m/%Y")
#lower é para ignorar formatação maiuscula e minuscula.
    if sexo.lower() == 'masculino':
       idade_minima = 65 
       tempo_contribuição_minimo = 35
    elif sexo.lower() == 'feminino':
        idade_minima = 62 
        tempo_contribuição_minimo = 30
    else:
        return "sexo invalido. use 'masculino' ou 'feminino'."

    data_aposentadoria_idade = data_nascimento + relativedelta(years=idade_minima)

    data_aposentadoria_tempo = data_inicio + relativedelta(years=tempo_contribuição_minimo)

    tempo_min_contribuição = 15
    data_min_contribuiçâo = data_inicio + relativedelta(years=tempo_min_contribuição)

    if data_aposentadoria_idade < data_min_contribuiçâo:
        data_aposentadoria_idade = data_min_contribuiçâo
 #max destaca o valor maior 
    data_aposentadoria = max(data_aposentadoria_idade, data_aposentadoria_tempo)
#return traz novamente o resultado para ser usado em outra função
    return data_aposentadoria.strftime ("%d/%m/%Y")

sexo = input('sexo (Feminino) ou (Masculino):')
data_nascimento = input('qual sua data de nascimento (dd/mm/aaaa):')
data_inicio_de_contribuição = input('data de inicio de contribuição (dd/mm/aaaa)')
resultado = calcular_data_aposentadoria(sexo, data_nascimento, data_inicio_de_contribuição )

print (f'a data prevista mais proxima será: {resultado}')


 #obs:não está considerando os 15 anos minimo para se aposentar. não consigo indentificar o por que. 
 