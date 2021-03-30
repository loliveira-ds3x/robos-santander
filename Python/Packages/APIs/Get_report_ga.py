import requests
import pandas as pd

def get_report(analytics=None, VIEW_ID=None, report_period=[], report_dimensions=[], report_metrics=[],report_filters_dimensions=[]):

    return analytics.reports().batchGet(body={'reportRequests': [{
        'viewId': VIEW_ID,
        'dateRanges': report_period,
        'dimensions': report_dimensions,
        'metrics': report_metrics,
        "dimensionFilterClauses": report_filters_dimensions

    }]}).execute()

def Multiple_reports_method(analytics=None, VIEW_ID=None, report_period=[],report_dimensions=[], report_metrics=[],report_filters_dimensions=[], funnel=[], desc=[]):
        return analytics.reports().batchGet(body={'reportRequests': [{
        'viewId': VIEW_ID,
        'dateRanges': report_period,
        'dimensions': report_dimensions,
        'metrics': report_metrics,
        "dimensionFilterClauses": report_filters_dimensions

        }]}).execute()

def Multichannel_funnel_reports_method(VIEW_ID='', access_token='',metrics='',dimensions='',start_date='',end_date=''):
    json_data = requests.get('https://www.googleapis.com/analytics/v3/data/mcf?ids=ga:'+VIEW_ID+'&metrics='+metrics+'&dimensions='+dimensions+'&start-date='+start_date+'&end-date='+end_date+'&access_token='+access_token).json()
    return json_data