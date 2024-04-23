import time
import selenium
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def FindLocalStores(latitude, longitude, radius):
    url = "http://overpass-api.de/api/interpreter"
    query = f"""
        [out:json];
        (
            node["shop"="supermarket"](around:{radius},{latitude},{longitude});
            node["shop"="grocery"](around:{radius},{latitude},{longitude});
            node["shop"="convenience"](around:{radius},{latitude},{longitude});
            node["shop"="market"](around:{radius},{latitude},{longitude});
            node["shop"="department_store"](around:{radius},{latitude},{longitude});
            node["shop"="corner_shop"](around:{radius},{latitude},{longitude});
            node["shop"="general"](around:{radius},{latitude},{longitude});
            node["shop"="mall"](around:{radius},{latitude},{longitude});
            
            node["shop"="walmart"](around:{radius},{latitude},{longitude});
            node["shop"="store"](around:{radius},{latitude},{longitude});
            node["shop"="store"](around:{radius},{latitude},{longitude});
            node["shop"="store"](around:{radius},{latitude},{longitude});
            node["shop"="store"](around:{radius},{latitude},{longitude});
            node["shop"="chemist"](around:{radius},{latitude},{longitude});
            node["shop"="pharmacy"](around:{radius},{latitude},{longitude});
            
            node["shop"="store"](around:{radius},{latitude},{longitude});
            node["shop"="shop"](around:{radius},{latitude},{longitude});
            node["shop"="outlet"](around:{radius},{latitude},{longitude});
            node["shop"="marketplace"](around:{radius},{latitude},{longitude});
            node["shop"="Supercenter"](around:{radius},{latitude},{longitude});
            
            node["branch"="SuperCenter"](around:{radius},{latitude},{longitude});
            node["brand"="walmart"](around:{radius},{latitude},{longitude});

        );
        out;
    """
    
    response = requests.post(url, data=query)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code)
        return None