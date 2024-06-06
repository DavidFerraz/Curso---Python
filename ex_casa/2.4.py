# Faça um programa que receba 4 notas de um aluno.
# Retorne a média dessas notas, a menor e a maior nota:
# Média: x
# Menor: y
# Maior: z

notas = []

for i in range(4):
    valor_nota = float(input(f"Insira a nota {i+1}: "))
    notas.append(valor_nota)

print(notas)

media = sum(notas)
print("Média:", media)

menor = notas[0]

for i in notas:
    if i < menor:
        menor = i

print("Menor:", menor)

maior = notas[0]

for i in notas:
    if i > menor:
        menor = i
        
print("Maior:", maior)   
    