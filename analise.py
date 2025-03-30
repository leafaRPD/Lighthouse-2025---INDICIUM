import pandas as pd

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


