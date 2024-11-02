import json

# Lê o arquivo JSONL gerado pelo Scrapy
with open('D:\workspace\WebScraping_mercadoLivre\data\data_magazineluiza.json', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Reescreve o arquivo com ensure_ascii=False para não escapar caracteres
with open('D:\workspace\WebScraping_mercadoLivre\data\data_magazineluiza.json', 'w', encoding='utf-8') as file:
    for line in lines:
        item = json.loads(line)
        file.write(json.dumps(item, ensure_ascii=False) + '\n')
