def GA_df_etl_method(partial_table=None, selected_columns=None, column_names=None,crawler_name=None):
    final_table = partial_table[selected_columns]
    final_table.columns = column_names
    final_table.to_csv('/home/ds3x/robos-santander/Outputs/'+crawler_name+'.csv', index = False, header=True, sep='|')
    #partial_table.to_csv('/home/ds3x/robos-santander/Outputs/'+crawler_name+'.csv', index = False, header=True, sep='|')
def GA_multipe_df_etl_method(partial_table=None, selected_columns=None, column_names=None,crawler_name=None,funnel_step=None):
    final_table = partial_table[selected_columns]
    final_table.columns = column_names
    final_table.to_csv('/home/ds3x/robos-santander/Outputs/'+crawler_name+'_'+funnel_step+'.csv', index = False, header=True, sep='|')
