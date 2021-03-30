import requests
import pandas as pd

def Get_account_infos(access_token=None):
    s = requests.get('https://www.googleapis.com/analytics/v3/management/accounts?access_token='+access_token)
    data1 = s.json()
    data2 = {}
    data3 = {}
    webproperty_links = []
    profile_links = []
    dados1 = []
    dados2 = []
    dados3 = []

    for item1 in data1['items']:

        dados1.append(item1)
        webproperty_links.append(item1['childLink']['href'])

    for wp in webproperty_links:
        data2 = requests.get(wp+'?access_token='+access_token).json()
        for item2 in data2['items']:
            dados2.append(item2)
            profile_links.append(item2['childLink']['href'])
    for views in profile_links:
        data3 = requests.get(views+'?access_token='+access_token).json()
        try:
            for item3 in data3['items']:
                dados3.append(item3)
        except: 
            dados3.append(None)
        
    account_infos = pd.DataFrame(dados1)
    account_infos = account_infos.rename(columns = {'id':'accountId'})

    webproperty_infos = pd.DataFrame(dados2)
    webproperty_infos = webproperty_infos.rename(columns = {'id':'webPropertyId'})

    profile_infos = pd.DataFrame(dados3)
    profile_infos = profile_infos.rename(columns = {'id':'profileId'})

    partial_hierarchy_table = pd.merge(profile_infos, account_infos, left_on='accountId',right_on='accountId',how='outer',suffixes=('_profile','_account'))
    hierarchy_table = pd.merge(partial_hierarchy_table, webproperty_infos, left_on='webPropertyId',right_on='webPropertyId',how='outer',suffixes=('_hierarchy','_wp'))


    return hierarchy_table

def Get_profiles_list(hierarchy_table):
    profiles_list = []
    profiles_list = hierarchy_table['profileId']
    return profiles_list