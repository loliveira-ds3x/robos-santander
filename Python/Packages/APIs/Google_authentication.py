from oauth2client.client import OAuth2WebServerFlow, GoogleCredentials
import httplib2
from googleapiclient.discovery import build
import pandas as pd
from datetime import datetime
import requests

def Get_access_token (token_url=None,data={},headers={}):
    token_response = requests.post(token_url,data,headers)
    access_token = token_response.json().get('access_token')
    return access_token

def Create_service_ga(access_token=None,client_id=None, client_secret=None, refresh_token=None):
    credentials = GoogleCredentials(access_token, client_id, client_secret, refresh_token, 3920, 'https://accounts.google.com/o/oauth2/token', 'test')
    http = httplib2.Http()
    http = credentials.authorize(http)
    analytics = build('analyticsreporting', 'v4', http=http)
    return analytics 

def Create_service_dcm(access_token=None,client_id=None, client_secret=None, refresh_token=None):
    credentials = GoogleCredentials(access_token, client_id, client_secret, refresh_token, 3920, 'https://accounts.google.com/o/oauth2/token', 'test')
    http = httplib2.Http()
    http = credentials.authorize(http)
    analytics = build('dfareporting', 'v3.4', http=http)
    return analytics 

def Create_service_dbm(access_token=None,client_id=None, client_secret=None, refresh_token=None):
    credentials = GoogleCredentials(access_token, client_id, client_secret, refresh_token, 3920, 'https://accounts.google.com/o/oauth2/token', 'test')
    http = httplib2.Http()
    http = credentials.authorize(http)
    analytics = build('doubleclickbidmanager', 'v1.1', http=http)
    return analytics