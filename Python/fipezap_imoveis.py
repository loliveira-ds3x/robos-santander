from Packages.Main import crawlers_main

#define variaveis
crawler_name = 'fipezap_imoveis'
start_url = 'https://www.fipe.org.br/pt-br/indices/fipezap/#indice-fipezap-historico'
html_path = 'div.tab ul li:nth-of-type(3) a[href]'
get_type = 'simple_url'
etl_type = 'fipezap_pivot'

input_file = crawler_name+'.xls'
output_file = crawler_name+'.csv'

input_file1_tab = 'Índice FipeZap'
index_columns = "B:BD"
##main
crawlers_main.main(get_type=get_type, etl_type=etl_type, start_url=start_url, html_path=html_path, input_file=input_file,input_file_tab1=input_file1_tab,output_file=output_file,crawler_name=crawler_name)