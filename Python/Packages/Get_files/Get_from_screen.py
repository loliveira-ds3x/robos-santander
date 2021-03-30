import requests
import pandas as pd
from bs4 import BeautifulSoup
import re

def Get_id_list(text):
    url = 'http://www.ipeadata.gov.br/ListaSeries.aspx?Text='+text
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data,'html.parser')

    id_list = []
    data = soup.find_all('a')
    for item in data:
        id = item['href']
        id = id.split('(')[1].split(')')[0]
        id_list.append(id)
    return id_list

def Get_from_screen_method(id):
    start_url = 'http://www.ipeadata.gov.br/ExibeSerie.aspx?module=M&serid='+id

    r = requests.get(start_url)
    data = r.text
    soup = BeautifulSoup(data,'html.parser')
    table =  soup.find_all("table",attrs={"class": "dxgvTable"})

    table1 = table[0]
    body = table1.find_all("tr")
    # Head values (Column names) are the first items of the body list
    head = body[0] # 0th item is the header row
    body_rows = body[1:] # All other items becomes the rest of the rows

    headings = []
    for item in head.find_all("td",attrs={"class": "dxgvHeader"}): # loop through all th elements
        # convert the th elements to text and strip "\n"
        item = (item.text).strip("\n")
        # append the clean column name to headings
        headings.append(item)

    all_rows = [] # will be a list for list for all rows
    for row_num in range(len(body_rows)): # A row at a time
        row = [] # this will old entries for one row
        for row_item in body_rows[row_num].find_all("td"): #loop through all row entries
            # row_item.text removes the tags from the entries
            # the following regex is to remove \xa0 and \n and comma from row_item.text
            # xa0 encodes the flag, \n is the newline and comma separates thousands in numbers
            aa = row_item.text
            #append aa to row - note one row entry is being appended
            row.append(aa)
        # append one row to all_rows
        all_rows.append(row)

    df = pd.DataFrame(data=all_rows,columns=headings)
    df_pivot = df.melt(id_vars=headings[0])
    df_pivot['id'] = id
    df_pivot = df_pivot.rename(columns = {'Data':'period'})
    df_pivot = df_pivot.rename(columns = {'variable':'nome'})
    
    return df_pivot