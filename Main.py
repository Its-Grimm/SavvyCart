import WebScraper
import GetUserLocation
import FindLocalStores

userLat, userLng = GetUserLocation.GetUserLocationLatLong()
print("Lat:", userLat)
print("Lng:", userLng)
print()

# Radius is in meters
result = FindLocalStores.FindLocalStores(userLat, userLng, 50_000)
storeList = []
if result:
    print("Grocery stores found:")
    for store in result.get('elements', []):
        storeName = store.get('tags', {}).get('name', '')
        if storeName not in storeList:
            storeList.append(storeName)
        # print(store['tags']['name'])
else:
    print("Failed to get data from Overpass API")
    
for store in storeList:
    print(store)