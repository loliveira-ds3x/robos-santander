from Packages.Main import crawlers_main 

##define variaveis
crawler_name = 'caged'
start_url = "http://pdet.mte.gov.br/"
get_type = 'selenium_simple_url'
etl_type = 'pivot_generic'

input_file = crawler_name + '.xls'
input_file_tab1 = 'Tabela 5'
column_names = ['period','Admissoes','Demissoes']
headers = [4]

output_file = crawler_name + '_hist.csv'

##main
crawlers_main.main(get_type=get_type, etl_type=etl_type, start_url=start_url, input_file=input_file,input_file_tab1=input_file_tab1, headers=headers,column_names=column_names,output_file=output_file,crawler_name=crawler_name)