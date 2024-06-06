# Escreva um programa que solicite ao usuário duas strings e as concatene em uma única String.
# Em seguida, exiba a String resultante.

dados = dict(nome = input("Digite o seu nome: "),
             sobrenome = (input("Digite o seu sobrenome: ")))

                
print(dados["nome"] + " " + dados["sobrenome"])
