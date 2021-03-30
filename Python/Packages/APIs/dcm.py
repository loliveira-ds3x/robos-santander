import argparse
import io
import os
import sys
from googleapiclient import http
from oauth2client import client
import time
import pandas as pd

CHUNK_SIZE = 32 * 1024 * 1024

def get_file_id(analytics=None,profile_id=None,report_id=None):
    report_file = analytics.reports().run(profileId=profile_id, reportId=report_id).execute()
    file_id = report_file['id']
    return file_id

def download_file(analytics=None, file_id=None, report_id=None,file_name=None):
    report_file = analytics.files().get(
        reportId=report_id, fileId=file_id).execute()

    if report_file['status'] == 'REPORT_AVAILABLE':
        # Prepare a local file to download the report contents to.
        out_file = io.FileIO('/home/ds3x/robos-santander/Outputs/'+file_name+'.csv', mode='wb')

        # Create a get request.
        request = analytics.files().get_media(reportId=report_id, fileId=file_id)

        # Create a media downloader instance.
        # Optional: adjust the chunk size used when downloading the file.
        downloader = http.MediaIoBaseDownload(out_file, request, chunksize=CHUNK_SIZE)

        # Execute the get request and download the file.
        download_finished = False
        while download_finished is False:
            _, download_finished = downloader.next_chunk()
    else:
        print('report não pronto')

def elt_csv(file_name=None,skiped_rows=None,last_rows=None,crawler_name=None):
    
    try:
        dcm_final_table = pd.read_csv('/home/ds3x/robos-santander/Outputs/'+file_name+'.csv',skiprows=skiped_rows)
    except Exception as e:
        print('etl csv to pd')
        print(e)
        print('etl csv to pd')
    try:
        dcm_final_table.drop(dcm_final_table.tail(last_rows).index, inplace = True)
    except Exception as e:
        print(e)
        print('etl drop last rows')
    try:
        dcm_final_table.to_csv('/home/ds3x/robos-santander/Outputs/'+crawler_name+'.csv', index = False, header=True, sep='|')
    except Exception as e:
        print(e)
        print('etl df to csv')