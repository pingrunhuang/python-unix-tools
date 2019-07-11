
"""
longitude = 121.618886
latitude =  31.215684
"""
import numpy as np
import random 

SEED = 1
FLOAT_SIZE = 6

class Location(object):
    def __init__(self, long, lat):
        self.long = long
        self.lat = lat
    def __eq__(self, other):
        return self.lat == other.lat and self.long == other.long

    def __hash__(self):
        return (self.long, self.lat)

    def __repr__(self):
        return str("'" + str(self.long)+"," + str(self.lat) + "'") 
    
    def __str__(self):
        return str(str(self.long)+","+str(self.lat))

def generate_random_location_by_polygon(
    upleft_long, 
    upleft_lat, 
    downright_long, 
    downright_lat,
    size = 1000):
    random.seed(SEED)
    result = []
    i = 0
    upleft_lat = round(upleft_lat, FLOAT_SIZE)
    upleft_long = round(upleft_long, FLOAT_SIZE)
    downright_lat = round(downright_lat, FLOAT_SIZE)

    while i < size:
        random_lat = round(upleft_lat - random.random()*abs(upleft_lat-downright_lat), FLOAT_SIZE)
        random_long = round(upleft_long + random.random()*abs(upleft_long-downright_long), FLOAT_SIZE)
        location = Location(random_long, random_lat)
        if location not in result:
            result.append(location)
            i+=1
    return result




if __name__ == "__main__":
    # maximum 25 pointg
    mapbox="curl \"https://api.mapbox.com/directions-matrix/v1/mapbox/driving/{}?approaches={}&access_token=pk.eyJ1IjoiZnJhbmstaHVhbmciLCJhIjoiY2p0cDlsZXlrMDJlazN5cXN6cG85bXNpNyJ9.9wnnEBj8K2MxFmUNOuyPRQ\""
    result = generate_random_location_by_polygon(121, 31, 121.5, 30.5, size=100)
    print(result)
    str_result = []
    for x in result:
        str_result.append(str(x))
    print(mapbox.format(";".join(str_result), ";".join(["curb" for _ in range(len(str_result))])))