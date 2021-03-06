#reduced version without the GeoJSON file. This program creates two Feature Groups or tabs, adding markers on each volcano
#location. One of the FGs adds the marker, colored according to the volcano height and the other one, colored depending on 
#the volcano's type.


import folium
import pandas

df=pandas.read_csv("Volcanoes_World.csv")
volctype = df.loc[:,"TYPE"]
n=0

map=folium.Map(location=[df['y'].mean(),df['x'].mean()],zoom_start=6,tiles='Stamen Terrain')


def color(elev):
    if elev in range (0,2000):
        col='green'
    elif elev in range (2001,5000):
        col='orange'
    else:
        col='red'
    return col

def color_type(t):
    if t == 'Potentially active':
        col='orange'
    elif t == 'Solfatara stage':
        col='green'
    else:
        col='red'
    return col

fg=folium.FeatureGroup(name='Volcano per height')

for lat,lon,name,elev in zip(df['y'],df['x'],df['NAME'],df['ELEV']):
    fg.add_child(folium.Marker([lat, lon], popup=name+' - '+str(elev)+'mts.',icon=folium.Icon(color=color(elev),icon='info-sign')))

map.add_child(fg)

volc_type=folium.FeatureGroup(name='Volcano Types')

for lat,lon,name,vtype in zip(df['y'],df['x'],df['NAME'],df['TYPE']):
    volc_type.add_child(folium.Marker([lat, lon], popup=name+' - '+vtype,icon=folium.Icon(color=color_type(vtype),icon='info-sign')))

map.add_child(volc_type)

map.add_child(folium.LayerControl())


map.save('mapa2.html')
