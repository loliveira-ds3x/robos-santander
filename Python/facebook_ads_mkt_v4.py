# -*- coding: utf-8 -*-
"""facebook_ads_mkt_v4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qfj_j-KdaGQ66nhEbY-m5jWrZCemtNt1

# **CONFIG**
"""

import pandas as pd
from datetime import date, timedelta
import requests
import numpy as np

my_app_id = '846087082604504'
my_app_secret = 'be005765b88d863c474a846a8fdd7df3'
my_access_token = 'EAAMBgwAB99gBAMRwUIti029ZAHX0rENDiN3n0ZCEKAES1HgVDOjYpSQkPiVkGZCdoAXYOAwX3j7yWYCZBhoV222KOHrL16CWLhoexgvYK9WzXEK5gqqgIp8X7DlAg2vazx9DOSG7J7eFM5rewMXAcn6NwbqBl5dIqsZAsrNPtpwZDZD'

"""# **GET DATA**"""

from datetime import date, timedelta

sdate = date(2020,10,5)   # start date
edate = date(2020,10,6)   # end date
dates_list = pd.date_range(sdate,edate-timedelta(days=1),freq='d')
dates_list

temp_account_list = ['195736164976038','452386382134979','695135207652208','2370632866512809','379443972745362','357355392303701','441354526553203'
                     ,'388111208831608','2220627108041218','512439552806897','376887976332285','275803296896081','1031444827371021','198457314677899'
                     ,'544315486437050','369587127294052','509895376461665','463042151250981','375363469724828'
                     ]

account_id_list = pd.DataFrame(temp_account_list)
account_id_list.columns = ['account_id']
account_id_list['account_id'] = account_id_list['account_id'].astype(str)

insights_level1_infos = []
df_adcreatives = []
df_adreach = []
df_addates = []
df_campaignreach = []
df_campaignreach_daily = []
df_campaigndates = []

for date in dates_list:
  date = str(date)[0:10]
  for account_id in account_id_list['account_id']:
    try:  
      account_insights = requests.get('https://graph.facebook.com/v9.0/act_'+account_id+'/insights?fields=account_currency,account_id,account_name,action_values,actions,ad_id,ad_name,adset_id,adset_name,buying_type,campaign_id,campaign_name,clicks,conversion_values,conversions,impressions,objective,outbound_clicks,spend,store_visit_actions,video_30_sec_watched_actions,video_p100_watched_actions,video_p50_watched_actions,video_p75_watched_actions,video_p95_watched_actions,video_play_actions,video_thruplay_watched_actions&level=ad&limit=1000&breakdowns=publisher_platform&action_attribution_windows=default&time_range={"since":"'+date+'","until":"'+date+'"}&access_token='+my_access_token).json()['data']
      df = pd.DataFrame(account_insights)
      insights_level1_infos.append(df)
    except:
      pass
    try:
      for ad_id in df['ad_id']:
        try:
          adcreatives_row = requests.get('https://graph.facebook.com/v9.0/'+ad_id+'/adcreatives?fields=status,effective_object_story_id,body,object_type&access_token='+my_access_token).json()['data']
          df_adcreatives_row = pd.json_normalize(adcreatives_row)
          df_adcreatives_row['ad_id'] = ad_id
          df_adcreatives.append(df_adcreatives_row)
        except:
          pass

        try:  
          adreach_row = requests.get('https://graph.facebook.com/v9.0/'+ad_id+'/insights?fields=ad_id,reach,frequency&level=ad&date_preset=lifetime&access_token='+my_access_token).json()['data']
          df_adreach_row = pd.json_normalize(adreach_row)
          df_adreach.append(df_adreach_row)
          
          ad_dates_row = requests.get('https://graph.facebook.com/v9.0/'+ad_id+'?fields=created_time,effective_status&access_token='+my_access_token).json()
          df_addates_row = pd.json_normalize(ad_dates_row)
          df_addates.append(df_addates_row)
        except:
          pass
    except:
      pass

    try:
      for campaign_id in df['campaign_id']:
        try:
          campaignreach_row = requests.get('https://graph.facebook.com/v9.0/'+campaign_id+'/insights?fields=campaign_id,reach,frequency&level=campaign&date_preset=lifetime&access_token='+my_access_token).json()['data']
          df_campaignreach_row = pd.json_normalize(campaignreach_row)
          df_campaignreach.append(df_campaignreach_row)

          campaignreach_daily_row = requests.get('https://graph.facebook.com/v9.0/'+campaign_id+'/insights?fields=campaign_id,reach,frequency&level=campaign&time_range={"since":"'+date+'","until":"'+date+'"}&access_token='+my_access_token).json()['data']
          df_campaignreach_daily_row = pd.json_normalize(campaignreach_daily_row)
          df_campaignreach_daily.append(df_campaignreach_daily_row)

          campaign_dates_row = requests.get('https://graph.facebook.com/v9.0/'+campaign_id+'?fields=start_time,stop_time,effective_status&access_token='+my_access_token).json()
          df_campaigndates_row = pd.json_normalize(campaign_dates_row)
          df_campaigndates.append(df_campaigndates_row)
        except:
          pass
    except:
      pass


