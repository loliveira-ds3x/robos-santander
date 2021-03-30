import argparse
import io
import os
import sys
from googleapiclient import http
from oauth2client import client
import time
import pandas as pd
from contextlib import closing
from six.moves.urllib.request import urlopen

def download_file(analytics=None, query_id=None,file_name=None):
    query = (analytics.queries().getquery(queryId=query_id).execute())
    report_url = query['metadata']['googleCloudStoragePathForLatestReport']
    
    with open('/home/ds3x/robos-santander/Outputs/'+file_name+'.csv', 'wb') as output:
        with closing(urlopen(report_url)) as url:
            output.write(url.read())
    print('Download complete.')

def elt_csv(file_name=None,last_rows=None,crawler_name=None):
    
    try:
        dbm_final_table = pd.read_csv('/home/ds3x/robos-santander/Outputs/'+file_name+'.csv')
    except Exception as e:
        print('etl csv to pd')
        print(e)
        print('etl csv to pd')
    try:
        dbm_final_table.drop(dbm_final_table.tail(last_rows).index, inplace = True)
    except Exception as e:
        print(e)
        print('etl drop last rows')
    try:
        dbm_final_table.to_csv('/home/ds3x/robos-santander/Outputs/'+crawler_name+'.csv', index = False, header=True, sep='|')
    except Exception as e:
        print(e)
        print('etl df to csv')