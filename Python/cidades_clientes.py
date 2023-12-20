import pandas as pd
from lista import lista, lista2

# Supondo que lista2 contém os caminhos dos arquivos e lista contém os valores para filtrar
dfs_resultantes = []

for arquivo in lista2:
    # Ler o arquivo CSV
    df = pd.read_csv(arquivo, sep=';', encoding='Latin1',dtype=str)

    # Filtrar o DataFrame para incluir apenas as linhas onde a primeira coluna está na lista
    df_filtrado = df[df[df.columns[0]].isin(lista)]
    print(df_filtrado.head())

    # Adicionar as linhas filtradas à lista de DataFrames resultantes
    dfs_resultantes.append(df_filtrado)

# Concatenar todos os DataFrames resultantes em um único DataFrame
df_resultado = pd.concat(dfs_resultantes, ignore_index=True)

# Imprimir as primeiras linhas do DataFrame resultante
print("DataFrame resultante:")
print(df_resultado.head())

# Salvar o DataFrame resultante em um arquivo Excel para melhor visualização
df_resultado.to_excel('resultado_final.xlsx', index=False)
print("DataFrame resultante salvo em resultado_final.xlsx")
