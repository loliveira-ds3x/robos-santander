from Packages.Main import crawlers_main

##VARIAVEIS ARQUIVO 1
crawler_name = 'icc'
start_url_1 = "https://www.fecomercio.com.br/pesquisas/indice/icc"
html_path_1 = 'div.boxDownload a[href]'
get_type_1 = 'simple_url'
etl_type_1 = 'excel_to_csv'

input_file_1 = crawler_name + '_icc_icea_iec.xls'
input_file_tab1_1 = 'SÉRIE'
index_columns_1 = "A,B,I,P"  
column_names_1 = [ 'data','ICC','ICEA','IEC']
                
output_file_1 = crawler_name + '_icc_icea_iec.csv'

##VARIAVEIS ARQUIVO 2
start_url_2 = "https://www.portaldaindustria.com.br/estatisticas/icei-indice-de-confianca-do-empresario-industrial/"
html_path_2 = 'div.estatiscas-info-adicionais-edicao div:nth-of-type(1) > div:nth-of-type(6) div > a[href]'
get_type_2 = 'simple_url'
etl_type_2 = 'pivot_excel_to_csv'

input_file_2 = crawler_name + '_icei.xls'
input_file_tab1_2 = 'Geral'
column_names_2 = [ 'data','ICEI']
header_2 = 7
skiped_rows_2 = [8]
nrows_2 = 1

output_file_2 = crawler_name + '_icei.csv'

##main
crawlers_main.main(get_type=get_type_1, etl_type=etl_type_1, start_url=start_url_1, html_path=html_path_1, input_file=input_file_1,input_file_tab1=input_file_tab1_1,index_columns=index_columns_1, column_names=column_names_1,output_file=output_file_1,crawler_name=crawler_name)
crawlers_main.main(get_type=get_type_2, etl_type=etl_type_2, start_url=start_url_2, html_path=html_path_2, input_file=input_file_2,input_file_tab1=input_file_tab1_2, column_names=column_names_2,output_file=output_file_2,crawler_name=crawler_name,headers=header_2,skiped_rows=skiped_rows_2,nrows=nrows_2)