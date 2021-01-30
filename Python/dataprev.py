from Packages.Main import crawlers_main

##define variaveis
crawler_name = 'dataprev'
start_url = 'https://dadosabertos.dataprev.gov.br/dataset/inss-beneficios-concedidos'
html_path = 'li.resource-item div.dropdown ul.dropdown-menu a.resource-url-analytics'
get_type = 'multiple_urls'
links_download = []

column_names = [ 'competencia_concessao','especie','cid', 'cid2', 'despacho', 'data_nascimento', 'sexo', 'clientela', 'municipio_residencia'
                ,'vinculo_dependentes','forma_filiacao','uf','qt_sm_rmi'
                ]

##main
crawlers_main.main(get_type=get_type, start_url=start_url, html_path=html_path, crawler_name=crawler_name, links_download=links_download)