insights_level1_infos = pd.concat(insights_level1_infos)

"""# **TRATA JSONs, TRANFORMA EM DATAFRAMA, TRATA DATAFRAME**"""

insights_level1_columns = ['account_currency','account_id','account_name','ad_id','ad_name','adset_id','adset_name','buying_type'
                          ,'campaign_id','campaign_name','clicks','impressions','objective','spend','date_start','publisher_platform']
insights_level1_infos_etl = insights_level1_infos[insights_level1_columns]
insights_level1_infos_etl = insights_level1_infos_etl.drop_duplicates()

"""## **Ad infos**"""

df_adcreatives_etl = pd.concat(df_adcreatives)
df_adcreatives_etl = df_adcreatives_etl.rename(columns = {'id':'adcreative_id'})
df_adcreatives_etl = df_adcreatives_etl.rename(columns = {'status':'adcreative_status'})
df_adcreatives_etl = df_adcreatives_etl.rename(columns = {'body':'post_message'})
df_adcreatives_etl = df_adcreatives_etl.rename(columns = {'object_type':'post_type'})       
df_adcreatives_etl[['page_id', 'post_id']] = df_adcreatives_etl['effective_object_story_id'].str.split('_', 1, expand=True)
df_adcreatives_etl['post_url'] = 'https://www.facebook.com/permalink.php?story_fbid'+df_adcreatives_etl['page_id']+'&id='+df_adcreatives_etl['post_id']
df_adcreatives_etl = df_adcreatives_etl.drop('effective_object_story_id',1)

df_adreach_etl = pd.concat(df_adreach)
df_adreach_etl = df_adreach_etl.drop_duplicates()
df_adreach_etl = df_adreach_etl.rename(columns = {'reach':'reach_ad'})
df_adreach_etl = df_adreach_etl.rename(columns = {'frequency':'frequency_ad'})
df_adreach_etl = df_adreach_etl.drop('date_stop',1)
df_adreach_etl = df_adreach_etl.drop('date_start',1)

df_addates_etl = pd.concat(df_addates)
df_addates_etl = df_addates_etl.drop_duplicates()
df_addates_etl = df_addates_etl.rename(columns = {'created_time':'ad_created_time'})
df_addates_etl = df_addates_etl.rename(columns = {'id':'ad_id'})
df_addates_etl = df_addates_etl.rename(columns = {'effective_status':'ad_effective_status'})

"""## **Campaign infos**"""

df_campaignreach_etl = pd.concat(df_campaignreach)
df_campaignreach_etl = df_campaignreach_etl.drop_duplicates()
df_campaignreach_etl = df_campaignreach_etl.rename(columns = {'reach':'reach_campaign'})
df_campaignreach_etl = df_campaignreach_etl.rename(columns = {'frequency':'frequency_campaign'})
df_campaignreach_etl = df_campaignreach_etl.drop('date_stop',1)
df_campaignreach_etl = df_campaignreach_etl.drop('date_start',1)

