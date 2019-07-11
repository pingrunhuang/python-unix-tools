import requests
from location_generator import generate_random_location_by_polygon
import json
import time
from functools import wraps
import 


def timmer(func):
    @wraps(func)
    def run(*args, **wargs):
        start = time.time()
        result = func(*args, **wargs)
        end = time.time()
        print(end-start)
        return result
    return run


def mapbox_test(points):
    """
    approaches 
    """
    url = "https://api.mapbox.com/directions-matrix/v1/mapbox/driving/{}?approaches={}&access_token=pk.eyJ1IjoiZnJhbmstaHVhbmciLCJhIjoiY2p0cDlsZXlrMDJlazN5cXN6cG85bXNpNyJ9.9wnnEBj8K2MxFmUNOuyPRQ".format(";".join([str(x) for x in points]), ";".join(["curb" for _ in range(len(points))]))
    print(url)
    result = requests.get(url)
    return result



@timmer
def baidu_transit_test(points):
    """
    
    """
    import urllib
    import hashlib

    root = "http://api.map.baidu.com/direction/v2/transit"

    ak = "51882082a72a49dc9b43c7c2d56b0b6f"
    # origin = "40.056878,116.30815"
    origin = "39.989643, 116.481028"
    # destination = "31.222965,121.505821"
    destination = "40.004717, 116.465302"
    sk = "75c62689612e4c5bb8b6b425452b6b93"
    
    # 以get请求为例http://api.map.baidu.com/geocoder/v2/?address=百度大厦&output=json&ak=yourak
    queryStr = '/direction/v2/transit?origin={}&destination={}&ak={}'.format(origin, destination, ak)

    # 对queryStr进行转码，safe内的保留字符不转换
    encodedStr = urllib.parse.quote(queryStr, safe="/:=&?#+!$,;'@()*[]")
    # 在最后直接追加上yoursk
    rawStr = encodedStr + sk

    # md5计算出的sn值7de5a22212ffaa9e326444c75a58f9a0
    # 最终合法请求url是http://api.map.baidu.com/geocoder/v2/?address=百度大厦&output=json&ak=yourak&sn=7de5a22212ffaa9e326444c75a58f9a0
    sn = hashlib.md5(urllib.parse.quote_plus(rawStr).encode("utf-8")).hexdigest()
    print(sn)
    
    url = "{}?origin={}&destination={}&ak={}&sn={}".format(root, origin, destination, ak, sn)
    # response = requests.get(url)
    # print(json.loads(response.content))

@timmer
def gaode_test(points):
    root = "https://restapi.amap.com/v3/direction/driving?"
    origin = "116.481028,39.989643"
    destination = "116.465302,40.004717"
    waypoints = ";".join([
        '121.423717,30.932818', 
        '121.127535,30.618113', 
        '121.224746,30.752282', 
        '121.394362,30.674204', 
        '121.014174,30.95307', 
        '121.216384,30.582117', 
        '121.001053,30.61886', 
        '121.36077,30.777306', 
        '121.472635,30.885619', 
        '121.015295,30.549286', 
        '121.270706,30.987277', 
        '121.190602,30.530425', 
        '121.211058,30.8917', 
        '121.110846,30.98548', 
        '121.247906,30.781056', 
        '121.115433,30.883458'])
    key = "a7ee2da7b5ec9db9eabd868fa9248340"
    strategy = ""
    

    url = "{}origin={}&destination={}&extensions=all&output=json&key={}&waypoints={}"\
        .format(root, origin, destination, key, waypoints)
    response = requests.get(url)
    response.encoding = "utf-8"
    result = json.loads(response.content)
    with open("gaode.json", 'w') as f:
        json.dump(result, f, ensure_ascii=False)
    return result
    




if __name__ == "__main__":
    result = generate_random_location_by_polygon(121, 31, 121.5, 30.5, size=5)
    # print(mapbox_test(result).content)
    gaode_test(result)
    # baidu_transit_test(result)




