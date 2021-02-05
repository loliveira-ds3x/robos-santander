def Join_df(account_infos, wp_infos, profile_infos, report):
    partial_table = account_infos.join(wp_infos, lsuffix='_account', rsuffix='_wb')
    partial_table = partial_table.join(profile_infos, lsuffix='_wb', rsuffix='_profile')
    partial_table = partial_table.join(report,  lsuffix='_profile', rsuffix='_report')
    return partial_table