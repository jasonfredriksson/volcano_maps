import folium
import pandas

df=pandas.read_csv("Volcanoes_USA.txt")


map = folium.Map(location=[df['LAT'].mean(),df['LON'].mean()],zoom_start=6,tiles='Stamen Terrain')


def color(elev):
	if elev in range (0,1000):
		col='green'
	elif elev in range (1001,3000):
		col='orange'
	else:
		col='red'
	return col	


for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
	folium.Marker([lat, lon], popup=name,icon=folium.Icon(color=color(elev),icon='info-sign')).add_to(map)


map.save('mapa.html')
