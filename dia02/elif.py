idade = int(input("Entre com sua idade: "))

if idade < 18:
    print("Você é menor de idade!")
    print("Vá para casa beber leite!")

elif idade > 90:
    print("Cuidado, você já tem certa de idade!")

else:
    print("Você é maior de idade")
    print("Beba a vontade!")

# %%

if 18 <= idade <= 89:
    print("Você é maior de idade")
    print("Beba a vontade!")

elif idade >= 90:
    print("Cuidado, você já tem certa de idade!")

else:
    print("Você é menor de idade!")
    print("Vá para casa beber leite!")