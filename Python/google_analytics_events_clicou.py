from Packages.Main import GoogleAPI_main

api_type = 'simple_report'
crawler_name = 'google_analytics_events_clicou'
VIEW_ID = '236533316'
info_level = 'basic'
period = 'day'

report_period = [{'startDate': '2017-01-01', 'endDate': '2018-01-01'}]
report_dimensions = [{'name': 'ga:date'},
                     {'name': 'ga:pagePath'}]
report_metrics = [{'expression': 'ga:eventValue'},
                  {'expression': 'ga:totalEvents'},
                  {'expression': 'ga:uniqueEvents'}]

report_filters_dimensions = [
    [
    {'operator': 'OR',
        'filters': 
        [
        {
            'dimensionName': 'ga:eventAction',
            'operator': 'EXACT',
            'expressions': ['clicou']
        }
        ]
    }
    ]
]

selected_columns = ['date' ,'pagePath', 'accountId_account','name_account', 'webPropertyId_wb' ,'name_wb'         ,'level'            ,'websiteUrl_wb'          ,'currency'        ,'type'        ,'websiteUrl_profile' ,'profileId_profile','name'        ,'eventValue', 'totalEvents', 'uniqueEvents' , 'uploadtime', 'info', 'period']
column_names =     ['tempo','page_path','account_id'       ,'account_name', 'webproperty_id'   ,'webproperty_name','webproperty_level','webproperty_website_url','profile_currency','profile_type','profile_website_url','profile_id'       ,'profile_name','event_value','total_events','unique_events','upload_time','info', 'period']


GoogleAPI_main.main(api_type=api_type,crawler_name=crawler_name, VIEW_ID=VIEW_ID, info_level=info_level, period=period, selected_columns=selected_columns, column_names=column_names,report_period=report_period,report_dimensions=report_dimensions, report_metrics=report_metrics,report_filters_dimensions=report_filters_dimensions)