df_campaignreach_daily_etl = pd.concat(df_campaignreach_daily)
df_campaignreach_daily_etl = df_campaignreach_daily_etl.drop_duplicates()
df_campaignreach_daily_etl = df_campaignreach_daily_etl.rename(columns = {'reach':'reach_campaign_daily'})
df_campaignreach_daily_etl = df_campaignreach_daily_etl.rename(columns = {'frequency':'frequency_campaign_daily'})
df_campaignreach_daily_etl = df_campaignreach_daily_etl.drop('date_stop',1)

df_campaigndates_etl = pd.concat(df_campaigndates)
df_campaigndates_etl = df_campaigndates_etl.drop_duplicates()
df_campaigndates_etl = df_campaigndates_etl.rename(columns = {'start_time':'created_time'})
df_campaigndates_etl = df_campaigndates_etl.rename(columns = {'id':'campaign_id'})
df_campaigndates_etl = df_campaigndates_etl.rename(columns = {'effective_status':'campaign_effective_status'})
df_campaigndates_etl

"""## **Actions e custom_ids**"""

action_infos_etl = insights_level1_infos[['ad_id','date_start','publisher_platform','actions']]

action_infos = []
for ad, publ,date,actions in zip(action_infos_etl['ad_id'],action_infos_etl['publisher_platform'],action_infos_etl['date_start'],action_infos_etl['actions']):
  try:
    df_action_row = pd.json_normalize(actions)
    df_action_row['ad_id']       = ad
    df_action_row['publisher_platform'] = publ
    df_action_row['date_start'] = date
    action_infos.append(df_action_row)
  except:
    pass
action_infos_etl = pd.concat(action_infos)
action_infos_etl = pd.pivot_table(action_infos_etl,index=['ad_id','publisher_platform','date_start'],columns='action_type',values='value', aggfunc=np.max, fill_value=0)
action_infos_etl.reset_index(inplace=True)

action_infos_etl.columns = action_infos_etl.columns.astype(str).str.replace(".", "_")
action_infos_etl = action_infos_etl.reset_index()

action_columns = action_infos_etl.columns
conversion_columns = []
for item in range(len(action_columns)):
  if action_columns[item][:25] == 'offsite_conversion_custom':
    conversion_columns.append(action_columns[item])
  elif action_columns[item] == 'ad_id':
    conversion_columns.append(action_columns[item])
  elif action_columns[item] == 'publisher_platform':
    conversion_columns.append(action_columns[item])
  elif action_columns[item] == 'date_start':
    conversion_columns.append(action_columns[item])
value = []
offsite_conversion_custom_actions = action_infos_etl[conversion_columns]
offsite_conversion_custom_actions = pd.melt(offsite_conversion_custom_actions,id_vars=['ad_id', 'publisher_platform','date_start'])
offsite_conversion_custom_actions.rename(columns={'action_type':'offsite_conversion_custom_id'},inplace=True)
offsite_conversion_custom_actions.rename(columns={'value':'offsite_conversion_custom_actions'},inplace=True)
for row in offsite_conversion_custom_actions['offsite_conversion_custom_id']:
  value.append(row.split('_')[3])
offsite_conversion_custom_actions['offsite_conversion_custom_id'] = value

for item in range(len(action_columns)):
  if action_columns[item][:25] == 'offsite_conversion_custom':
    action_infos_etl.drop(action_columns[item],1,inplace=True)
  else:
    action_infos_etl.rename(columns={action_columns[item]:'actions_'+action_columns[item]},inplace=True)

offsite_conversion_custom_actions = offsite_conversion_custom_actions.loc[(offsite_conversion_custom_actions != 0).all(axis=1), :]

"""## **Action values**"""

df_action_values_etl = insights_level1_infos[['ad_id','date_start','publisher_platform','action_values']]

