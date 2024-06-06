# %%

dados = ["téo", "calvo", 31]

nome = dados[0]

# %%

dados = {"nome":"Téo",
         "sobrenome":"calvo",
         "idade":31,
         "ex":["Nah", "Josefina", "Elaine"],
         "filhos":[{"nome":"Maria", "idade":2}, {"nome":"Raul", "idade":1}]
         }

nome = dados["nome"]
print(nome)

print(dados["filhos"][0]["idade"])

dados

# %%
dados.keys() # Retorna as chaves do dicionario

# %%
dados.values() # Retorna os valores do dicionario

# %%
dados.items() # Retorna em pares as chaves e os valores do dicionario