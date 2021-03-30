from Packages.Main import GoogleAPI_main

api_type = 'mcf_report'
crawler_name = 'google_analytics_assistencia_de_midia'
info_level = 'basic'
period = 'day'

VIEW_ID = ['169440724','175359674','175409556']
start_date = '2020-12-01'
end_date = '2020-12-31'
metrics = 'mcf:assistedConversions'
dimensions = 'mcf:conversionDate,mcf:conversionGoalNumber'

selected_columns = ['conversionDate', 'conversionGoalNumber','accountId_hierarchy','name_account', 'webPropertyId' ,'name'            ,'level'            ,'websiteUrl_wp'          ,'currency'        ,'type'        ,'websiteUrl_hierarchy','profileId' ,'name_profile', 'assistedConversions','uploadtime', 'info', 'period']
column_names =     ['tempo'         , 'goal'                ,'account_id'         ,'account_name', 'webproperty_id','webproperty_name','webproperty_level','webproperty_website_url','profile_currency','profile_type','profile_website_url' ,'profile_id','profile_name', 'assistedConversions','upload_time','info', 'period']


GoogleAPI_main.main(api_type=api_type,crawler_name=crawler_name, info_level=info_level, period=period, VIEW_ID=VIEW_ID, selected_columns=selected_columns, column_names=column_names,metrics=metrics,dimensions=dimensions,start_date=start_date,end_date=end_date)