import folium
import pandas

df=pandas.read_csv("Volcanoes_USA.txt")

map = folium.Map(location=[45.372, -121.697],tiles='Stamen Terrain')

for lat,lon,name in zip(df['LAT'],df['LON'],df['NAME']):
	folium.Marker([lat, lon], popup=name,icon=folium.Icon(color='red',icon='info-sign')).add_to(map)


map.save('mapa.html')