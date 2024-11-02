# WebScraping_MercadoLivre

Criar/iniciar o projeto de webscarping - scrapy startproject nome_projeto
'''bash
scrapy startproject webscraping
'''
Criar o Spyder - cirar o arquivo para iniciar o webscraping
'''bash
scrapy genspider mercadolivre https://lista.mercadolivre.com.br/smartphone
'''

Executar a coleta criando arquivo de saida (jsonl)
'''bash
scrapy runspider .\src\coleta\spiders\mercadolivre.py -O .\data\data.jsonl
scrapy runspider .\src\coleta\spiders\magazineluiza.py -O .\data\data_magazineluiza.jsonl
'''

Executar o tratamento no Pandas e salvar na banco de dados SQLite
'''bash
python .\src\transformacao\main.py
'''
