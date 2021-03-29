# -*- coding: utf-8 -*-
"""instagram_insights_pages.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-ts41e3IX8BnSFgSmjfLOLU7b_Zb4a9U
"""

import pandas as pd
from datetime import datetime
import requests
import numpy as np

my_app_id = '846087082604504'
my_app_secret = 'be005765b88d863c474a846a8fdd7df3'
my_access_token = 'EAAMBgwAB99gBAMRwUIti029ZAHX0rENDiN3n0ZCEKAES1HgVDOjYpSQkPiVkGZCdoAXYOAwX3j7yWYCZBhoV222KOHrL16CWLhoexgvYK9WzXEK5gqqgIp8X7DlAg2vazx9DOSG7J7eFM5rewMXAcn6NwbqBl5dIqsZAsrNPtpwZDZD'

accounts_infos = requests.get('https://graph.facebook.com/v9.0/me/accounts?fields=name,username,access_token&limit=1000&access_token='+my_access_token).json()['data']
df_accounts_infos = pd.json_normalize(accounts_infos)
df_accounts_infos.rename(columns = {'name':'page_name'},inplace=True)
df_accounts_infos.rename(columns = {'id':'page_id'},inplace=True)
df_accounts_infos = df_accounts_infos.loc[df_accounts_infos['page_id'] != '442659496581990']
df_accounts_infos

df_list = []
for page_id,username in zip(df_accounts_infos['page_id'],df_accounts_infos['username']):
  ig_page_id = requests.get('https://graph.facebook.com/v9.0/'+page_id+'?fields=instagram_business_account&access_token='+my_access_token).json()['instagram_business_account']['id']
  ig_page_insights = requests.get('https://graph.facebook.com/v9.0/'+ig_page_id+'/insights?metric=impressions,reach,follower_count,email_contacts,phone_call_clicks,text_message_clicks,get_directions_clicks,website_clicks,profile_views&period=day&since=2021-03-01&until=2021-03-25&access_token='+my_access_token).json()['data']

  for dimensions in range(len(ig_page_insights)):
    df = pd.json_normalize(ig_page_insights[dimensions]['values'])
    df['dimension'] = ig_page_insights[dimensions]['name']
    df['fb_page_id'] = page_id
    df['ig_page_id'] = ig_page_id
    df_list.append(df)
df_list = pd.concat(df_list)

final_table = pd.pivot_table(df_list,index=['fb_page_id','ig_page_id','end_time'],columns='dimension',values='value', aggfunc=np.max, fill_value=0)
final_table.reset_index(inplace=True)
final_table