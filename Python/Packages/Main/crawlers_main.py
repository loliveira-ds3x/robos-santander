from Packages.Get_files import Simple_url
from Packages.ETLs import Xls_to_csv

def main(file_type, start_url, html_path, input_file,input_file_tab1,index_columns, column_names,output_file):
  if file_type == 'simple_url':
    file = Simple_url.Simple_url_method(file_type, start_url,html_path,input_file)
    file.get_file()
  else:
    #logging.error('Erro nas classes')
    print('Erro')
  Xls_to_csv.Xls_to_csv_method(input_file, input_file_tab1,index_columns,column_names,output_file)