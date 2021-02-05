from Packages.APIs import Google_authentication, Account_hierarchy, Get_report_ga, GA_report_to_df, GA_join_df, GA_df_etl
from datetime import datetime

#define credenciais de autenticação
token_url = 'https://oauth2.googleapis.com/token'
client_id = '959085883070-61rrk0v3ogpdf7d38o5i27ocj4sqles4.apps.googleusercontent.com'
client_secret = 'RXYi722AwIrVH_HO-x0V8Kkc'
refresh_token = '1//0hqj21TVBTcdWCgYIARAAGBESNwF-L9Irt0d3ExRAh5uYZZlt1GVK4B1QIPzXkNmODPjUTGZgZG4Vj07r2Td0YljtU34fcCZe1Vs'
headers = {"Content-Type" : "application/x-www-form-urlencoded"}

data = {'client_id': client_id,
        'client_secret': client_secret,
        'refresh_token':refresh_token,
        'grant_type': 'refresh_token',
        }
now = datetime.now()

def main(api_type=None,crawler_name=None,token_url=token_url, data=data, headers=headers,client_secret=client_secret, VIEW_ID=None, info_level=None, period=None, selected_columns=[], column_names=[], refresh_token=refresh_token,report_period=[],report_dimensions=[], report_metrics=[],report_filters_dimensions=[], funnel_step=[], description=[]):
  try:
    if api_type == 'simple_report':
      #obtem o token de acesso
        access_token = Google_authentication.Get_access_token (token_url=token_url,data=data,headers=headers)
        #inicia o serviço da API
        analytics = Google_authentication.Create_service(access_token=access_token, client_id=client_id, client_secret=client_secret, refresh_token=refresh_token)

        #cria dataframes com infos sobre conta, webproperties e perfils(views)
        account_infos = Account_hierarchy.Get_account_infos(access_token)
        wp_infos = Account_hierarchy.Get_wp_infos(access_token)
        profile_infos = Account_hierarchy.Get_profile_infos(access_token)

        #cria o dataframe com as infos do report
        report_json = Get_report_ga.get_report(analytics, VIEW_ID, report_period, report_dimensions, report_metrics)
        report = GA_report_to_df.response2df(report_json,VIEW_ID, now, info_level, period)
        #junta todos os dataframes em uma única tabela
        partial_table = GA_join_df.Join_df(account_infos, wp_infos, profile_infos, report)
        #seleciona somente as colunas necessárias e renomeia
        GA_df_etl.GA_df_etl_method(partial_table=partial_table, selected_columns=selected_columns, column_names=column_names,crawler_name=crawler_name)

    elif api_type == 'multiple_simple_reports':
        access_token = Google_authentication.Get_access_token (token_url=token_url,data=data,headers=headers)
        #inicia o serviço da API
        analytics = Google_authentication.Create_service(access_token=access_token, client_id=client_id, client_secret=client_secret, refresh_token=refresh_token)#

        #cria dataframes com infos sobre conta, webproperties e perfils(views)
        account_infos = Account_hierarchy.Get_account_infos(access_token)
        wp_infos = Account_hierarchy.Get_wp_infos(access_token)
        profile_infos = Account_hierarchy.Get_profile_infos(access_token)

        #cria o dataframe com as infos do report
        try:
                for metrics, filters,funnel,desc in zip(report_metrics, report_filters_dimensions,funnel_step,description):
                        report_json = Get_report_ga.Multiple_reports_method(analytics, VIEW_ID, report_period, report_dimensions, metrics, filters, funnel, desc)
                        funnel_step = funnel
                        description = desc
                        report = GA_report_to_df.Multiple_response2df(report_json,VIEW_ID, now, info_level, period, funnel_step, description)
                        partial_table = GA_join_df.Join_df(account_infos, wp_infos, profile_infos, report)
                        GA_df_etl.GA_multipe_df_etl_method(partial_table=partial_table, selected_columns=selected_columns, column_names=column_names,crawler_name=crawler_name,funnel_step=funnel_step)
        except Exception as e:
                print(e)
        else:
    #logging.error('Erro nas classes')
                print('Sucesso multiple reports')
  except Exception as e:
    print(e)
  else:
    #logging.error('Erro nas classes')
    print('Sucesso get')