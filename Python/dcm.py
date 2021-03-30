from Packages.Main import GoogleAPI_main

profile_id='4307950'
report_id = '694215297'
file_name = 'DCM_SANTANDER_BBI'
skiped_rows = 10
last_rows = 1
crawler_name = 'dcm'
api_type = 'dcm_report'

GoogleAPI_main.main(api_type=api_type,crawler_name=crawler_name,profile_id=profile_id,report_id=report_id,file_name=file_name
                   ,skiped_rows=skiped_rows,last_rows=last_rows)