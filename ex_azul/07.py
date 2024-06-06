# Faça um programa que conte quantas vezes a letra “a” aparece em uma palavra.

palavra = input("Entre com a palavra? ")
qtde = 0

for i in palavra:
    if i == "a":
       qtde += 1
print("A letra 'a' possui", qtde, "ocorrências na palavra", palavra)

# %%
#Outra forma de estar verificando as ocorrencia da letra 'a'
palavra = "banana"
palavra.count("a")