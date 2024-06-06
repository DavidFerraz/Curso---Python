# %%
# Faça um programa que calcule a raiz quadrada de um número e exiba o resultado.

numero = int(input("Entre com valor para calcular a raiz quadrada: "))

resultado = numero ** 0.5
resultado = round(resultado, 2)
print("A raiz quadrada de", numero, "é:", resultado)