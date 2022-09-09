from pprint import pprint
import requests



url = "https://api.rawg.io/api/games/cannon-fodder?key="
# url = "https://api.rawg.io/api/games?key=&search=cannon-fodder&platforms=166"
# url = "https://api.rawg.io/api/games?key="

headers = {

	"X-RapidAPI-Host": "rawg-video-games-database.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

pprint(response.text)
print(type(response))
