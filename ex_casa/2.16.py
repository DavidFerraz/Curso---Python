# Escreva um programa que solicite ao usuário um número e exiba a tabuada desse número de 1 a 10.

numero = int(input("Digite um numero: "))

for i in range(1,11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")