df_action_values = []
for ad, publ,date,action_values in zip(df_action_values_etl['ad_id'],df_action_values_etl['publisher_platform'],df_action_values_etl['date_start'],df_action_values_etl['action_values']):
  try:
    df_action_value_row = pd.json_normalize(action_values)
    df_action_value_row['ad_id']       = ad
    df_action_value_row['publisher_platform'] = publ
    df_action_value_row['date_start']       = date
    df_action_values.append(df_action_value_row)
  except:
    pass

df_action_values_etl = pd.concat(df_action_values)
df_action_values_etl = pd.pivot_table(df_action_values_etl,index=['ad_id','publisher_platform','date_start'],columns='action_type',values='value', aggfunc=np.max, fill_value=0)
df_action_values_etl = df_action_values_etl.reset_index()
df_action_values_etl.columns = df_action_values_etl.columns.astype(str).str.replace(".", "_")


action_columns = df_action_values_etl.columns
conversion_columns = []
for item in range(len(action_columns)):
  if action_columns[item][:25] == 'offsite_conversion_custom':
    conversion_columns.append(action_columns[item])
  elif action_columns[item] == 'ad_id':
    conversion_columns.append(action_columns[item])
  elif action_columns[item] == 'publisher_platform':
    conversion_columns.append(action_columns[item])
  elif action_columns[item] == 'date_start':
    conversion_columns.append(action_columns[item])
value = []
offsite_conversion_custom_action_values = df_action_values_etl[conversion_columns]
offsite_conversion_custom_action_values = pd.melt(offsite_conversion_custom_action_values,id_vars=['ad_id', 'publisher_platform','date_start'])
offsite_conversion_custom_action_values.rename(columns={'action_type':'offsite_conversion_custom_id'},inplace=True)
offsite_conversion_custom_action_values.rename(columns={'value':'offsite_conversion_custom_action_values'},inplace=True)
for row in offsite_conversion_custom_action_values['offsite_conversion_custom_id']:
  value.append(row.split('_')[3])
offsite_conversion_custom_action_values['offsite_conversion_custom_id'] = value


action_value_columns = df_action_values_etl.columns
for item in range(len(action_value_columns)):
  if action_value_columns[item][:25] == 'offsite_conversion_custom':
    df_action_values_etl.drop(action_value_columns[item],1,inplace=True)
  else:
    df_action_values_etl.rename(columns={action_value_columns[item]:'action_values_'+action_value_columns[item]},inplace=True)

offsite_conversion_custom_action_values = offsite_conversion_custom_action_values.loc[(offsite_conversion_custom_action_values != 0).all(axis=1), :]

"""## **outbound_clicks**"""

df_outbound_clicks_etl = insights_level1_infos[['ad_id','date_start','publisher_platform','outbound_clicks']]
df_outbound_clicks = []
for ad, publ,date,outbounds in zip(df_outbound_clicks_etl['ad_id'],df_outbound_clicks_etl['publisher_platform'],df_outbound_clicks_etl['date_start'],df_outbound_clicks_etl['outbound_clicks']):
  try:
    df_outbound_clicks_row = pd.json_normalize(outbounds)
    df_outbound_clicks_row['ad_id'] = ad
    df_outbound_clicks_row['publisher_platform'] = publ
    df_outbound_clicks_row['date_start'] = date
    df_outbound_clicks.append(df_outbound_clicks_row)
  except:
    pass

df_outbound_clicks_etl = pd.concat(df_outbound_clicks)
df_outbound_clicks_etl = pd.pivot_table(df_outbound_clicks_etl,index=['ad_id','publisher_platform','date_start'],columns='action_type',values='value', aggfunc=np.max, fill_value=0)
df_outbound_clicks_etl = df_outbound_clicks_etl.reset_index()
df_outbound_clicks_etl = df_outbound_clicks_etl.rename(columns = {'outbound_click':'outbound_clicks_outbound_click'})

"""## **video_30_sec**"""

