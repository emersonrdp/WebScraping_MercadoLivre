import pandas as pd
import sqlite3
from datetime import datetime

# Ler o arquivo jsonl
#df = pd.read_json('D:\workspace\WebScraping_mercadoLivre\data\data_magazineluiza_OK.json')
#df = pd.read_json('data\data_magazineluiza_OK.json')
df = pd.read_csv('data\data_magazineluiza_teste.csv', sep=',')

#df = pd.read_csv('D:\workspace\WebScraping_mercadoLivre\data\data_magazineluiza_teste.csv', sep=',')

# Adicionando colunas com o site de onde os dados forma coletados
df['_origem_dados'] = 'https://www.magazineluiza.com.br/busca/smartphone/?from=submit'

# Adicionando colunas com a data da coleta
df['_data_coleta'] = datetime.now()

# Remover o prefixo "R$ " e converter para float
df['preco_old'] = df['preco_old'].str.replace('R\$', '', regex=True).fillna(0).astype(float)
df['preco_avista'] = df['preco_avista'].str.replace('R\$', '', regex=True).fillna(0).astype(float)
df['preco_parcelado'] = df['preco_parcelado'].str.replace('R\$', '', regex=True).fillna(0).astype(float)

# Separando a avaliação e a quantidade de avaliações
df['qtd_avaliacoes'] = df['avaliacao'].str.extract(r'\((\d+)\)').astype(int)
df['avaliacao'] = df['avaliacao'].str[:3].astype(float)

# Reordenar as colunas
df = df[['nome','avaliacao', 'qtd_avaliacoes', 'preco_old', 'preco_avista', 'preco_parcelado', '_origem_dados', '_data_coleta']]

#print(df.head())
#df.info()


# Conectando no SQLite  (ou criar um novo)
conn = sqlite3.connect('data\cotacoes.db')

# Salvar o Dataframe no Banco de Dados
df.to_sql('magazineluiza_itens', conn, if_exists='replace', index=False)

#Fechando a conexão com o Banco de Dados
conn.close()


# Executar esse código
# python .\src\transformacao\main.py