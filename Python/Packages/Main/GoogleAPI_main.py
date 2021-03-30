from Packages.APIs import Google_authentication, Account_hierarchy, Get_report_ga, GA_report_to_df, GA_join_df, GA_df_etl, dcm, dbm
from datetime import datetime
import pandas as pd
import time

target = None

#define credenciais de autenticação
token_url = 'https://oauth2.googleapis.com/token'
client_id = '937012240596-vp85uvfttct2ic3b24v5ks7tg8mqg59k.apps.googleusercontent.com'
client_secret = 'vngwDuxcr9_A5uNG4GH_xmJA'
refresh_token = '1//04TCfqkMrxLBgCgYIARAAGAQSNwF-L9IrGw0_re0mndeZ4GvM--jjoN1l37jbhG04YqbRMo8-_jxK5Hgir_p0hA8KOB14jg_BSCk'
headers = {"Content-Type" : "application/x-www-form-urlencoded"}

refresh_token_dcm = '1//04zMKuVEjG98aCgYIARAAGAQSNwF-L9Irw5xK-CS5lZ_xF7TfpETAugWw1xkaNuor7aa9SQGZnEQ7AfAbjwc9XF7da5jg7SHsh14'
refresh_token_dbm = '1//04Duuj2ormuTCCgYIARAAGAQSNwF-L9Ir5yHkHEh207SQxkDKOQbRGEzlDvUCg8W3kreo-llfVel_87wPz6Q1AY1a4GRFxU0piq4'

data = {'client_id': client_id,
        'client_secret': client_secret,
        'refresh_token':refresh_token,
        'grant_type': 'refresh_token',  
        }
now = datetime.now()

