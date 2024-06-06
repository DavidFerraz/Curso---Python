# Faça um programa que receba um número em segundos,converta esse número para horas, minuto e segundos.

numero = int(input("Informe o numero em segundos: "))
hora = 0
minuto = 0
segundo = 0
if numero >= 3600:
    hora = numero // 3600
    minuto_resto = numero % 3600
    if minuto_resto >= 60:
        minuto = minuto_resto // 60
        segundo = minuto_resto % 60
    else:
        segundo = minuto_resto % 3600
elif 60 <= numero <= 3599:
    minuto = numero // 60
    segundo = numero % 60
else:
    segundo = numero

print(hora, ":", minuto, ":", segundo)

# FORMA OTIMIZADA DE SE FAZER
# Faça um programa que receba um número em segundos,
# converta esse número para horas, minuto e segundos.
# Exemplos:

# Entrada: 556
# Saída: 0:9:16

# Entrada: 140153
# Saída: 38:55:53

segundos = int(input("Entre com um número em segundos: "))

horas = segundos // (60*60) # horas inteiras

segundos = segundos % (60*60) # resto de segundos da divisao por hora

minutos = segundos // 60 # minutos inteiros

segundos = segundos % 60 # resto de segundos da divisão por minuto

print(horas, minutos, segundos, sep=":")