# import libraries
from credentials import client_id, client_secret, redirect_uri, access_code, access_token, refresh_token
from oauth2client.client import OAuth2WebServerFlow, GoogleCredentials
import httplib2
from googleapiclient.discovery import build