df_videos_30_sec_etl = insights_level1_infos[['ad_id','date_start','publisher_platform','video_30_sec_watched_actions']]
df_videos_30_sec = []
for ad, publ,date,video_30_sec in zip(df_videos_30_sec_etl['ad_id'],df_videos_30_sec_etl['publisher_platform'],df_videos_30_sec_etl['date_start'],df_videos_30_sec_etl['video_30_sec_watched_actions']):
  try:
    df_video_30_sec_row = pd.json_normalize(video_30_sec)
    df_video_30_sec_row['ad_id'] = ad
    df_video_30_sec_row['publisher_platform'] = publ
    df_video_30_sec_row['date_start'] = date
    df_videos_30_sec.append(df_video_30_sec_row)
  except:
    pass

df_videos_30_sec_etl = pd.concat(df_videos_30_sec)
df_videos_30_sec_etl = pd.pivot_table(df_videos_30_sec_etl,index=['ad_id','publisher_platform','date_start'],columns='action_type',values='value', aggfunc=np.max, fill_value=0)
df_videos_30_sec_etl = df_videos_30_sec_etl.reset_index() 
df_videos_30_sec_etl = df_videos_30_sec_etl.rename(columns = {'video_view':'video_30_sec_watched_actions_video_view'})

"""## **video_p100**"""

df_videos_p100_etl = insights_level1_infos[['ad_id','date_start','publisher_platform','video_p100_watched_actions']]
df_videos_p100 = []
for ad, publ,date,video_p100 in zip(df_videos_p100_etl['ad_id'],df_videos_p100_etl['publisher_platform'],df_videos_p100_etl['date_start'],df_videos_p100_etl['video_p100_watched_actions']):
  try:
    df_video_p100_row = pd.json_normalize(video_p100)
    df_video_p100_row['ad_id'] = ad
    df_video_p100_row['publisher_platform'] = publ
    df_video_p100_row['date_start'] = date
    df_videos_p100.append(df_video_p100_row)
  except:
    pass

df_videos_p100_etl = pd.concat(df_videos_p100)
df_videos_p100_etl = pd.pivot_table(df_videos_p100_etl,index=['ad_id','publisher_platform','date_start'],columns='action_type',values='value', aggfunc=np.max, fill_value=0)
df_videos_p100_etl = df_videos_p100_etl.reset_index() 
df_videos_p100_etl = df_videos_p100_etl.rename(columns = {'video_view':'video_p100_watched_actions_video_view'})

"""## **videos_p50**"""

df_videos_p50_etl = insights_level1_infos[['ad_id','date_start','publisher_platform','video_p50_watched_actions']]
df_videos_p50 = []
for ad, publ,date,video_p50 in zip(df_videos_p50_etl['ad_id'],df_videos_p50_etl['publisher_platform'],df_videos_p50_etl['date_start'],df_videos_p50_etl['video_p50_watched_actions']):
  try:
    df_video_p50_row = pd.json_normalize(video_p50)
    df_video_p50_row['ad_id'] = ad
    df_video_p50_row['publisher_platform'] = publ
    df_video_p50_row['date_start'] = date
    df_videos_p50.append(df_video_p50_row)
  except:
    pass

df_videos_p50_etl = pd.concat(df_videos_p50)
df_videos_p50_etl = pd.pivot_table(df_videos_p50_etl,index=['ad_id','publisher_platform','date_start'],columns='action_type',values='value', aggfunc=np.max, fill_value=0)
df_videos_p50_etl = df_videos_p50_etl.reset_index() 
df_videos_p50_etl = df_videos_p50_etl.rename(columns = {'video_view':'video_p50_watched_actions_video_view'})

"""## **videos_p75**"""

df_videos_p75_etl = insights_level1_infos[['ad_id','date_start','publisher_platform','video_p75_watched_actions']]
df_videos_p75 = []
for ad, publ,date,video_p75 in zip(df_videos_p75_etl['ad_id'],df_videos_p75_etl['publisher_platform'],df_videos_p75_etl['date_start'],df_videos_p75_etl['video_p75_watched_actions']):
  try:
    df_video_p75_row = pd.json_normalize(video_p75)
    df_video_p75_row['ad_id'] = ad
    df_video_p75_row['publisher_platform'] = publ
    df_video_p75_row['date_start'] = date
    df_videos_p75.append(df_video_p75_row)
  except:
    pass

