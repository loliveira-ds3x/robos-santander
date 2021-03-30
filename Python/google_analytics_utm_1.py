from Packages.Main import GoogleAPI_main

api_type = 'simple_report'
crawler_name = 'google_analytics_utm_1'
VIEW_ID = ['156719244']
info_level = 'basic'
period = 'day'

report_period = [{'startDate': '2020-12-01', 'endDate': '2020-12-31'}]
report_dimensions = [{'name': 'ga:date'},
                     {'name': 'ga:campaign'},
                     {'name': 'ga:adContent'},
                     {'name': 'ga:pagePath'},
                     {'name': 'ga:dcmClickSite'},
                     {'name': 'ga:dimension45'},
                     {'name': 'ga:dimension46'}]
                     
report_metrics = [{'expression': 'ga:sessions'}]

selected_columns = ['date' ,'campaign','adContent','pagePath', 'dcmClickSite','dimension45','dimension46','accountId_hierarchy','name_account', 'webPropertyId' ,'name'            ,'level'            ,'websiteUrl_wp'          ,'currency'        ,'type'        ,'websiteUrl_hierarchy','profileId' ,'name_profile', 'sessions','uploadtime', 'info', 'period']
column_names =     ['tempo','campaign','adContent','pagePath', 'dcmClickSite','utm_mmm'    ,'utm_id_sts' ,'account_id'         ,'account_name', 'webproperty_id','webproperty_name','webproperty_level','webproperty_website_url','profile_currency','profile_type','profile_website_url' ,'profile_id','profile_name', 'sessions','upload_time','info', 'period']


GoogleAPI_main.main(api_type=api_type,crawler_name=crawler_name, info_level=info_level, period=period, VIEW_ID=VIEW_ID, selected_columns=selected_columns, column_names=column_names,report_period=report_period,report_dimensions=report_dimensions, report_metrics=report_metrics)