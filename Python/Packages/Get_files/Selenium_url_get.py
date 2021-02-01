import os
from pyvirtualdisplay import Display
from selenium import webdriver
import requests


class Selenium_simple_url_method():
    def __init__(self, get_type=None, start_url=None,input_file=None):
        self.get_type = get_type
        self.start_url = start_url
        self.input_file = input_file

    def Selenium_get_url(self):
        try:
            display = Display(visible=0, size=(800, 600))
            display.start()

            firefox_profile = webdriver.FirefoxProfile()
            firefox_profile.set_preference('browser.download.folderList', 2)
            firefox_profile.set_preference('browser.download.manager.showWhenStarting', False)
            firefox_profile.set_preference('browser.download.dir',os.getcwd())
            firefox_profile.set_preference('browser.helperApps.neverAsk.saveToDisk', '/home/ds3x/robos-santander/Temp/')

            driver = webdriver.Firefox(firefox_profile=firefox_profile)

            driver.get(self.start_url)
            path_novo_caged = driver.find_element_by_css_selector('li.item-5866 a')
            link_novo_caged = path_novo_caged.get_attribute('href')
            
            driver.get(link_novo_caged)
            
            path_download_file = driver.find_element_by_css_selector('li.item-5951 a')
            link_download_file = path_download_file.get_attribute('href')

            driver.quit()
            display.stop()
        except Exception as e:
            print(e)
            #logging.error('Erro ao fazer o download')
        else:  
            return link_download_file

    def Selenium_get_file(self,link_download_file):
        s = requests.get(link_download_file, allow_redirects=True)
        open('/home/ds3x/robos-santander/Outputs/'+self.input_file, 'wb').write(s.content)