df_videos_p75_etl = pd.concat(df_videos_p75)
df_videos_p75_etl = pd.pivot_table(df_videos_p75_etl,index=['ad_id','publisher_platform','date_start'],columns='action_type',values='value', aggfunc=np.max, fill_value=0)
df_videos_p75_etl = df_videos_p75_etl.reset_index() 
df_videos_p75_etl = df_videos_p75_etl.rename(columns = {'video_view':'video_p75_watched_actions_video_view'})

"""## **videos_p95**"""

df_videos_p95_etl = insights_level1_infos[['ad_id','date_start','publisher_platform','video_p95_watched_actions']]
df_videos_p95 = []
for ad, publ,date,video_p95 in zip(df_videos_p95_etl['ad_id'],df_videos_p95_etl['publisher_platform'],df_videos_p95_etl['date_start'],df_videos_p95_etl['video_p95_watched_actions']):
  try:
    df_video_p95_row = pd.json_normalize(video_p95)
    df_video_p95_row['ad_id'] = ad
    df_video_p95_row['publisher_platform'] = publ
    df_video_p95_row['date_start'] = date
    df_videos_p95.append(df_video_p95_row)
  except:
    pass

df_videos_p95_etl = pd.concat(df_videos_p95)
df_videos_p95_etl = pd.pivot_table(df_videos_p95_etl,index=['ad_id','publisher_platform','date_start'],columns='action_type',values='value', aggfunc=np.max, fill_value=0)
df_videos_p95_etl = df_videos_p95_etl.reset_index() 
df_videos_p95_etl = df_videos_p95_etl.rename(columns = {'video_view':'video_p95_watched_actions_video_view'})

"""## **video_play**"""

df_video_play_actions_etl = insights_level1_infos[['ad_id','date_start','publisher_platform','video_play_actions']]
df_video_play_actions = []
for ad, publ,date,video_plays in zip(df_video_play_actions_etl['ad_id'],df_video_play_actions_etl['publisher_platform'],df_video_play_actions_etl['date_start'],df_video_play_actions_etl['video_play_actions']):
  try:
    df_video_play_actions_row = pd.json_normalize(video_plays)
    df_video_play_actions_row['ad_id'] = ad
    df_video_play_actions_row['publisher_platform'] = publ
    df_video_play_actions_row['date_start'] = date
    df_video_play_actions.append(df_video_play_actions_row)
  except:
    pass

df_video_play_actions_etl = pd.concat(df_video_play_actions)
df_video_play_actions_etl = pd.pivot_table(df_video_play_actions_etl,index=['ad_id','publisher_platform','date_start'],columns='action_type',values='value', aggfunc=np.max, fill_value=0)
df_video_play_actions_etl = df_video_play_actions_etl.reset_index()
df_video_play_actions_etl = df_video_play_actions_etl.rename(columns = {'video_view':'video_play_actions_video_view'})

"""## **video_thruplay**"""

df_video_thruplay_watched_actions_etl = insights_level1_infos[['ad_id','date_start','publisher_platform','video_thruplay_watched_actions']]
df_video_thruplay_watched_actions = []
for ad,publ,date,video_thruplay in zip(df_video_thruplay_watched_actions_etl['ad_id'],df_video_thruplay_watched_actions_etl['publisher_platform'],df_video_thruplay_watched_actions_etl['date_start'],df_video_thruplay_watched_actions_etl['video_thruplay_watched_actions']):
  try:
    df_video_thruplay_watched_actions_row = pd.json_normalize(video_thruplay)
    df_video_thruplay_watched_actions_row['ad_id'] = ad
    df_video_thruplay_watched_actions_row['publisher_platform'] = publ
    df_video_thruplay_watched_actions_row['date_start'] = date
    df_video_thruplay_watched_actions.append(df_video_thruplay_watched_actions_row)
  except:
    pass

