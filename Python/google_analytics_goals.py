from Packages.Main import GoogleAPI_main

api_type = 'simple_report'
crawler_name = 'google_analytics_goals'
VIEW_ID = ['169440724','175359674', '175409556']
info_level = 'basic'
period = 'day'

report_period = [{'startDate': '2020-12-01', 'endDate': '2020-12-31'}]
report_dimensions = [{'name': 'ga:date'},
                    {'name': 'ga:dcmClickSite'},
                    {'name': 'ga:source'},
                    {'name': 'ga:medium'},
                    {'name': 'ga:campaign'},
                    {'name': 'ga:adContent'},
                    {'name': 'ga:keyword'}
]

report_metrics = [
            {'expression': 'ga:sessions'},
            {'expression': 'ga:pageviews'},
            {'expression': 'ga:bounces'},
            {'expression': 'ga:sessionDuration'},
            {'expression': 'ga:goal1Completions'},
            {'expression': 'ga:goal2Completions'},
            {'expression': 'ga:goal3Completions'},
            {'expression': 'ga:goal4Completions'},
            {'expression': 'ga:goal5Completions'},
            {'expression': 'ga:goal6Completions'},
            {'expression': 'ga:goal7Completions'},
            {'expression': 'ga:goal8Completions'},
            {'expression': 'ga:goal9Completions'},
            {'expression': 'ga:goal10Completions'},
            {'expression': 'ga:goal11Completions'},
            {'expression': 'ga:goal12Completions'},
            {'expression': 'ga:goal13Completions'},
            {'expression': 'ga:goal14Completions'},
            {'expression': 'ga:goal15Completions'},
            {'expression': 'ga:goal16Completions'},
            {'expression': 'ga:goal17Completions'},
            {'expression': 'ga:goal18Completions'},
            {'expression': 'ga:goal19Completions'},
            {'expression': 'ga:goal20Completions'}
]
selected_columns = ['date' ,'dcmClickSite','source','medium','campaign', 'adContent', 'keyword', 'accountId_hierarchy','name_account', 'webPropertyId' ,'name'            ,'level'            ,'websiteUrl_wp'          ,'currency'        ,'type'        ,'websiteUrl_hierarchy','profileId' ,'name_profile', 'bounces', 'pageviews', 'sessions', 'sessionDuration', 'goal1Completions', 'goal2Completions','goal3Completions', 'goal4Completions','goal5Completions','goal6Completions', 'goal7Completions','goal8Completions', 'goal9Completions','goal10Completions','goal11Completions', 'goal12Completions','goal13Completions', 'goal14Completions','goal15Completions','goal16Completions', 'goal17Completions','goal18Completions', 'goal19Completions','goal20Completions','uploadtime', 'info', 'period']
column_names =     ['tempo','dcmClickSite','source','medium','campaign', 'ad_content', 'keyword','account_id'         ,'account_name', 'webproperty_id','webproperty_name','webproperty_level','webproperty_website_url','profile_currency','profile_type','profile_website_url' ,'profile_id','profile_name', 'bounces', 'pageviews', 'sessions', 'session_duration', 'goal1Completions', 'goal2Completions','goal3Completions', 'goal4Completions','goal5Completions','goal6Completions', 'goal7Completions','goal8Completions', 'goal9Completions','goal10Completions','goal11Completions', 'goal12Completions','goal13Completions', 'goal14Completions','goal15Completions','goal16Completions', 'goal17Completions','goal18Completions', 'goal19Completions','goal20Completions','upload_time','info', 'period']

GoogleAPI_main.main(api_type=api_type,crawler_name=crawler_name, info_level=info_level, period=period, VIEW_ID=VIEW_ID, selected_columns=selected_columns, column_names=column_names,report_period=report_period,report_dimensions=report_dimensions, report_metrics=report_metrics)