import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# %%

############# GRAFICA INTERNACION

import pandas as pd
import plotly.express as px

cds = pd.read_csv('csv\cds.csv', encoding='ISO-8859-1')
medicos = pd.read_csv('csv\medicos.csv',encoding='ISO-8859-1')
mortalidad = pd.read_csv('csv\mortalidad.csv', encoding='ISO-8859-1')
fig = px.scatter_mapbox(cds, lon=cds["lon"], lat=cds["lat"], zoom=6, hover_name=cds["localidad"], color=cds["internacion"])
fig.update_layout(mapbox_style="open-street-map")
fig.show()



# %%

######GRAFICA PEDIATRAS POR PROVINCIA

import pandas as pd
import plotly.express as px
import json
import numpy as np


with open('geo\provincias2.json') as response:
    mapa = json.loads(response.read())
    
medicos = pd.read_csv('csv\medicos2.csv', encoding='utf-8')
lat=[]
lon=[]
id=[]



for k, features in enumerate(mapa["provincias"]):    
    lat.append(mapa["provincias"][k]["centroide"]["lat"])
    lon.append(mapa["provincias"][k]["centroide"]["lon"])
    id.append(mapa["provincias"][k]["id"])
    
### esto es para sacar las coordenadas del json y ponerlas en el df
### no me coordinan porque los nombres están en cualquiera sino se podría hacer macheando strings(ver bases de datos)
#### así como esta sirve para graficar la mortalidad tb

medicos["lat"]=lat
medicos["lon"]=lon
medicos["id"]=id

#### usando el mapa en json saque los centros e hice los puntos porquie el mapa por provincias no está bien hecho y se rompe el gráfico
### falta q los codigos del json coordinen con los nombres de las provincias. habría q ver si es el mismo codigo de la mortalidad
#### podría ser pediatroas/ habitantes niños para q quede un gráfico más amigable.


# prom=[]
# for k in medicos["Medicos"]:
#     prom.append((k*100/sum(medicos["Medicos"])))
# medicos["prom"]=prom
# print(prom)

fig=px.scatter_mapbox(medicos, lon=medicos["lon"], lat=medicos["lat"], zoom=4, hover_name=medicos["Provincia"], size=medicos["Medicos"],color=medicos["Medicos"], color_continuous_scale=px.colors.cyclical.IceFire)

fig.update_layout(mapbox_style="open-street-map")

fig.show()


# %%
import pandas as pd
import plotly.express as px

cds = pd.read_csv('csv\cds.csv', encoding='ISO-8859-1')
medicos = pd.read_csv('csv\medicos.csv',encoding='ISO-8859-1')
mortalidad = pd.read_csv('csv\mortalidad.csv', encoding='ISO-8859-1')

fig = px.scatter_mapbox(cds, lon=cds["lon"], lat=cds["lat"], zoom=6, hover_name=cds["localidad"], color=cds["internacion"])
fig.update_layout(mapbox_style="open-street-map")
fig.show()

#%%

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

mortalidad = pd.read_csv('csv\mortalidad.csv', encoding='ISO-8859-1')
medicos = pd.read_csv('csv\medicos2.csv', encoding='utf-8')




for k in mortalidad["GRUPEDAD"]:
    if k[:2] == "02" or k[:2] == "01":
        print(k)
    


# fig = go.Figure()

# fig.add_trace(go.Bar(
#     x=medicos["Provincia"],
#     y=medicos["Medicos"],
#     name='Pediatras',
#     marker_color='indianred'
# ))

# fig.add_trace(go.Bar(
#     x=medicos["Provincia"],
#     y=medicos["Medicos"],
#     name='Mortalidad Infantil',
#     marker_color='lightsalmon'
# ))

# # Here we modify the tickangle of the xaxis, resulting in rotated labels.
# fig.update_layout(barmode='group', xaxis_tickangle=-45)
# fig.show()


# %%
import pandas as pd
import plotly.express as px

cds = pd.read_csv('/content/drive/MyDrive/tpprogramacion2/cds.csv', encoding='ISO-8859-1')
medicos = pd.read_csv('/content/drive/MyDrive/tpprogramacion2/medicos.csv',encoding='ISO-8859-1')
timelinemortalidad = pd.read_csv('/content/drive/MyDrive/tpprogramacion2/mortalidad.csv', encoding='ISO-8859-1')

#%%
timelinemortalidad['anio_def'] =timelinemortalidad.anio_def.astype('string')

grafico={}
for i in timelinemortalidad['anio_def'].unique():
  grafico['grupo_etario']=[]
  grafico[i]=[]
  
  
  for x in timelinemortalidad['grupo_etario'].unique():
    if x == '08.sin especificar':
      pass
    else:
      grafico['grupo_etario'].append(x)
      df2 = timelinemortalidad[timelinemortalidad['anio_def'].str.contains(f'{i}') & timelinemortalidad['grupo_etario'].str.contains(f'{x}')]
      valor=df2['grupo_etario'].count()
      grafico[i].append(valor)

grafico=pd.DataFrame(grafico)


#%%
import plotly.express as px

fig = px.scatter(grafico, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
           size="pop", color="continent", hover_name="country", facet_col="continent",
           log_x=True, size_max=45, range_x=[100,100000], range_y=[25,90])
fig.show()