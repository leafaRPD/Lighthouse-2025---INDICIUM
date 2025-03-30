import os
import pandas as pd

# Caminho da pasta onde os arquivos estão armazenados
# alterar o caminho conforme necessidade, caso tenha gravado em outra pasta
caminho_pasta = r"C:\Users\RAFAEL\PycharmProjects\Lighthouse-2025---INDICIUM\Data"

# Lista para armazenar os DataFrames
lista_dfs = []

# Percorre todos os arquivos CSV da pasta
for arquivo in os.listdir(caminho_pasta):
    if arquivo.endswith(".csv"):
        caminho_arquivo = os.path.join(caminho_pasta, arquivo)

        try:
            # Tenta ler com delimitador ponto e vírgula (;)
            df = pd.read_csv(caminho_arquivo, delimiter=";", on_bad_lines="skip")
        except pd.errors.ParserError:
            try:
                # Se falhar, tenta com vírgula (,)
                df = pd.read_csv(caminho_arquivo, delimiter=",", on_bad_lines="skip")
            except Exception as e:
                print(f"Erro ao ler {arquivo}: {e}")
                continue  # Pula esse arquivo e vai para o próximo

        lista_dfs.append(df)  # Adiciona à lista

# Verifica se conseguiu carregar algum arquivo
if lista_dfs:
    # Une todos os DataFrames em um único
    df_final = pd.concat(lista_dfs, ignore_index=True)

    # Salva o resultado consolidado
    df_final.to_csv("dados_integrados.csv", index=False)

    print("Dados integrados com sucesso! Salvo como 'dados_integrados.csv'.")
else:
    print("Nenhum arquivo CSV pôde ser carregado.")
