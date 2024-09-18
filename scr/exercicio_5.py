# Questão 5 - Inversão de string
def inverter_string(s):
    invertida = ""
    for i in range(len(s)-1, -1, -1):
        invertida += s[i]
    return invertida

# String de entrada
entrada = input("Informe uma string para inverter: ")

# Inverter e mostrar a string
print(f"String invertida: {inverter_string(entrada)}")
