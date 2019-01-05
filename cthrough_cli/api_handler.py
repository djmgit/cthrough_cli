import requests
import json

def api_handler(url, data):
	try:
		response = requests.request("POST", url, json=data)
		if response.status_code != 200:
			return None
		data = response.json()
		if data.get("status") != "OK":
			return None

		return data
	except:
		return None
