#7. (Valor: 25 pontos) Desenvolva um código em Python que solicite ao usuário que informe os
#comprimentos dos três lados de um triângulo. Em seguida, verifique se esses comprimentos podem
#formar um triângulo. Caso afirmativo, calcule e informe os valores dos ângulos do triângulo e classifiqueo quanto aos lados e aos ângulos.

#• Instruções:

#a) Peça ao usuário para inserir os comprimentos dos três lados do triângulo.

#b) Verifique se os comprimentos fornecidos podem formar um triângulo. Caso contrário, informe
#que não é possível formar um triângulo com esses lados.

#c) Se for possível formar um triângulo, calcule os três ângulos do triângulo.

#d) Classifique o triângulo quanto aos lados (equilátero, isósceles ou escaleno) e aos ângulos
#agudo, obtuso ou retângulo).

#e) Exiba a classificação do triângulo quanto aos lados e aos ângulos.

#• Observações:

#o Para determinar se os lados fornecidos pelo usuário podem formar um triângulo, é necessário
#verificar a seguinte condição: A soma de quaisquer dois lados de um triângulo deve ser
#sempre maior que o terceiro lado.
#o Você pode usar a Lei dos cossenos para calcular os ângulos de um triângulo.
#o Para classificar quanto aos lados, verifique se os três lados são iguais (equilátero), se dois
#lados são iguais (isósceles) ou se todos os lados são diferentes (escaleno).
#o Para classificar quanto aos ângulos, verifique se um dos ângulos é maior que 90 graus
#(obtuso), se um dos ângulos é igual a 90 graus (retângulo) ou se todos os ângulos são
#menores que 90 graus (agudo).
#o Considere que os ângulos são expressos em graus.

#Desenvolva o código em Python para atender às especificações acima.

#Dica: Utilize a biblioteca math.

import math
#def 
def verificar_triangulo(l1, l2, l3):
    return l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1 

#função "degrees" usa para converter de radianos para graus e "acos" pega o cosseno inverso de um valor.
#calculo para conseguir o valor dos cossenos e 
def calcular_angulos (l1, l2, l3):
    angulo_A = math.degrees(math.acos((l2**2 + l3**2 - l1**2) / (2 * 12 * 13)))
    angulo_B = math.degrees(math.acos((l2**2 + l3**2 - l1**2) / (2 * 12 * 13)))
    angulo_C = 180 - angulo_A - angulo_B
    
    return angulo_A, angulo_B, angulo_C

def classificar_triangulo(l1, l2, l3, angulo_A, angulo_B, angulo_C):
    if l1 == l2 == l3:
        tipo_lados = "Equilátero"
    elif l1 == l2 or l1 == l3 or l2 == l3:
        tipo_lados = "isóceles"
    else:
        tipo_lados == "Escaleno"
#o "in" está inserido pois ele quem dirá se à algum angolo de 90°. "any faz o mesmo porem agora toma como base o "in"
    if 90 in (angulo_A, angulo_B, angulo_C):
        tipo_angulos = "Retangulo"
    elif any(angulo > 90 for angulo in (angulo_A, angulo_B, angulo_C)):
        tipo_angulos = "Obtuso"
    else: 
        tipo_angulos = "Agudo"
    return tipo_angulos, tipo_lados
    
    
l1 = float(input('qual dado do primeiro lado?'))
l2 = float(input('do segundo lado?'))
l3 = float(input('do terceiro lado?'))
#o "*" fara o descompactamento de uma lista, e evniará os valores separadamente 
if verificar_triangulo(l1, l2, l3):
    angulos = calcular_angulos(l1, l2, l3)
    tipo_lados, tipo_angulos = classificar_triangulo(l1, l2, l3, *angulos)

    print (f'\n classificação dos lados: {tipo_lados}')
    print (f'classificação dos angulos: {tipo_angulos}')
    print (f'ângulos do triangulo: A = {angulos[0]:.2f}°, B = {angulos[0]:.2f}°, C = {angulos[0]:.2f}°')
else:
    print(f'os dados informados não formam um triangulo.')