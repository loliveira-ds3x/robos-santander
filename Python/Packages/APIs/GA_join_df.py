import pandas as pd
def Join_df(hierarchy_table, report):
    partial_table = pd.merge(report, hierarchy_table, left_on='profileId',right_on='profileId',how='inner',suffixes=('_report','_account'))

    return partial_table