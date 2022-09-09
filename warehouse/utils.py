from pprint import pprint
import requests



url = "https://api.rawg.io/api/games/cannon-fodder?key=b55a581e99e8409aba9f9aee43603202"
# url = "https://api.rawg.io/api/games?key=b55a581e99e8409aba9f9aee43603202&search=cannon-fodder&platforms=166"
# url = "https://api.rawg.io/api/games?key=b55a581e99e8409aba9f9aee43603202"

headers = {
	"X-RapidAPI-Key": "17998f3b96msh01d58ff55e3cd95p12d75ejsnf13360bc660d",
	"X-RapidAPI-Host": "rawg-video-games-database.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

pprint(response.text)
print(type(response))
