# Faça um programa com uma função que recebe uma frase. Para cada palavra nesta frase, inverta a ordem das letras. Exiba o resultado:

# 	Esta é a frase original

# 	atsE é a esarf lanigiro


frase = "Esta é a frase original"

# Dividir a frase em palavras
palavra = frase.split()

palavras_invertidas = []


for i in palavra:
    palavra_invertida = i[::-1]
    palavras_invertidas.append(palavra_invertida)
    
nova_frase = " ".join(palavras_invertidas)            
print(nova_frase)