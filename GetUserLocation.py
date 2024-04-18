import geocoder

myCoords = geocoder.ip('me')
print("Lat:\t\t", myCoords.latlng[0])
print("Long:\t\t", myCoords.latlng[1])
print("City:\t\t", myCoords.city)
print("Province:\t", myCoords.state)
print("Country:\t", myCoords.country)