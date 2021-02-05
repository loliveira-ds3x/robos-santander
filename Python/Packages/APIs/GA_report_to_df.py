import pandas as pd

def response2df(report_json=None,VIEW_ID=None, now=None, info_level=None, period=None):
    report = report_json.get('reports', [])[0] # expected just one report
    # headers
    header_dimensions = report.get('columnHeader', {}).get('dimensions', [])
    header_metrics = [value['name'] for value in report.get('columnHeader', {}).get('metricHeader', {}).get('metricHeaderEntries', [])]
    headers = header_dimensions + header_metrics
    headers = list(map((lambda x: x.split(':', 1)[-1]), headers)) # removes "ga:" from each column
    # values
    values = []
    rows = report.get('data', {}).get('rows', [])
    for row in rows:
        values_dimensions = row.get('dimensions', [])
        values_metrics = row.get('metrics', [])[0].get('values', [])
        values.append(values_dimensions + values_metrics)
    # to dataframe
    df = pd.DataFrame(columns=headers, data=values)
    df['profileId'] = VIEW_ID
    df['uploadtime'] = now
    df['info'] = info_level
    df['period'] = period
    return df

def Multiple_response2df(report_json=None,VIEW_ID=None, now=None, info_level=None, period=None,funnel_step=None,description=None):
    report = report_json.get('reports', [])[0] # expected just one report
    # headers
    header_dimensions = report.get('columnHeader', {}).get('dimensions', [])
    header_metrics = [value['name'] for value in report.get('columnHeader', {}).get('metricHeader', {}).get('metricHeaderEntries', [])]
    headers = header_dimensions + header_metrics
    headers = list(map((lambda x: x.split(':', 1)[-1]), headers)) # removes "ga:" from each column
    # values
    values = []
    rows = report.get('data', {}).get('rows', [])
    for row in rows:
        values_dimensions = row.get('dimensions', [])
        values_metrics = row.get('metrics', [])[0].get('values', [])
        values.append(values_dimensions + values_metrics)
    # to dataframe
    df = pd.DataFrame(columns=headers, data=values)
    df['profileId'] = VIEW_ID
    df['uploadtime'] = now
    df['info'] = info_level
    df['period'] = period
    df['funnel_step'] = funnel_step
    df['description'] = description
    return df