import requests
from bs4 import BeautifulSoup

class Simple_url_method():
    def __init__(self, get_type=None, start_url=None,html_path=None,input_file=None):
        self.get_type = get_type
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
          print(link_download)
          #request no link do download
          s = requests.get(link_download, allow_redirects=True)
        except Exception as e:
          print(e)
          #logging.error('Erro ao fazer o download')
        else:  
          #logging.info('Download executado com sucesso')
          #abre o excel
          f = open('/home/ds3x/robos-santander/Outputs/'+self.input_file, mode='wb',encoding='utf-8').write(s.content)
          return f

class Multiple_url_method():

    def __init__(self, get_type=None, start_url=None,html_path=None,crawler_name=None, links_download=[]):
        self.get_type = get_type
        self.start_url = start_url
        self.html_path = html_path
        self.crawler_name = crawler_name
        self.links_download = links_download
    def get_urls(self):
        try:
            links_download = []
            r  = requests.get(self.start_url, allow_redirects=True,verify = False)
            data = r.text
            soup = BeautifulSoup(data)
            element = soup.select(self.html_path)

            for item in element:
                links_download.append(item['href'])

        except Exception as e:
            print(e)
        else:
            return links_download

    def get_files(self,links_download):
        try:
            for link in links_download:
                input_file = '/home/ds3x/robos-santander/Outputs/'+self.crawler_name+link[-12:]
                s = requests.get(link, allow_redirects=True,verify = False)
                g = open(input_file, 'wb')
                g.write(s.content)
                g.close()
        except Exception as e:
            print(e)
        else:
            print('Sucesso')