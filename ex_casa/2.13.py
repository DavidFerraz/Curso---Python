# Faça um programa que receba um número e exiba seu fatorial.

numero =  int(input("Digite o numero da fatorial: "))
fatorial = 1

for i in range(1,numero+1):
    fatorial = fatorial * i

print(fatorial)