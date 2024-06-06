# Escreva um programa que solicite ao usuário um nome e uma idade, e crie um dicionário com essas informações.
# Em seguida, exiba o dicionário.

dados = dict(nome = input("Digite o seu nome: "),
             idade = int(input("Digite a sua idade: ")))

                
print(dados.items())