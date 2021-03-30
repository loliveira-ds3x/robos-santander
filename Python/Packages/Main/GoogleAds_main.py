from Packages.APIs import googleads
from datetime import datetime
import pandas as pd

now = datetime.now()

def main(crawler_name,column_names,name, date_range_type, report_type, download_format, query_fields, query_date_range):
    try:
        #Cria lista de customerIds
        customer_list = googleads.get_customers_list()
        print('######Lista de customerIds######')
        print(customer_list)
    except Exception as e:
        print('erro get customers ids')
        print(e)
    try:
        report_final_table = []
        #Baixa report pra todos customerIds da lista
        for customerid in customer_list:
            print('Baixando report de: ',customerid)
            for n, r, q in zip(name, report_type,query_fields):
                try:
                    partial_report = googleads.get_report(customerid,n,date_range_type,r,download_format,q,query_date_range)
                    report_final_table.append(partial_report)
                except Exception as e:
                    None
        report_final_table = pd.concat(report_final_table)
        #salva dataframe em csv
        googleads.Convert_df_to_csv(report_final_table,crawler_name,column_names)
    except Exception as e:
        print(e)
    else:
        #logging.error('Erro nas classes')
        print('Sucesso')