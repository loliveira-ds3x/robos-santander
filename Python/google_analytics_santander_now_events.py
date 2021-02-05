from Packages.Main import GoogleAPI_main

api_type = 'simple_report'
crawler_name = 'google_analytics_santander_now_events'
VIEW_ID = '236533316'
info_level = 'basic'
period = 'day'

report_period = [{'startDate': '2017-01-01', 'endDate': '2018-01-01'}]
report_dimensions = [{'name': 'ga:date'},
                     {'name': 'ga:eventCategory'},
                     {'name': 'ga:eventLabel'},
                     {'name': 'ga:eventAction'}
                     ]
report_metrics = [{'expression': 'ga:totalEvents'},
            {'expression': 'ga:eventValue'},
            {'expression': 'ga:uniqueEvents'},
            {'expression': 'ga:pageviews'},
            {'expression': 'ga:pageviewsPerSession'},
            {'expression': 'ga:users'}]

selected_columns = ['date', 'eventCategory', 'eventLabel', 'eventAction', 'accountId_account','name_account', 'webPropertyId_wb' ,'name_wb'         ,'level'            ,'websiteUrl_wb'          ,'currency'        ,'type'        ,'websiteUrl_profile' ,'profileId_profile','name'        ,'totalEvents', 'eventValue' , 'uniqueEvents' , 'pageviews', 'pageviewsPerSession',  'users', 'uploadtime', 'info', 'period']
column_names =     ['tempo','event_category','event_label','event_action','account_id'      ,'account_name', 'webproperty_id'   ,'webproperty_name','webproperty_level','webproperty_website_url','profile_currency','profile_type','profile_website_url','profile_id'       ,'profile_name' ,'total_events','event_values','unique_events', 'pageviews', 'pageviews_per_session','users', 'upload_time','info', 'period']


GoogleAPI_main.main(crawler_name=crawler_name, VIEW_ID=VIEW_ID, info_level=info_level, period=period, selected_columns=selected_columns, column_names=column_names,report_period=report_period,report_dimensions=report_dimensions, report_metrics=report_metrics)