import geocoder

g = geocoder.arcgis("Adelaide, Australia")
print(g.latlng)


def getLatLong(location):
    return geocoder.arcgis(location).latlng
