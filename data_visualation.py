import numpy as np
import pandas as pd
import folium as fo
data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/Volcano.csv")
print(data.head())

lat = list(data["Latitude"])
lon = list(data["Longitude"])
name = list(data["Name"])

volcano = fo.FeatureGroup(name="Volcano")
for a, b, c in zip(lat, lon, name):
  volcano.add_child(fo.Marker(location=[a, b], popup=c, icon=fo.Icon(color='blue')))
  
fo.Map().add_child(volcano)                                                                               
