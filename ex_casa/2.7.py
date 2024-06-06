# Escreva um programa que crie um dicionário com nomes de frutas como chaves e seus respectivos preços como valores.
# Solicite ao usuário o nome de uma fruta e exiba o preço correspondente.

nome_fruta = input("Entre com o nome da fruta: [Maçã/Banana/Uva/Pera/Laranja/Limão/Goiaba/Abacaxi/Jaca] ")

preco_fruta = {
    "Maçã" : 1.50,
    "Banana": 2.75,
    "Uva" : 1.90,
    "Pera" : 1.25,
    "Laranja" : 0.65,
    "Limão": 1.25,
    "Goiaba": 2.15,
    "Abacaxi": 3.20,
    "Jaca" : 5.80
}

print("O valor da fruta ", nome_fruta, ": R$", preco_fruta[nome_fruta], sep="")