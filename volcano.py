import folium
import pandas

df=pandas.read_csv("Volcanoes_World.csv")


map = folium.Map(location=[df['y'].mean(),df['x'].mean()],zoom_start=6,tiles='Stamen Terrain')


def color(elev):
	if elev in range (0,2000):
		col='green'
	elif elev in range (2001,5000):
		col='orange'
	else:
		col='red'
	return col	


fg=folium.FeatureGroup(name='Volcano Locations')

for lat,lon,name,elev in zip(df['y'],df['x'],df['NAME'],df['ELEV']):
	fg.add_child(folium.Marker([lat, lon], popup=name,icon=folium.Icon(color=color(elev),icon='info-sign')))

map.add_child(fg)

map.add_child(folium.GeoJson(data=open('world_pop.geojson'),
name='World Population',
style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005']<10000000  else 'yellow' if x['properties']['POP2005']<30000000 else 'red'}))


map.add_child(folium.LayerControl())


map.save('mapa.html')
