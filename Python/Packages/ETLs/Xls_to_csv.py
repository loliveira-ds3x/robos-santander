import pandas as pd 

def Xls_to_csv_method(input_file, input_file_tab1,index_columns,column_names,output_file):         
  
  try:
    #logging.info('Iniciando tratamentos do arquivo. Convertendo em csv.')
    #lê o excel, renomeia colunas e salva o csv
    df = pd.read_excel('/home/ds3x/robos-santander/Outputs/'+input_file, input_file_tab1, usecols = index_columns)
    df.columns = column_names
    df.to_csv('/home/ds3x/robos-santander/Outputs/'+output_file, index = False, header=True, sep='|')
  except Exception as e:
    print(e)
    #logging.error('Erro ao fazer tratamento do arquivo') 
  else:  
    print('Sucesso')  
    #logging.info('Csv gerado com sucesso')
