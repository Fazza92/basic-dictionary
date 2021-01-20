import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
  if elevation < 1000:
    return 'green'
  elif 3000 <= elevation < 3000:
    return 'red'
  else:
    return 'orange' 

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev):
  fg.add_child(folium.CircleMarker(location=[lt, ln], popup=str(el), icon=folium.Icon(color=color_producer(el))))
map.add_child(fg)

map.save("Map1.html")