df_video_thruplay_watched_actions_etl = pd.concat(df_video_thruplay_watched_actions)
df_video_thruplay_watched_actions_etl = pd.pivot_table(df_video_thruplay_watched_actions_etl,index=['ad_id','publisher_platform','date_start'],columns='action_type',values='value', aggfunc=np.max, fill_value=0)
df_video_thruplay_watched_actions_etl = df_video_thruplay_watched_actions_etl.reset_index()
df_video_thruplay_watched_actions_etl = df_video_thruplay_watched_actions_etl.rename(columns = {'video_view':'video_thruplay_watched_actions_video_view'})

"""## **conversion_values**"""

df_conversion_values_etl = insights_level1_infos[['ad_id','date_start','publisher_platform','conversion_values']]
df_conversion_values = []
for ad,publ,date,conversion in zip(df_conversion_values_etl['ad_id'],df_conversion_values_etl['publisher_platform'],df_conversion_values_etl['date_start'],df_conversion_values_etl['conversion_values']):
  try:
    df_conversion_values_row = pd.json_normalize(conversion)
    df_conversion_values_row['ad_id'] = ad
    df_conversion_values_row['publisher_platform'] = publ
    df_conversion_values_row['date_start'] = date
    df_conversion_values.append(df_conversion_values_row)
  except:
    pass

df_conversion_values_etl = pd.concat(df_conversion_values)
df_conversion_values_etl = pd.pivot_table(df_conversion_values_etl,index=['ad_id','publisher_platform','date_start'],columns='action_type',values='value', aggfunc=np.max, fill_value=0)
df_conversion_values_etl = df_conversion_values_etl.reset_index()

conversion_values_columns = df_conversion_values_etl.columns
for item in range(len(conversion_values_columns)):
  df_conversion_values_etl.rename(columns={conversion_values_columns[item]:'conversion_values_'+conversion_values_columns[item]},inplace=True)

"""## **conversions**"""

df_conversions_etl = insights_level1_infos[['ad_id','date_start','publisher_platform','conversions']]
df_conversions = []
for ad,publ,date,conversion in zip(df_conversions_etl['ad_id'],df_conversions_etl['publisher_platform'],df_conversions_etl['date_start'],df_conversions_etl['conversions']):
  try:
    df_conversions_row = pd.json_normalize(conversion)
    df_conversions_row['ad_id'] = ad
    df_conversions_row['publisher_platform'] = publ
    df_conversions_row['date_start'] = date
    df_conversions.append(df_conversions_row)
  except:
    pass

df_conversions_etl = pd.concat(df_conversions)
df_conversions_etl = pd.pivot_table(df_conversions_etl,index=['ad_id','publisher_platform','date_start'],columns='action_type',values='value', aggfunc=np.max, fill_value=0)
df_conversions_etl = df_conversions_etl.reset_index()

conversions_columns = df_conversions_etl.columns
for item in range(len(conversions_columns)):
  df_conversions_etl.rename(columns={conversions_columns[item]:'conversions_'+conversions_columns[item]},inplace=True)

"""# **JOIN DATAFRAMES**"""

try:
  final_table = insights_level1_infos_etl.merge(df_adcreatives_etl,left_on=['ad_id'],right_on=['ad_id'],how='left')
except:
  pass
try:
  final_table = final_table.merge(df_adreach_etl,left_on=['ad_id'],right_on=['ad_id'],how='left')
except:
  pass
try:
  final_table = final_table.merge(df_addates_etl,left_on='ad_id',right_on='ad_id',how='left')
except:
  pass
try:
  final_table = final_table.merge(df_campaignreach_etl,left_on=['campaign_id'],right_on=['campaign_id'],how='left')
except:
  pass
try:
  final_table = final_table.merge(df_campaignreach_daily_etl,left_on=['campaign_id','date_start'],right_on=['campaign_id','date_start'],how='left')
except:
  pass
try:
  final_table = final_table.merge(df_campaigndates_etl,left_on='campaign_id',right_on='campaign_id',how='left')  
except:
  pass

try:
  final_table = final_table.merge(action_infos_etl,left_on=['ad_id','date_start','publisher_platform'],right_on=['actions_ad_id','actions_date_start','actions_publisher_platform'],how='left')
except:
  pass
