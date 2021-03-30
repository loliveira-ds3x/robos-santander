import sys
from googleads import adwords
import pandas as pd
import numpy as np
import io

# Define output como string
output = io.StringIO()

#cria uma lista de customer ids da conta para que sejam usados na função get_report
def get_customers_list():
    #inicia o client com configs definidas no arquivo home/google-ads.yaml e define o serviço de gerencia de customers
    adwords_client = adwords.AdWordsClient.LoadFromStorage()
    managed_customer_service = adwords_client.GetService(
        'ManagedCustomerService', version='v201809')

    selector = {
        'fields': ['CustomerId', 'Name'] 
        }
    get_selector = managed_customer_service.get(selector)
    #seleciona somente a lista de customers da conta
    customers = []
    for account in get_selector['entries']:
        customers.append(str(account['customerId']))    
    return customers

#faz o get do report para um customer id dado; os parametros da query estao definidos no script do robo
def get_report(customer_id, name, date_range_type, report_type, download_format, query_fields, query_date_range): 
  #inicia o client com configs definidas no arquivo home/google-ads.yaml e define o serviço de gerencia de download de reports
  adwords_client = adwords.AdWordsClient.LoadFromStorage()
  adwords_client.SetClientCustomerId(customer_id)
  report_downloader = adwords_client.GetReportDownloader(version='v201809')

  #define os parâmetros da query
  report = {
      'reportName': name,
      'dateRangeType': date_range_type,
      'reportType': report_type,
      'downloadFormat': download_format,
      'selector': {
          'fields': query_fields,
          'dateRange': query_date_range
      }
  }

  #direciona saída para 'output'; tira todos os headers e linhas com impressões nulas
  report_downloader.DownloadReport(
    report, output, skip_report_header=True, skip_column_header=True, skip_report_summary=True,include_zero_impressions=False)
  output.seek(0)
  #salva output em um dataframe pra ser usado na main
  df = pd.read_csv(output)
  print(df)
  return df

#renomeia o dataframa final e salva no diretório especificado
def Convert_df_to_csv(table,crawler_name,column_names):
    #table.columns = column_names
    table.to_csv('/home/ds3x/robos-santander/Outputs/'+crawler_name+'.csv', index = False, header=True, sep='|')