def main(api_type=None,crawler_name=None,token_url=token_url, data=data, headers=headers,client_secret=client_secret, VIEW_ID=None
        ,info_level=None, period=None, start_date=None, end_date=None,metrics=None, dimensions=None,selected_columns=[], column_names=[]
        ,refresh_token=refresh_token,report_period=[],report_dimensions=[], report_metrics=[],report_filters_dimensions=[], funnel_step=[]
        ,description=[], profile_id=None, report_id=None,file_name=None, skiped_rows=None,last_rows=None,output_file=None
        ,query_id=None):
  repo_list = []
  try:
    if api_type == 'simple_report':
      #obtem o token de acesso
        try:
          access_token = Google_authentication.Get_access_token(token_url=token_url,data=data,headers=headers)
          #inicia o serviço da API
          analytics = Google_authentication.Create_service_ga(access_token=access_token, client_id=client_id, client_secret=client_secret, refresh_token=refresh_token)
          #cria dataframe com as contas, webproperties e profiles
          hierarchy_table = Account_hierarchy.Get_account_infos(access_token)
          #cria lista de profilels pra gerar os reports
          profile_list = Account_hierarchy.Get_profiles_list(hierarchy_table)
          if VIEW_ID == None:
            repo_list = profile_list
          else:
            repo_list = VIEW_ID
          #cria o dataframe com as infos do report
          report_final_table_ga = []
          for repo in repo_list:
              print(repo)
              report_json = Get_report_ga.get_report(analytics, repo, report_period, report_dimensions, report_metrics)
              report = GA_report_to_df.response2df(report_json,repo, now, info_level, period)
              report_final_table_ga.append(report)
          report_final_table_ga = pd.concat(report_final_table_ga)
          #join das infos da conta com o report
          report_full_ga = GA_join_df.Join_df(hierarchy_table, report_final_table_ga)  
          #seleciona somente as colunas necessárias e renomeia
          GA_df_etl.GA_df_etl_method(partial_table=report_full_ga, selected_columns=selected_columns, column_names=column_names,crawler_name=crawler_name)
        except Exception as e:
          print(e)
          print(repo)
        else:
        #logging.error('Erro nas classes')
          print('Sucesso simple reports')
          
    elif api_type == 'mcf_report':
      #obtem o token de acesso
        try:
          access_token = Google_authentication.Get_access_token(token_url=token_url,data=data,headers=headers)
          #inicia o serviço da AP                                 
        except Exception as e:
          print(e)
          #cria dataframe com as contas, webproperties e profiles
        try:
          hierarchy_table = Account_hierarchy.Get_account_infos(access_token)
        except Exception as e:
          print(e)
          #cria lista de profilels pra gerar os reports
        try:
          profile_list = Account_hierarchy.Get_profiles_list(hierarchy_table)
        except Exception as e:
          print(e)
        try:
          if VIEW_ID == None:
            repo_list = profile_list
          else:
            repo_list = VIEW_ID
          #cria o dataframe com as infos do report
        except Exception as e:
          print('erro ao definir a lista')
          print(e)
        report_final_table_mcf = []
        for repo in repo_list:
          try:
            report_json = Get_report_ga.Multichannel_funnel_reports_method(VIEW_ID=repo,access_token=access_token,metrics=metrics,dimensions=dimensions,start_date=start_date,end_date=end_date)
          except Exception as e:
            print('erro no get do report')
            print(e)
          try:  
            report = GA_report_to_df.Multichannel_funnel_report_to_df(report_json,repo, now, info_level, period)
          except Exception as e:
            print('erro ao transformar em dataframe')
            print(e)
          try:
            report_final_table_mcf.append(report)
          except Exception as e:
            print('erro ao appendar dado')
            print(e)
        report_final_table_mcf = pd.concat(report_final_table_mcf)
        
          #join das infos da conta com o report
        try:
          report_full_mcf = GA_join_df.Join_df(hierarchy_table, report_final_table_mcf)  
          #seleciona somente as colunas necessárias e renomeia
        except Exception as e:
          print(e)
        try:  
          GA_df_etl.GA_df_etl_method(partial_table=report_full_mcf, selected_columns=selected_columns, column_names=column_names,crawler_name=crawler_name)
        except Exception as e:
          print(e)
        else:
        #logging.error('Erro nas classes')
          print('Sucesso simple reports')
    
    elif api_type == 'dcm_report':
      #obtem o token de acesso
        try:
          access_token = Google_authentication.Get_access_token(token_url=token_url,data=data,headers=headers)
          #inicia o serviço da API
          analytics = Google_authentication.Create_service_dcm(access_token=access_token, client_id=client_id, client_secret=client_secret, refresh_token=refresh_token_dcm)
        except Exception as e:
          print(e)
          print('auth')
        try:
          file_id = dcm.get_file_id(analytics=analytics,profile_id=profile_id,report_id=report_id)
          time.sleep(10)
        except Exception as e:
          print(e)
          print('get file id')
        try:
          dcm.download_file(analytics=analytics, file_id=file_id, report_id=report_id,file_name=file_name)
        except Exception as e:
          print(e)
          print('download file')
        try:
          dcm.elt_csv(file_name=file_name,skiped_rows=skiped_rows,last_rows=last_rows,crawler_name=crawler_name)
        except Exception as e:
          print(e)
          print('etl csv')

    elif api_type == 'dbm_report':
      #obtem o token de acesso
        try:
          access_token = Google_authentication.Get_access_token(token_url=token_url,data=data,headers=headers)
          #inicia o serviço da API
          analytics = Google_authentication.Create_service_dbm(access_token=access_token, client_id=client_id, client_secret=client_secret, refresh_token=refresh_token_dbm)
        except Exception as e:
          print(e)
          print('auth')
        try:
          dbm.download_file(analytics=analytics, query_id=query_id,file_name=file_name)
        except Exception as e:
          print(e)
          print('download file')
        try:
          dbm.elt_csv(file_name=file_name,last_rows=last_rows,crawler_name=crawler_name)
        except Exception as e:
          print(e)
          print('etl csv')
        
    elif api_type == 'simple_report':
      #obtem o token de acesso
        try:
          access_token = Google_authentication.Get_access_token(token_url=token_url,data=data,headers=headers)
          #inicia o serviço da API
          analytics = Google_authentication.Create_service_ga(access_token=access_token, client_id=client_id, client_secret=client_secret, refresh_token=refresh_token)
          #cria dataframe com as contas, webproperties e profiles
          hierarchy_table = Account_hierarchy.Get_account_infos(access_token)
          #cria lista de profilels pra gerar os reports
          profile_list = Account_hierarchy.Get_profiles_list(hierarchy_table)
          if VIEW_ID == None:
            repo_list = profile_list
          else:
            repo_list = VIEW_ID
          #cria o dataframe com as infos do report
          report_final_table_ga = []
          for repo in repo_list:
            for metrics, filters,funnel,desc in zip(report_metrics, report_filters_dimensions,funnel_step,description):
              report_json = Get_report_ga.get_report(analytics, repo, report_period, report_dimensions, report_metrics)
              report = GA_report_to_df.response2df(report_json,repo, now, info_level, period)
              report_final_table_ga.append(report)
          report_final_table_ga = pd.concat(report_final_table_ga)
          #join das infos da conta com o report
          report_full_ga = GA_join_df.Join_df(hierarchy_table, report_final_table_ga)  
          #seleciona somente as colunas necessárias e renomeia
          GA_df_etl.GA_df_etl_method(partial_table=report_full_ga, selected_columns=selected_columns, column_names=column_names,crawler_name=crawler_name)
        except Exception as e:
          print(e)
          print(repo)
        else:
        #logging.error('Erro nas classes')
          print('Sucesso simple reports')
        
        
        #try:
        #        for metrics, filters,funnel,desc in zip(report_metrics, report_filters_dimensions,funnel_step,description):
        #                report_json = Get_report_ga.Multiple_reports_method(analytics, VIEW_ID, report_period, report_dimensions, metrics, filters, funnel, desc)
        #                funnel_step = funnel
        #                description = desc
        #                report = GA_report_to_df.Multiple_response2df(report_json,VIEW_ID, now, info_level, period, funnel_step, description)
        #                partial_table = GA_join_df.Join_df(account_infos, wp_infos, profile_infos, report)
        #                GA_df_etl.GA_multipe_df_etl_method(partial_table=partial_table, selected_columns=selected_columns, column_names=column_names,crawler_name=crawler_name,funnel_step=funnel_step)
        
    else:
      print('tipo de report não definido')
  except Exception as e:
    print(e)
  else:
    #logging.error('Erro nas classes')
    print('Sucesso get')