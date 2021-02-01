import logging
import os

from pyvirtualdisplay import Display
from selenium import webdriver

import requests

logging.getLogger().setLevel(logging.INFO)

BASE_URL = 'http://pdet.mte.gov.br/'

def firefox_example():
    display = Display(visible=0, size=(800, 600))
    display.start()
    logging.info('Initialized virtual display..')

    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference('browser.download.folderList', 2)
    firefox_profile.set_preference('browser.download.manager.showWhenStarting', False)
    firefox_profile.set_preference('browser.download.dir',os.getcwd())
    firefox_profile.set_preference('browser.helperApps.neverAsk.saveToDisk', '/home/ds3x/robos-santander/Temp/')

    logging.info('Prepared firefox profile..')

    driver = webdriver.Firefox(firefox_profile=firefox_profile)
    logging.info('Initialized firefox browser..')


    driver.get(BASE_URL)
    logging.info('Accessed %s ..', BASE_URL)
    path_novo_caged = driver.find_element_by_css_selector('li.item-5866 a')
    link_novo_caged = path_novo_caged.get_attribute('href')
    
    driver.get(link_novo_caged)
    logging.info('Accessed %s ..', link_novo_caged)
    
    path_download_file = driver.find_element_by_css_selector('li.item-5951 a')
    link_download_file = path_download_file.get_attribute('href')

    driver.quit()
    display.stop()

    s = requests.get(link_download_file, allow_redirects=True)
    open('/home/ds3x/robos-santander/Temp/caged.xlsx', 'wb').write(s.content)

if __name__ == '__main__':
    firefox_example()
