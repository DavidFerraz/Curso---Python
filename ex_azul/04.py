# Faça um programa que verifique se a pessoa pertence à família “calvo”.

nome = input("Entre com seu nome completo: ")

nome = nome.lower()

if "calvo" in nome:
    print("Você pertence a familia Calvo")
else:
    print("Você não pertence a familia Calvo!")
