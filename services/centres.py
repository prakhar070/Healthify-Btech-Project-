import urllib.request 
import json
from . import reversegeocode

def getNearbyHospitals(latlng):
	print("inside here lat is {} and long is {}".format(latlng['lat'],latlng['lng']))
	url = 'https://us1.locationiq.com/v1/nearby.php?key=4badff9bc7a2c4&lat={}&lon={}&tag=hospital&radius=15000&format=json'
	url = url.format(latlng['lat'],latlng['lng'])
	response = urllib.request.urlopen(url);
	data = json.loads(response.read().decode("utf-8"))
	results = []
	for i in range(len(data)):
		if 'name' in data[i]:
			add = reversegeocode.getAddress(data[i]['lat'],data[i]['lon'])
			add = add[add.find(',')+1:]
			res = {'name':data[i]['name'],'address':add,'dis':data[i]['distance']}
			results.append(res)
	return results






