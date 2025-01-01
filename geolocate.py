import geocoder

g = geocoder.arcgis("Darwin, Australia")
print(g.latlng)


"""
https://api.open-meteo.com/v1/forecast?latitude=12.45&longitude=131.5&daily=temperature_2m&hourly=precipitation&start_date=2024-01-01"""
