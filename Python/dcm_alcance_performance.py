from Packages.Main import GoogleAPI_main

profile_id='4307950'
report_id = '707689126'
file_name = 'DCM_HUB_REACH_BBI'
skiped_rows = 13
last_rows = 2
crawler_name = 'dcm_alcance_performance'
api_type = 'dcm_report'

GoogleAPI_main.main(api_type=api_type,crawler_name=crawler_name,profile_id=profile_id,report_id=report_id,file_name=file_name
                   ,skiped_rows=skiped_rows,last_rows=last_rows)