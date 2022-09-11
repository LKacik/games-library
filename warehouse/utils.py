import json
from pprint import pprint
import requests



# url = "https://api.rawg.io/api/games/cannon-fodder?key="
# # url = "https://api.rawg.io/api/games?key=&search=cannon-fodder&platforms=166"
# # url = "https://api.rawg.io/api/games?key="
#
# headers = {
#
# 	"X-RapidAPI-Host": "rawg-video-games-database.p.rapidapi.com"
# }
#
# response = requests.request("GET", url, headers=headers)
#
# pprint(response.text)
# print(type(response))

response = requests.get("https://api.rawg.io/api/games/cannon-fodder?key=b55a581e99e8409aba9f9aee43603202&platforms=10&page=1")

if response.status_code != requests.codes.ok:
	print('Error')
else:
	# print(json.dumps(response.json(), indent=4))
	json_string = json.dumps(response.json(), indent=4)
	data = json.loads(json_string)
	pprint(data)

	description = data['description']
	name = data['name']
	slug = data['slug']
	developers = data['developers'][0]['name']
	platform = [component['platform']['name'] for component in data['platforms']]
	released = data['released']

	print(description)
	print(name)
	print(slug)
	print(developers)
	print(platform)
	print(released)

# for dat in data['platforms']:
# 	print(dat['platform']['name'])
