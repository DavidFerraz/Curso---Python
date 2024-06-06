# Faça um programa que receba um número. Verifique se o número informado é par ou ímpar. Exiba o resultado da seguinte maneira:
# 	O número x é impar
# ou
# 	O número x é par

numero = int(input("Entre com o numero: "))

if numero % 2 == 0:
    print("O número", numero, "é par")
elif numero % 2 != 0:
    print("O número", numero, "é impar")