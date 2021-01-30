import pandas as pd 

def Xls_to_csv_method(input_file=None, input_file_tab1=None,index_columns=None,column_names=[],output_file=None,skiped_rows=[]):         
  
  try:
    #logging.info('Iniciando tratamentos do arquivo. Convertendo em csv.')
    #lê o excel, renomeia colunas e salva o csv
    df = pd.read_excel('/home/ds3x/robos-santander/Outputs/'+input_file, input_file_tab1, usecols = index_columns, skiprows=skiped_rows)
    df.columns = column_names
    df.to_csv('/home/ds3x/robos-santander/Outputs/'+output_file, index = False, header=True, sep='|')
  except Exception as e:
    print(e)
    #logging.error('Erro ao fazer tratamento do arquivo') 
  else:  
    print('Sucesso excel_to_csv')  
    #logging.info('Csv gerado com sucesso')

def Pivot_excel_to_csv_method(input_file=None,input_file_tab1=None,output_file=None,headers=None,skiped_rows=[],column_names=[],nrows=None):

  try:
    print(input_file)
    df = pd.read_excel('/home/ds3x/robos-santander/Outputs/'+input_file, input_file_tab1,header=headers, skiprows=skiped_rows,nrows=nrows)
    pivot = df.melt(id_vars=["Unnamed: 2"], var_name="Date", value_name="Value").drop([0, 1]).drop(columns=["Unnamed: 2"])
    pivot.columns = column_names
    pivot.to_csv('/home/ds3x/robos-santander/Outputs/'+output_file, index = False, header=True, sep='|')
  except Exception as e:
    print(e)
    #logging.error('Erro ao fazer tratamento do arquivo') 
  else:  
    print('Sucesso pivo_excel_to_csv')  
    #logging.info('Csv gerado com sucesso')  
  