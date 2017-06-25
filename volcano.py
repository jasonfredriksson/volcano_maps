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

fg=folium.FeatureGroup(name='Volcano Locations')

for lat,lon,name,elev in zip(df['y'],df['x'],df['NAME'],df['ELEV']):
	fg.add_child(folium.Marker([lat, lon], popup=name+' - '+str(elev)+'mts.',icon=folium.Icon(color=color(elev),icon='info-sign')))

map.add_child(fg)

map.add_child(folium.GeoJson(data=open('world_pop.geojson'),
name='World Population',
style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005']<10000000  else 'yellow' if x['properties']['POP2005']<30000000 else 'red'}))

volc_type=folium.FeatureGroup(name='Volcano Types')

for lat,lon,name,vtype in zip(df['y'],df['x'],df['NAME'],df['TYPE']):
	volc_type.add_child(folium.Marker([lat, lon], popup=name+' - '+vtype,icon=folium.Icon(color=color_type(vtype),icon='info-sign')))

map.add_child(volc_type)

map.add_child(folium.LayerControl())


map.save('mapa.html')
