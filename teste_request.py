import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0'}

#r = requests.get('https://lista.mercadolivre.com.br/smartphone', headers=headers)
r = requests.get('https://lista.mercadolivre.com.br/smartphone')

#r = requests.get('https://www.amazon.com.br/s?k=smartphone', headers=headers)
#r = requests.get('https://www.amazon.com.br/s?k=smartphone')

print(r.status_code)