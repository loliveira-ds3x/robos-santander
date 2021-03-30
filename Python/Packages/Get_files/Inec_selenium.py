import os
import time
from pyvirtualdisplay import Display
from selenium import webdriver
import pandas as pd
import requests


def firefox_example(start_url):
    display = Display(visible=0, size=(1200, 700))
    display.start()
    
    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference('browser.download.folderList', 2)
    firefox_profile.set_preference('browser.download.manager.showWhenStarting', False)
    firefox_profile.set_preference('browser.download.dir','/home/ds3x/robos-santander/Outputs/')
    firefox_profile.set_preference("browser.helperApps.neverAsk.saveToDisk",
                                   "text/plain,text/x-csv,text/csv,application/vnd.ms-excel,application/csv,application/x-csv,text/csv,text/comma-separated-values,text/x-comma-separated-values,text/tab-separated-values,application/pdf")
    driver = webdriver.Firefox(firefox_profile=firefox_profile)

    driver.get(start_url)
    time.sleep(5)
    #seleciona todos os segmentos
    driver.find_element_by_id('listaResultadoForm:dtResult:selecionarValores').click()
    time.sleep(3)
    #download de todos os arquivos
    driver.find_element_by_id('listaResultadoForm:btnExportarExcel1').click()
    time.sleep(3)

    driver.quit()
    display.stop()

def Pivot_excel_to_csv_method(input_file,input_file_tab1,output_file):
    column_names = []
    df = pd.read_excel('/home/ds3x/robos-santander/Outputs/'+input_file, input_file_tab1)
    df.dropna(subset = ["Indice nacional de expectativa do consumidor - INEC\nÍndice de expectativa de compras de bens de maior valor\naté 4ª série do fund.\n Difusão"], inplace=True)
    columns = df.columns.tolist()
    for column in columns:
        if column == 'Mes/Ano':
            column_names.append(column)
        else:
            column_names.append(column.split('\n')[2])
    df.columns = column_names
    df = df.melt(id_vars=["Mes/Ano"], var_name="Date", value_name="Value")
    df.columns = ['data','medida','valor']
    df['recordid'] = df.index
    df.to_csv('/home/ds3x/robos-santander/Outputs/'+output_file, index = False, header=True, sep='|')
