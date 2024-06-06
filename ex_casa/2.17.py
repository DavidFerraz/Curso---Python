# Escreva um programa que solicite ao usuário uma palavra e verifique se a palavra é um palíndromo (ou seja, é a mesma palavra quando lida de trás para frente).

palavra = input("Digite uma palavra: ").lower()

palavra_sep = palavra.split()

for i in palavra_sep:
    palavra_invertida = i[::-1]

print(palavra_invertida)

if palavra == palavra_invertida:
    print(f"A palavra {palavra} é um palíndromo")
else:
    print(f"A palavra {palavra} não é um palíndromo, de trás para frente fica {palavra_invertida}")