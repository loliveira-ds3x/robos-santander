from Packages.Main import crawlers_main

##define variaveis
crawler_name = 'abecip'
start_url = "https://www.abecip.org.br/credito-imobiliario/financiamento"
html_path = 'div.bloco_anexo a[href]'
get_type = 'simple_url'
etl_type = 'excel_to_csv'
last_rows = 2

input_file = crawler_name + '.xls'
input_file_tab1 = 'BD_Unidades'
index_columns = "A:G"  
column_names = [ 'tempo', 'Unid_construcao','unid_aquisicao','unid_total','valor_construcao','valor_aquisicao','valor_total']
skiped_rows = [1,2,3,4,5]
output_file = crawler_name + '.csv'

##main
crawlers_main.main(get_type=get_type, etl_type=etl_type, start_url=start_url, html_path=html_path, input_file=input_file,input_file_tab1=input_file_tab1,index_columns=index_columns, column_names=column_names,output_file=output_file,crawler_name=crawler_name,skiped_rows=skiped_rows,last_rows=last_rows)