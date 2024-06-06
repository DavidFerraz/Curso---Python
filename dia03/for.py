# %%

for i in "Téo Calvo":

    if i == "T":
        continue

    if i == " ":
        continue

    print(i)

# %%

seq = range(0, 10) # (start, stop); qtde = stop - start

for i in range (1, 11):
    print(i)

# %%

qtde = int(input("Quantos fodase você quer? "))

for i in range(qtde):
    print("Fodase")

#%%

for i in range(1,16):
    if i % 2 == 0:
        print(i)