import scrapy
from time import sleep


class MagazineluizaSpider(scrapy.Spider):
    name = "magazineluiza"
    allowed_domains = ["www.magazineluiza.com.br"]
    start_urls = ["https://www.magazineluiza.com.br/busca/smartphone/?from=submit"]
    cont_pagina = 1
    max_pagina = 5


    def parse(self, response):
        #produtos = response.css('div.ui-search-result__wrapper')
        #produtos = response.css('div.poly-card.poly-card--list')
        print(response)
        produtos = response.css('div.sc-evdWiO.cEdKXb')

        for produto in produtos:
            yield { 
                'nome': produto.css('h2.sc-gQSkpc.iWaBVz::text').get()
                , 'avaliacao': produto.css('span.sc-cezyBN.iJpWGJ::text').get()
                , 'preco_old': produto.css('p.sc-dcJsrY.lmAmKF.sc-bddgXz.kXcaxX::text').get()
                , 'preco_avista': produto.css('p.sc-dcJsrY.eLxcFM.sc-eHsDsR.eGPZvr::text').get()
                , 'preco_parcelado': produto.css('p.sc-dcJsrY.dpUJi.sc-bdOgaJ.gYMJkM::text').get()
            }
        sleep(1)

        #pegar o numero total de páginas
        paginas = response.css('a.sc-dGCmGc.gNNmXi')
        num_total_paginas = int(paginas[4].css('a.sc-dGCmGc.gNNmXi::text').get())

        # limitar o scrraping a uma quantidade de páginas apra não ser bloqueado e só seguir se existir próxima página
        if self.cont_pagina < self.max_pagina:
            #proxima_pagina = response.csv('button.sc-fAGzit.hffImw::attr(href)').get()
            proxima_pagina = f'https://www.magazineluiza.com.br/busca/smartphone/?from=submit&page={self.cont_pagina + 1}'
            if proxima_pagina:
                self.cont_pagina += 1
                sleep(3)
                yield scrapy.Request(url=proxima_pagina, callback=self.parse)
