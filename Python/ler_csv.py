import pandas as pd

df = pd.read_csv(r'arquivos\Estabelecimentos0\K3241.K03200Y0.D31209.ESTABELE', sep=';', encoding='Latin1',dtype=str)

print(df.head())