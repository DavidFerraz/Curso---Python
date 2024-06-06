# Faça um programa que verifique se o item que a pessoa escolheu para comprar na loja 
# está na lista: laranja, cerveja, miojo, carvão, picanha.

item = input("Qual item deseja comprar? [laranja, cerveja, miojo, carvão, picanha] ")
lista = "laranja, cerveja, miojo, carvão, picanha"


if item in lista:
    print("Pode se dirigir ao caixa, o item", item, "esta na lista!")
else:
    print("Estamos em falta!")