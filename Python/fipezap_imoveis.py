from Packages.Main import crawlers_main

#define variaveis
crawler_name = 'fipezap_imoveis'
start_url = "https://www.fecomercio.com.br/pesquisas/indice/peic"
html_path = 'div.boxDownload a[href]'
get_type = 'simple_url'
etl_type = 'fipezap_pivot'

input_file = crawler_name + '.xls'
input_file_tab1 = 'Índice FipeZap'

output_file = crawler_name + '.csv'

##main
crawlers_main.main(get_type=get_type, etl_type=etl_type, start_url=start_url, html_path=html_path, input_file=input_file,input_file_tab1=input_file_tab1,output_file=output_file,crawler_name=crawler_name)