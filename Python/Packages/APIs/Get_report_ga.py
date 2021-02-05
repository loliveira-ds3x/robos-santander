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