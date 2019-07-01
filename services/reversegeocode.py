import urllib.request 
import json

def getAddress(lat, lng):
	url = 'https://us1.locationiq.com/v1/reverse.php?key=4badff9bc7a2c4&lat={}&lon={}&format=json'
	url = url.format(lat,lng)
	response = urllib.request.urlopen(url);
	data = json.loads(response.read().decode("utf-8"))
	#address = data['address']['neighbourhood'] + data['address']['city']
	return data['display_name']




