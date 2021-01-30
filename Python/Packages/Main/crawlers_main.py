from Packages.Get_files import Get_from_url
from Packages.ETLs import Xls_to_csv

def main(get_type=None, etl_type=None, start_url=None, html_path=None, input_file=None,input_file_tab1=None,index_columns=None, column_names=[],output_file=None,crawler_name=None, links_download=[],skiped_rows=None,headers=None,nrows=None):
  try:
    if get_type == 'simple_url':
      file = Get_from_url.Simple_url_method(get_type, start_url,html_path,input_file)
      file.get_file()
    elif get_type == 'multiple_urls':
      file = Get_from_url.Multiple_url_method(get_type, start_url,html_path,crawler_name, links_download)
      links_download = file.get_urls()
      print(links_download)
      file.get_files(links_download)
  except Exception as e:
    print(e)
  else:
    #logging.error('Erro nas classes')
    print('Sucesso get')
  
  try:
    if etl_type == 'excel_to_csv':
      Xls_to_csv.Xls_to_csv_method(input_file, input_file_tab1,index_columns,column_names,output_file,skiped_rows)
    
    elif etl_type == 'pivot_excel_to_csv':
      Xls_to_csv.Pivot_excel_to_csv_method(input_file,input_file_tab1,output_file,headers,skiped_rows,column_names,nrows)

  except Exception as e:
    print(e)
  else:
    #logging.error('Erro nas classes')
    print('Sucesso etl')