# Considere a seguinte lista:
# [123, 435, 987, 1984, 2, 19, 423, -178, 320]

# Faça um programa que retorne a posição do menor e do maior valor encontrado:

# O maior valor está na posição x
# O menor valor está na posição y


lista = [123, 435, 987, 1984, 2, 19, 423, -178, 320]

menor = 0
maior = 0

for i in range(1, len(lista)):
    if lista[i] < lista[menor]:
        menor = i
    elif lista[i] > lista[maior]:
        maior = i

# menor_posicao = lista.index(menor)
# print("Menor:", menor_posicao)
        
# maior_posicao = lista.index(maior)
# print("Maior:", maior_posicao)

print("O maior valor está na posição:", menor)
print("O menor valor está na posição:", maior)

