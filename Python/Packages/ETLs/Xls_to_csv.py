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

def Fipezap_pivot_method(input_file=None, input_file1_tab=None, output_file=None,header=[0,1,2,3]):
    try:
      df = pd.read_excel('/home/ds3x/robos-santander/Outputs/'+input_file, sheet_name=input_file1_tab,header=[0,1,2,3])
      print(df)
      df.columns = ['_'.join(col)for col in df.columns]
      df = df.rename(columns = {'Índice FipeZap_Unnamed: 1_level_1_Unnamed: 1_level_2_Data':'Data'})
      df = df.drop('Unnamed: 0_level_0_Unnamed: 0_level_1_Unnamed: 0_level_2_Unnamed: 0_level_3', 1)
      df1 = pd.melt(df, id_vars =['Data'])
      df1[['tipo', 'categoria','calculo','colunas']] = df1['variable'].str.split('_', n=3, expand=True)
      df1 = df1.drop('variable', 1)
      df1.to_csv('/home/ds3x/robos-santander/Outputs/'+output_file, index = False, header=True, sep='|')
    except Exception as e:
      print(e)
    else:  
      print('Sucesso Fipezap_pivot') 

def Pivot_excel_to_csv_method_generic(input_file=None,input_file_tab1=None,output_file=None,headers=[],column_names=[]):
  try:
    df = pd.read_excel('/home/ds3x/robos-santander/Outputs/'+input_file, input_file_tab1,header=headers)
    df = df.drop('Unnamed: 0', 1)
    df1 = df[["Mês", "Admissões", "Desligamentos"]]
    df1.columns = column_names
    df1 = pd.melt(df1, id_vars =['period'], var_name="nome", value_name="value")
    df1.to_csv('/home/ds3x/robos-santander/Outputs/'+output_file, index = False, header=True, sep='|')
  except Exception as e:
    print(e)
    #logging.error('Erro ao fazer tratamento do arquivo') 
  else:  
    print('Sucesso pivo_excel_to_csv')  
    #logging.info('Csv gerado com sucesso')