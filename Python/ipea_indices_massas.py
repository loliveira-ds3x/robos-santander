from Packages.Main import Ipea_main
from Packages.Get_files import Get_from_screen

crawler_name = 'ipea_indices_massas'
text = 'massa+de+rend.'

serie_id = Get_from_screen.Get_id_list(text)
Ipea_main.main(serie_id, crawler_name)