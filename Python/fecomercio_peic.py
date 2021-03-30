from Packages.Main import crawlers_main

#define variaveis
crawler_name = 'fecomercio_peic'
start_url = "https://www.fecomercio.com.br/pesquisas/indice/peic"
html_path = 'div.boxDownload a[href]'
get_type = 'simple_url'
etl_type = 'excel_to_csv'

input_file = crawler_name + '.xls'
input_file_tab1 = 'Série Histórica'
index_columns = "A,B,C,D,F,G,H,J,K,L,M"  
column_names = [ 'data','familias_endividadas_perc','familias_contas_em_atraso_perc','familias_sem_condicao_de_pagar_perc','familias_endividadas_abs','familias_contas_em_atraso_abs'
              ,'familias_sem_condicao_de_pagar_abs','prazo_comprometimento_renda_3_meses','prazo_comprometimento_renda_3_a_6_meses','prazo_comprometimento_renda_6_a_12_meses'
              ,'prazo_comprometimento_renda_mais_de_12_meses'
                ]

output_file = crawler_name + '_hist.csv'

##main
crawlers_main.main(get_type=get_type, etl_type=etl_type, start_url=start_url, html_path=html_path, input_file=input_file,input_file_tab1=input_file_tab1,index_columns=index_columns, column_names=column_names,output_file=output_file,crawler_name=crawler_name)