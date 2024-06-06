# Faça um programa que verifique se a pessoa pertence à família “calvo” ou “silva”.

nome = input("Digite seu nome completo: ")

nome = nome.lower()
#for i in range(nome):
if "calvo" in nome or "silva" in nome:
    print("Pertence a familia Calvo ou Silva")
else:
    print("Não pertence a nenhuma das familias!")