from Packages.Main import GoogleAPI_main

api_type = 'simple_report'
crawler_name = 'google_analytics_farol_mensal' 
VIEW_ID = ['218018311']
info_level = 'basic'
period = 'month'

report_period = [{'startDate': '2020-12-01', 'endDate': '2020-12-31'}]
report_dimensions = [{'name': 'ga:month'},
                     {'name': 'ga:year'},
                     {'name': 'ga:pagePath'}]
report_metrics = [{'expression': 'ga:users'},
            {'expression': 'ga:sessions'},
            {'expression': 'ga:pageviews'},
            {'expression': 'ga:bounces'},
            {'expression': 'ga:timeOnPage'},
            {'expression': 'ga:uniquePageviews'},
            {'expression': 'ga:newUsers'}]

selected_columns = ['month'  , 'year', 'pagePath' ,'accountId_hierarchy','name_account', 'webPropertyId' ,'name'            ,'level'            ,'websiteUrl_wp'          ,'currency'        ,'type'        ,'websiteUrl_hierarchy','profileId' ,'name_profile' ,'users', 'bounces', 'newUsers' , 'pageviews', 'sessions', 'timeOnPage',  'uniquePageviews', 'uploadtime', 'info', 'period']
column_names =     ['ano_mes', 'year', 'page_path','account_id'         ,'account_name', 'webproperty_id','webproperty_name','webproperty_level','webproperty_website_url','profile_currency','profile_type','profile_website_url' ,'profile_id','profile_name' ,'users', 'bounces', 'new_users', 'pageviews', 'sessions', 'time_on_page','unique_pageviews','upload_time','info', 'period']

GoogleAPI_main.main(api_type=api_type,crawler_name=crawler_name, info_level=info_level, period=period, VIEW_ID=VIEW_ID, selected_columns=selected_columns, column_names=column_names,report_period=report_period,report_dimensions=report_dimensions, report_metrics=report_metrics)