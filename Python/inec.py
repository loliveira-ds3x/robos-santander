from Packages.Main import crawlers_main

start_url = 'http://www6.sistemaindustria.org.br/gpc/externo/listaResultados.faces?codPesquisa=120'
input_file = 'Relatorio_Series.xls'
input_file_tab1 = 'Linhas'
output_file = 'inec.csv'
get_type = 'inec_selenium'

crawlers_main.main(get_type=get_type, start_url=start_url,input_file=input_file,input_file_tab1=input_file_tab1,output_file=output_file)