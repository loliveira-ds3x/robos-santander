from Packages.Main import crawlers_main

##define variaveis
crawler_name = 'fecomercio_icf'
start_url = "https://www.fecomercio.com.br/pesquisas/indice/icf"
html_path = 'div.boxDownload a[href]'
file_type = 'simple_url'

input_file = crawler_name + '.xls'
input_file_tab1 = 'Série Histórica'
index_columns = "A:Y"  
column_names = [ 'data', 'icf', 'icf_ate_10_sm', 'icf_mais_de_10_sm', 'emprego_atual', 'emprego_atual_ate_10_sm'
                ,'emprego_atual_mais_de_10_sm', 'perspectiva_profissional', 'perspectiva_profissional_ate_10_sm'
                ,'perspectiva_profissional_mais_de_10_sm', 'renda_atual', 'renda_atual_ate_10_sm'
                ,'renda_atual_mais_de_10_sm', 'acesso_a_credito', 'acesso_a_credito_ate_10_sm', 'acesso_a_credito_mais_de_10_sm'
                ,'nivel_de_consumo_atual', 'nivel_de_consumo_atual_ate_10_sm', 'nivel_de_consumo_atual_mais_de_10_sm'
                ,'perspectiva_de_consumo', 'perspectiva_de_consumo_ate_10_sm', 'perspectiva_de_consumo_mais_de_10_sm'
                ,'momento_para_duraveis', 'momento_para_duraveis_ate_10_sm', 'momento_para_duraveis_mais_de_10_sm'
                ]

output_file = crawler_name + '_hist.csv'

##main
crawlers_main.main(file_type, start_url, html_path, input_file,input_file_tab1,index_columns, column_names,output_file)