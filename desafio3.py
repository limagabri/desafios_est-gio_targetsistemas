import json
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

with open('dados_desafio3.json', 'r') as file:
    dados = json.load(file)

valores_faturamento = [item['valor'] for item in dados if item['valor'] > 0]
menor_faturamento = min(valores_faturamento)
maior_faturamento = max(valores_faturamento)
media_faturamento = sum(valores_faturamento) / len(valores_faturamento)

dias_acima_media = len([valor for valor in valores_faturamento if valor > media_faturamento])

print("Menor faturamento: R$", locale.currency(menor_faturamento, grouping=True))
print("Maior faturamento: R$", locale.currency(maior_faturamento, grouping=True))
print("Número de dias acima da média:", dias_acima_media)
