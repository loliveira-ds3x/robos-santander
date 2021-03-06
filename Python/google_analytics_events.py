from Packages.Main import GoogleAPI_main

api_type = 'simple_report'
crawler_name = 'google_analytics_events'
#VIEW_ID = '236533316'
info_level = 'basic'
period = 'day'

report_period = [{'startDate': '2017-01-01', 'endDate': '2018-01-01'}]
report_dimensions = [{'name': 'ga:date'}]
report_metrics = [{'expression': 'ga:users'},
            {'expression': 'ga:sessions'},
            {'expression': 'ga:pageviews'},
            {'expression': 'ga:bounces'},
            {'expression': 'ga:timeOnPage'},
            {'expression': 'ga:uniquePageviews'},
            {'expression': 'ga:newUsers'}]
#report_filters_dimensions = 'ga:eventAction=~(clicou|clic|click),ga:eventCategory=~(clicou|clic|click),ga:eventAction=~(clicou|clic|click)'

report_filters_dimensions = [
    [
    {'operator': 'OR',
        'filters': 
        [
        {
            'dimensionName': 'ga:eventAction',
            'operator': 'PARTIAL',
            'expressions': ['(clicou|clic|click)']
        }
        ]
    }
    ],
    [
    {'operator': 'OR',
        'filters': 
        [
        {
            'dimensionName': 'ga:eventCategory',
            'operator': 'PARTIAL',
            'expressions': ['(clicou|clic|click)']
        }
        ]
    }
    ]
]

selected_columns = ['date' ,'accountId_account','name_account', 'webPropertyId_wb' ,'name_wb'         ,'level'            ,'websiteUrl_wb'          ,'currency'        ,'type'        ,'websiteUrl_profile' ,'profileId_profile','name'        ,'users', 'bounces', 'newUsers' , 'pageviews', 'sessions', 'timeOnPage',  'uniquePageviews', 'uploadtime', 'info', 'period']
column_names =     ['tempo', 'account_id'      ,'account_name', 'webproperty_id'   ,'webproperty_name','webproperty_level','webproperty_website_url','profile_currency','profile_type','profile_website_url','profile_id'       ,'profile_name','users', 'bounces', 'new_users', 'pageviews', 'sessions', 'time_on_page','unique_pageviews','upload_time','info', 'period']


GoogleAPI_main.main(api_type=api_type, crawler_name=crawler_name, info_level=info_level, period=period, selected_columns=selected_columns, column_names=column_names,report_period=report_period,report_dimensions=report_dimensions, report_metrics=report_metrics)