try:
  final_table = final_table.merge(df_action_values_etl,left_on=['ad_id','date_start','publisher_platform'],right_on=['action_values_ad_id','action_values_date_start','action_values_publisher_platform'],how='left')
except:
  pass
try:
  final_table = final_table.merge(offsite_conversion_custom_actions,left_on=['ad_id','date_start','publisher_platform'],right_on=['ad_id','date_start','publisher_platform'],how='left')
except:
  pass
try:
  final_table = final_table.merge(offsite_conversion_custom_action_values,left_on=['ad_id','date_start','publisher_platform','offsite_conversion_custom_id'],right_on=['ad_id','date_start','publisher_platform','offsite_conversion_custom_id'],how='left')
except:
  pass
try:
  final_table = final_table.merge(df_outbound_clicks_etl,left_on=['ad_id','date_start','publisher_platform'],right_on=['ad_id','date_start','publisher_platform'],how='left')
except:
  pass
try:
  final_table = final_table.merge(df_conversion_values_etl,left_on=['ad_id','date_start','publisher_platform'],right_on=['conversion_values_ad_id','conversion_values_date_start','conversion_values_publisher_platform'],how='left')
except:
  pass
try:
  final_table = final_table.merge(df_conversions_etl,left_on=['ad_id','date_start','publisher_platform'],right_on=['conversions_ad_id','conversions_date_start','conversions_publisher_platform'],how='left')
except:
  pass

try:
  final_table = final_table.merge(df_videos_30_sec_etl,left_on=['ad_id','date_start','publisher_platform'],right_on=['ad_id','date_start','publisher_platform'],how='left')
except:
  pass
try:
  final_table = final_table.merge(df_videos_p100_etl,left_on=['ad_id','date_start','publisher_platform'],right_on=['ad_id','date_start','publisher_platform'],how='left')
except:
  pass
try:
  final_table = final_table.merge(df_videos_p95_etl,left_on=['ad_id','date_start','publisher_platform'],right_on=['ad_id','date_start','publisher_platform'],how='left')
except:
  pass
try:
  final_table = final_table.merge(df_videos_p75_etl,left_on=['ad_id','date_start','publisher_platform'],right_on=['ad_id','date_start','publisher_platform'],how='left')
except:
  pass
try:
  final_table = final_table.merge(df_videos_p50_etl,left_on=['ad_id','date_start','publisher_platform'],right_on=['ad_id','date_start','publisher_platform'],how='left')
except:
  pass
try:
  final_table = final_table.merge(df_video_play_actions_etl,left_on=['ad_id','date_start','publisher_platform'],right_on=['ad_id','date_start','publisher_platform'],how='left')
except:
  pass
try:
  final_table = final_table.merge(df_video_thruplay_watched_actions_etl,left_on=['ad_id','date_start','publisher_platform'],right_on=['ad_id','date_start','publisher_platform'],how='left')
except:
  pass

"""# **Final ETL**"""

drop_specific_columns = ['adcreative_status','post_message','post_type','adcreative_id','page_id','post_id','post_url','reach_ad','frequency_ad'
                        ,'ad_created_time','reach_campaign','frequency_campaign','reach_campaign_daily','frequency_campaign_daily'
                        ,'created_time','stop_time'
                        ]
final_table.drop(drop_specific_columns,1,inplace=True)

drop_default_columns = ['actions_index','actions_ad_id','actions_publisher_platform','actions_date_start'
                ,'actions_add_to_cart','actions_complete_registration','actions_initiate_checkout'
                ,'actions_purchase'
                ,'actions_search','actions_view_content','action_values_ad_id','action_values_publisher_platform'
                ,'action_values_date_start','action_values_add_to_cart','action_values_initiate_checkout'
                ,'conversion_values_ad_id','conversion_values_publisher_platform','conversion_values_date_start'
                ,'conversions_ad_id','conversions_publisher_platform','conversions_date_start'
                ]

for column in drop_default_columns:
  try:
    final_table.drop(column,1,inplace=True)
  except:
    pass

final_table.to_csv('facebook_ads_mkt.csv',sep='|')
