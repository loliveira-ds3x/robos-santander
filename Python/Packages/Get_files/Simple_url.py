import requests
from bs4 import BeautifulSoup

class Simple_url_method():
    def __init__(self, file_type, start_url,html_path,input_file):
        self.file_type = file_type
        self.start_url = start_url
        self.html_path = html_path
        self.input_file = input_file

    def get_file(self):
        #url da página do download  
        
        r  = requests.get(self.start_url, allow_redirects=True)
        try:
          #logging.info('Iniciando download do arquivo')
          #url da página do download  
          r  = requests.get(self.start_url, allow_redirects=True)
          
          #o link muda todo mês; por isso faço get no link toda vez
          data = r.text
          soup = BeautifulSoup(data)
          element = soup.select_one(self.html_path)
          link_download = element['href']
          #request no link do download
          s = requests.get(link_download, allow_redirects=True)
        except Exception as e:
          print(e)
          #logging.error('Erro ao fazer o download')
        else:  
          #logging.info('Download executado com sucesso')
          #abre o excel
          f = open('/home/ds3x/robos-santander/Outputs/'+self.input_file, 'wb').write(s.content)
          return f
