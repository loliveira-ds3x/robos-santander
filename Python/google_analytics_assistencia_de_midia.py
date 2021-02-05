from Packages.Main import GoogleAPI_main

api_type = 'simple_report'
crawler_name = 'google_analytics_assistencia_de_midia'
VIEW_ID = '236533316'
info_level = 'basic'
period = 'day'

report_period = [{'startDate': '2017-01-01', 'endDate': '2018-01-01'}]
report_dimensions = [{'name': 'ga:date'},
                     {'name': 'mcf:conversionGoalNumber'}]

report_metrics = [{'expression': 'mcf:assistedConversions'},
            {'expression': 'mcf:lastInteractionConversions'}]

selected_columns = ['date', 'accountId_account','name_account', 'webPropertyId_wb' ,'profileId_profile','name'        ,'conversionGoalNumber' ,'assistedConversions', 'lastInteractionConversions', 'info', 'period']
column_names =     ['tempo','account_id'      ,'account_name' , 'webproperty_id'   ,'profile_id'       ,'profile_name','goal'                 ,'assisted_conversion', 'last_interaction_conversions', 'info', 'period']


GoogleAPI_main.main(crawler_name=crawler_name, VIEW_ID=VIEW_ID, info_level=info_level, period=period, selected_columns=selected_columns, column_names=column_names,report_period=report_period,report_dimensions=report_dimensions, report_metrics=report_metrics)