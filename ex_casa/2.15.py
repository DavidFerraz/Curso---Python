# Escreva um programa que receba uma lista de números do usuário e conte quantas vezes um número específico aparece na lista.
# Solicite ao usuário um número e exiba a contagem.

lista = []

while True:

    numero = int(input("Digite um numero: "))

    if numero != 0:   
        lista.append(numero)
        continue
    else:
        break  

exibir = int(input("Digite o numero que deseja saber a quantidade: "))
print(lista.count(exibir))