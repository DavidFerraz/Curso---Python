# %%

count = 1

while count <= 10:
    print("Fodase!", count)
    count += 1# count = count + 1

# %%

while True:

    senha = input("Entre com a senha: ")

    if senha == "fodase":
        break

    elif senha == "teozinho":
        print("quase...")
        continue

    print("fodase")
    print("Mais um fodase")

print("Sai! Porra!")

# %%

contador = 1
while contador <= 15:

    if contador % 2 == 0:
        print(contador)
    
    contador += 1