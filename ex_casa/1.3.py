# Faça um programa que receba o raio de uma circunferência em centímetros.
# Retorne para o usuário qual é a área e perímetro desta circunferência no seguinte formato.
# Área:  x.xx
# Perímetro:  y.yy


raio = int(input("Insira o raio da circuferência: "))

area = 3.14 * (raio ** 2)
perimetro = 2 * 3.14 * raio

print("Área:", round(area, 3))
print("Perímetro:", round(perimetro,3))