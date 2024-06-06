# Faça um programa que receba um número. Este número corresponde a uma posição na sequência de Fibonacci: 1, 1, 2, 3, 5,...
# Exiba o número da sequência cuja posição foi informada:
# 	A posição x corresponde ao número y

posicao = int(input("Digite a posição que deseja saber na sequência de Fibonacci: "))

seq_fibonacci = [1 , 1, 2]

for i in range(3, posicao):                                            
    seq_fibonacci.append(seq_fibonacci[-1] + seq_fibonacci[-2])

print(f"A posição {posicao} corresponde ao número {seq_fibonacci[posicao-1]}")