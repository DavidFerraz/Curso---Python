# %%

minha_lista = []
print(minha_lista)

#%%

minha_lista = ['teo', 'calvo', 31, 1.82]
print(minha_lista)

# %%

# Primeiro elemento:
minha_lista[0]

# %%

# Segundo elemento:
minha_lista[1]

# %%

minha_lista[-1]

# %%

minha_lista[-2:]

# %%

nova_lista = minha_lista[:]
print(nova_lista)

# %%

minha_lista[::-1] # inversão da lista

# %%

minha_lista[::2]

# %%

notas = []
nota = 7.75

notas.append(nota)
print(notas)

notas.append(10)
print(notas)

notas.extend([5.75, 6.24])
print(notas)

notas = notas + [10, 9.25]
print(notas)

notas.remove(10)
print(notas)

# %%
notas[2]

# %%

nomes = ['teo', 'maria', 'nah']

for i in nomes:
    print(i.title())

nomes.extend(['teodoro'])

print(nomes)

# %%

dados =["Teo", "Calvo", 31, ["Nah", "Josefina", "Elaina"], ["Maria"]]
dados[3][2]

# %%

dados[-1][0][0]