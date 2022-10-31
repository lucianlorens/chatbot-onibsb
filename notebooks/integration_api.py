import urllib.request, json 
import pandas as pd
import folium
from time import sleep

with urllib.request.urlopen("http://00224.transdatasmart.com.br:22401/ITS-infoexport/api/Data/VeiculosGTFS") as url:
    data = json.loads(url.read().decode())

df = pd.DataFrame.from_records( data['Dados'], columns=data['Campos'])

df.head()