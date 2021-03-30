from Packages.Main import GoogleAPI_main

api_type = 'multiple_simple_reports'
crawler_name = 'google_analytics_funnel_nc'
VIEW_ID = '156719244'
info_level = 'basic'
period = 'day'

funnel_step = ['Aprovado', 'CPF']
description = ['NÃO CORRENTISTA - NC', 'NÃO CORRENTISTA - NC']

report_period = [{'startDate': '2017-01-01', 'endDate': '2018-01-01'}]
report_dimensions = [{'name': 'ga:date'}]
report_metrics = [
                  [{'expression': 'ga:eventValue'}],
                  [{'expression': 'ga:eventValue'}]
                ]

report_filters_dimensions = [
    [
    {'operator': 'OR',
        'filters': 
        [
        {
            'dimensionName': 'ga:pagePath',
            'operator': 'PARTIAL',
            'expressions': ['pf/funil/cartoes.*cartao-aprovado']
        }
        ]
    }
    ],
    [
    {'operator': 'OR',
        'filters': 
        [
        {
            'dimensionName': 'ga:pagePath',
            'operator': 'PARTIAL',
            'expressions': ['funil/cartoes/.*cpf']
        }
        ]
    }
    ]
]

selected_columns = ['date' , 'accountId_account','name_account', 'webPropertyId_wb' ,'name_wb'         ,'level'            ,'websiteUrl_wb'          ,'currency'        ,'type'        ,'websiteUrl_profile' ,'profileId_profile','name'        ,'eventValue', 'uploadtime', 'info', 'period']
column_names =     ['tempo', 'account_id'       ,'account_name', 'webproperty_id'   ,'webproperty_name','webproperty_level','webproperty_website_url','profile_currency','profile_type','profile_website_url','profile_id'       ,'profile_name','eventValue', 'upload_time','info', 'period']

GoogleAPI_main.main(api_type=api_type,crawler_name=crawler_name, VIEW_ID=VIEW_ID, info_level=info_level, period=period, selected_columns=selected_columns, column_names=column_names,report_period=report_period,report_dimensions=report_dimensions, report_metrics=report_metrics,report_filters_dimensions=report_filters_dimensions, funnel_step=funnel_step, description=description)