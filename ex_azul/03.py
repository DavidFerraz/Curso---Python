# Faça o programa de uma sorveteria, onde o usuário pode escolher:
# Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
# Sabor do sorvete: morango, creme, chocolate
# Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)

sorvete = input("Qual o tipo de sorvete gostaria? [casquinha/cascão/cestinha]: ")
sabor = input("Qual sabor do sorvete? ")
cobertura =  input("Qual o o sabor da cobertura? [caramelo/morango/chocolate]")
valor_sorvete = 0

if sorvete == "casquinha":
    valor_sorvete = 1.50
    if cobertura != "":
        valor_sorvete +=  + 1.50  
elif sorvete == "cascão":
    valor_sorvete = 2.50
    if cobertura != "":
        valor_sorvete += + 1.50
elif sorvete == "cestinha":
    valor_sorvete = 4.00
    if cobertura != "":
        valor_sorvete += 1.50
else:
    print("Faça uma escolha válida!")

if cobertura == "":
    cobertura = "sem cobertura"

print("O seu sorvete de", sorvete, "com sabor de", sabor, "e cobertura", cobertura, "ficou no valor de R$", valor_sorvete)