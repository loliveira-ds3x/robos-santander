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

def Multichannel_funnel_report_to_df(json_data=None,VIEW_ID=None,now=None,info_level=None,period=None):
    
    headers = []
    date = []
    goal = []
    assisted_conversions = []
    
    for row in json_data['columnHeaders']:
        headers.append(row['name'])
        headers = list(map((lambda x: x.split(':', 1)[-1]), headers))

    for lista in json_data['rows']:
        date.append(lista[0].get('primitiveValue'))
        goal.append(lista[1].get('primitiveValue'))
        assisted_conversions.append(lista[2].get('primitiveValue'))

    d = {headers[0]: date, headers[1]: goal,headers[2]: assisted_conversions}
    df_values = pd.DataFrame(d)
    df_values['profileId'] = VIEW_ID
    df_values['uploadtime'] = now
    df_values['info'] = info_level
    df_values['period'] = period
    return df_values


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