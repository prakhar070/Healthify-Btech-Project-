import urllib.request 
import json
import re

def getCoords(address):	
	url = 'https://us1.locationiq.com/v1/search.php?key=4badff9bc7a2c4&q={}&format=json'
	url = url.format(address)
	response = urllib.request.urlopen(url);
	data = json.loads(response.read().decode("utf-8"))
	#formatted_address = re.sub("[ ,/.-_]","+",address)
	#url = url.format(formatted_address)
	#response = urllib.request.urlopen(url);
	#data = json.loads(response.read().decode("utf-8"))
	latlng = {'lat':(data[0]['lat']),'lng':(data[0]['lon'])}
	#print(latlng)
	return latlng