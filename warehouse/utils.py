import jsonfrom pprint import pprintimport randomimport requestsimport osos.environ['DJANGO_SETTINGS_MODULE'] = 'main.settings'import djangodjango.setup()from warehouse.models import Games# url = "https://api.rawg.io/api/games/cannon-fodder?key="# # url = "https://api.rawg.io/api/games?key=&search=cannon-fodder&platforms=166"# # url = "https://api.rawg.io/api/games?key="## headers = {## 	"X-RapidAPI-Host": "rawg-video-games-database.p.rapidapi.com"# }## response = requests.request("GET", url, headers=headers)## pprint(response.text)# print(type(response))def add_new_game(title):	game_name = converting_title(title)	api_key = 'b55a581e99e8409aba9f9aee43603202'	response = requests.get(f"https://api.rawg.io/api/games/{game_name}?key={api_key}&platforms=10&page=1")	if response.status_code != requests.codes.ok:		print('Error')	else:		# print(json.dumps(response.json(), indent=4))		json_string = json.dumps(response.json(), indent=4)		data = json.loads(json_string)		pprint(data)		pk_games = data['id']		description = data['description']		description = description.replace('<br/>', '\n').replace('<p>', '').replace('</p>', '\n').replace('<br />', '\n')		name = data['name']		slug = data['slug']		developers = data['developers'][0]['name']		platform = [component['platform']['name'] for component in data['platforms']]		released = data['released']		# print(description)		# print(name)		# print(slug)		# print(developers)		# print(platform)		# print(released)		response_image = requests.get(f"https://api.rawg.io/api/games/{pk_games}/screenshots?key={api_key}&platforms=10")		if response_image.status_code != requests.codes.ok:			print('Error')		else:			json_string = json.dumps(response_image.json(), indent=4)			data = json.loads(json_string)			# image = data['results'][0]['image']			image = data['results'][random.randrange(0, len(data['results']))]['image']			print(image)			add_games = Games()			add_games.name = name			add_games.released = released			add_games.slug = slug			add_games.image = image			add_games.description = description			add_games.platform = platform			add_games.developers = developers			add_games.save()def converting_title(title):	new_title = title.lower().replace(' ', '-')	return new_title