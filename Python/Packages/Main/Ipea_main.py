from Packages.Get_files import Get_from_screen
import pandas as pd

def main (serie_id, crawler_name):
    all_data = []
    for id in serie_id:
        df_pivot = Get_from_screen.Get_from_screen_method(id)
        all_data.append(df_pivot)
    all_data = pd.concat(all_data)
    all_data.to_csv('/home/ds3x/robos-santander/Outputs/'+crawler_name+'.csv', index = False, header=True, sep='|')