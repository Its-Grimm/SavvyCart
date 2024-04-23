import geocoder

def GetUserLocationCity():
    myCoords = geocoder.ip('me')
    return myCoords.city, myCoords.state, myCoords.country

def GetUserLocationLatLong():
    myCoords = geocoder.ip('me')
    return myCoords.latlng