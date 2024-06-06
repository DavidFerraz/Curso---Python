# Faça um programa que vende uma garrafa de água:
# Se o cliente escolher água mineral natural, será cobrado R$1,50
# Se o cliente escolher água mineral com gás, será cobrado R$2,50
# Altere o programa anterior para considerar a quantidade de água

escolha = input("Você gostaria de uma garrafa de água mineral ou com gás? [mineral/gas]: ")
quantidade = int(input("Quantas águas você deseja? "))  
valor_total = 0

if escolha == "mineral":
    valor_total = quantidade * 1.50  
elif escolha == "gas":
    valor_total = quantidade * 2.50 
else:
    print("Faça uma escolha válida!")

print("Você me deve R$", valor_total, sep="")