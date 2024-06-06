# Faça o programa de uma sorveteria, onde o usuário pode escolher:
# Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
# Sabor do sorvete: morango, creme, chocolate
# Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)

tipo_sorvete = input("Qual o tipo de sorvete gostaria: [casquinha/cascão/cestinha] ").lower()
sabor = input("Qual sabor do sorvete: [morango/creme/chocolate] ").lower()
cobertura =  input("Qual o o sabor da cobertura: [caramelo/morango/chocolate] ").lower()

# Um dicionario com o nome do sorvete e valor atribuido a ele
sorvetes = {
    "casquinha": 1.00,
    "cascão": 2.5,
    "cestinha": 4.00
}

valor = 0


if tipo_sorvete in sorvetes:
    valor += sorvetes[tipo_sorvete]
else:
    print("Seu pedido vai vir cagado. Entre com um valor válido!")

# Um dicionario com o nome da cobertura e valor atribuido a cada cobertura
coberturas = {
    "caramelo": 1.5,
    "morango": 1.5,
    "chocolate": 1.5,
    "": 0
}

if cobertura in coberturas:
    valor += coberturas[cobertura]
else:
    print("Seu pedido vai vir cagado. Entre com um valor válido!")

print("O seu sorvete de", tipo_sorvete, "com sabor de", sabor, "e cobertura", cobertura, "ficou no valor de R$", valor)
