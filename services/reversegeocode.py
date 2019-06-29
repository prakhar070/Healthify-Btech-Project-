import urllib.request 
import json

def getAddress(lat, lng):
	url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}&key=AIzaSyBHhLM77Z5mrxgMNJ-Dp_nFUTWJ9YcRKSE'
	url = url.format(lat,lng)
	response = urllib.request.urlopen(url);
	data = json.loads(response.read().decode("utf-8"))
	return data['results'][0]['formatted_address']

