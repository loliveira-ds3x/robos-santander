from Packages.Main import GoogleAPI_main

api_type = 'simple_report'
crawler_name = 'google_analytics_active_users'
VIEW_ID = ['156702689', '156708522', '166221744']
info_level = 'basic'
period = 'day'

report_period = [{'startDate': '2020-12-01', 'endDate': '2020-12-31'}]
report_dimensions = [{'name': 'ga:date'}]

report_metrics = [{'expression': 'ga:1dayUsers'},
                  {'expression': 'ga:7dayUsers'},
                  {'expression': 'ga:14dayUsers'},
                  {'expression': 'ga:28dayUsers'},
                  {'expression': 'ga:30dayUsers'}]

selected_columns = ['date', 'accountId_hierarchy','name_account', 'webPropertyId' ,'name'            ,'level'            ,'websiteUrl_wp'          ,'currency'        ,'type'        ,'websiteUrl_hierarchy','profileId' ,'name_profile' ,'1dayUsers', '7dayUsers', '14dayUsers'   ,'28dayUsers'    ,'30dayUsers','info', 'period']
column_names =     ['tempo','account_id'         ,'account_name', 'webproperty_id','webproperty_name','webproperty_level','webproperty_website_url','profile_currency','profile_type','profile_website_url' ,'profile_id','profile_name' ,'day_user' , 'week_user', 'two_week_user','four_week_user','month_user','info', 'period']

GoogleAPI_main.main(api_type=api_type,crawler_name=crawler_name, info_level=info_level, period=period, VIEW_ID=VIEW_ID, selected_columns=selected_columns, column_names=column_names,report_period=report_period,report_dimensions=report_dimensions, report_metrics=report_metrics)