# WebScraping_MercadoLivre

## Criar/iniciar o projeto de webscarping - scrapy startproject nome_projeto
scrapy startproject webscraping

## Criar o Spyder - cirar o arquivo para iniciar o webscraping
scrapy genspider mercadolivre https://lista.mercadolivre.com.br/smartphone

# Executar a coleta criando arquivo de saida (jsonl)
scrapy runspider .\coleta\coleta\spiders\mercadolivre.py -O .\data\data.jsonl
scrapy runspider .\coleta\coleta\spiders\magazineluiza.py -O .\data\data_magazineluiza.jsonl

