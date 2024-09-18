import json

# Altere o caminho para o local correto onde está salvo o arquivo JSON no seu computador
with open('D:/Users/User/Desktop/exercicio_estagio/scr/dados.json') as f:
    dados_faturamento = json.load(f)

# Extraindo os valores de faturamento
faturamento_filtrado = [dia["valor"] for dia in dados_faturamento if dia["valor"] > 0]

# Cálculo do menor, maior faturamento e média
menor_faturamento = min(faturamento_filtrado)
maior_faturamento = max(faturamento_filtrado)
media_mensal = sum(faturamento_filtrado) / len(faturamento_filtrado)

# Número de dias com faturamento superior à média
dias_acima_da_media = len([f for f in faturamento_filtrado if f > media_mensal])

print(f"Menor faturamento: R${menor_faturamento:.2f}")
print(f"Maior faturamento: R${maior_faturamento:.2f}")
print(f"Número de dias com faturamento superior à média: {dias_acima_da_media}")
