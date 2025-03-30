import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo CSV
df = pd.read_csv("dados_integrados.csv")

clientes_unicos = df['customer_id'].nunique()
print(f"Número de clientes: {clientes_unicos}")

contagem_compras = df['customer_id'].value_counts()
clientes_uma_compra = (contagem_compras == 1).sum()
print(f"Número de clientes que compraram apenas uma vez: {clientes_uma_compra}")

"""- -- - - - """

# Calcular o total da compra para cada linha
df['total_compra'] = df['unit_price'] * df['quantity'] * (1 - df['discount'])

# Agrupar por 'order_id' e somar os valores de 'total_compra'
df_total_compras = df.groupby('order_id', as_index=False)['total_compra'].sum()

# Calcular a média do total das compras
media_total_compra = df_total_compras['total_compra'].mean()
print(f"Ticket médio das compras: {media_total_compra:.2f}")

# porcentagem de compras abaixo do ticket médio:
# Contar quantos pedidos têm 'total_compra' abaixo da média
compras_abaixo_media = df[df['total_compra'] < media_total_compra].shape[0]
# Total de pedidos
total_pedidos = df.shape[0]
# Calcular a porcentagem
percentual_abaixo_media = (compras_abaixo_media / total_pedidos) * 100
print(f"Porcentagem de compras abaixo da média: {percentual_abaixo_media:.2f}%")

print("O desvio padrão é:", df_total_compras['total_compra'].std().round(2))

"""////////////////////////"""
# Calcular média e desvio padrão
media_total_compra = df_total_compras['total_compra'].mean()
desvio_padrao = df_total_compras['total_compra'].std().round(2)

# Definir limite superior (1 desvio padrão acima da média)
limite_superior = media_total_compra + desvio_padrao

# Definir limite superior (2 desvio padrão acima da média)
limite_superior2 = media_total_compra + 2*desvio_padrao

# Contar quantos pedidos estão acima de 1 vez esse limite
compras_acima_1dp = df_total_compras[df_total_compras['total_compra'] > limite_superior].shape[0]

# Calcular a porcentagem
percentual_acima_1dp = (compras_acima_1dp / df_total_compras.shape[0]) * 100

print(f"Porcentagem de compras acima de 1 desvio padrão: {percentual_acima_1dp:.2f}%")

# Contar quantos pedidos estão acima desse limite
compras_acima_2dp = df_total_compras[df_total_compras['total_compra'] > limite_superior2].shape[0]

# Calcular a porcentagem
percentual_acima_2dp = (compras_acima_2dp / df_total_compras.shape[0]) * 100

print(f"Porcentagem de compras acima de 2 desvio padrão: {percentual_acima_2dp:.2f}%")

print(df_total_compras['total_compra'].describe().round(2))

import seaborn as sns
plt.figure(figsize=(8, 6))
sns.histplot(df_total_compras['total_compra'], bins=15, kde=True, color='blue')
plt.xlabel('Total da compra')
plt.ylabel('Frequência')
plt.title('Distribuição do Total das compras')
plt.show()
