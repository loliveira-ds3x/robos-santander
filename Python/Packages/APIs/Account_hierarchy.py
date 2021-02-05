import requests
import pandas as pd

def Get_account_infos(access_token=None):
    a1 = requests.get('https://www.googleapis.com/analytics/v3/management/accounts?access_token='+access_token)
    accounts_json = a1.json()
    account_infos = pd.json_normalize(accounts_json,['items'])
    account_infos = account_infos.rename(columns = {'id':'accountId'})
    return account_infos 

def Get_wp_infos(access_token=None):
    wp1 = requests.get('https://www.googleapis.com/analytics/v3/management/accounts/188545982/webproperties?access_token='+access_token)
    webproperties_json = wp1.json()
    webproperty_infos = pd.json_normalize(webproperties_json,['items'])
    webproperty_infos = webproperty_infos.rename(columns = {'id':'webPropertyId'})
    return webproperty_infos

def Get_profile_infos(access_token=None):
    p1 = requests.get('https://www.googleapis.com/analytics/v3/management/accounts/188545982/webproperties/UA-188545982-1/profiles?access_token='+access_token)
    profiles = p1.json()
    profile_infos = pd.json_normalize(profiles,['items'])
    profile_infos = profile_infos.rename(columns = {'id':'profileId'})
    return profile_infos
