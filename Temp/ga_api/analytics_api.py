from oauth2client.client import OAuth2WebServerFlow, GoogleCredentials
import httplib2
from googleapiclient.discovery import build

import requests

token_url = 'https://oauth2.googleapis.com/token'
client_id = '959085883070-61rrk0v3ogpdf7d38o5i27ocj4sqles4.apps.googleusercontent.com'
client_secret = 'RXYi722AwIrVH_HO-x0V8Kkc'
refresh_token = '1//0hqj21TVBTcdWCgYIARAAGBESNwF-L9Irt0d3ExRAh5uYZZlt1GVK4B1QIPzXkNmODPjUTGZgZG4Vj07r2Td0YljtU34fcCZe1Vs'

headers = {"Content-Type" : "application/x-www-form-urlencoded"}

data = {'client_id': client_id,
        'client_secret': client_secret,
        'refresh_token':refresh_token,
        'grant_type': 'refresh_token',
        }
token_response = requests.post(token_url, data=data, headers=headers)
access_token = token_response.json().get('access_token')

print(client_id)
print(client_secret)
print(refresh_token)
print(access_token)


# create connection based on project credentials
flow = OAuth2WebServerFlow(client_id=client_id,
                           client_secret=client_secret,
                           scope='https://www.googleapis.com/auth/analytics.readonly',
                           redirect_uri=token_url)

credentials = GoogleCredentials(access_token, client_id, client_secret, refresh_token, 3920, 'https://accounts.google.com/o/oauth2/token', 'test')
http = httplib2.Http()
http = credentials.authorize(http)
analytics = build('analyticsreporting', 'v4', http=http)

VIEW_ID = '236645841'

def get_report(analytics):
  """Queries the Analytics Reporting API V4.

  Args:
    analytics: An authorized Analytics Reporting API V4 service object.
  Returns:
    The Analytics Reporting API V4 response.
  """
  return analytics.reports().batchGet(
      body={
        'reportRequests': [
        {
          'viewId': VIEW_ID,
          'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'today'}],
          'metrics': [{'expression': 'ga:sessions'}],
          'dimensions': [{'name': 'ga:source'}]
        }]
      }
  ).execute()

def print_response(response):
  """Parses and prints the Analytics Reporting API V4 response.

  Args:
    response: An Analytics Reporting API V4 response.
  """
  for report in response.get('reports', []):
    columnHeader = report.get('columnHeader', {})
    dimensionHeaders = columnHeader.get('dimensions', [])
    metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])

    for row in report.get('data', {}).get('rows', []):
      dimensions = row.get('dimensions', [])
      dateRangeValues = row.get('metrics', [])

      for header, dimension in zip(dimensionHeaders, dimensions):
        print (header + ': ' + dimension)

      for i, values in enumerate(dateRangeValues):
        print ('Date range: ' + str(i))
        for metricHeader, value in zip(metricHeaders, values.get('values')):
          print (metricHeader.get('name') + ': ' + value)

print_response(get_report(analytics))