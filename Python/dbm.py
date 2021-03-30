from Packages.Main import GoogleAPI_main

file_name = 'santander_daily'
query_id = '632711311'
last_rows = 28
crawler_name = 'dbm'
api_type = 'dbm_report'

GoogleAPI_main.main(api_type=api_type,crawler_name=crawler_name,file_name=file_name
                   ,query_id=query_id,last_rows=last_rows)