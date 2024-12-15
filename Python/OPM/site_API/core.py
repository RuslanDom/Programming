import requests
from OPM.settings import SiteSettings
from fake_useragent import UserAgent

user = UserAgent().random
headers = {
    'user-agent': user,
    'x-rapidapi-host': SiteSettings.HOST_API,
    'x-rapidapi-key': SiteSettings.API_KEY
}

querystring = {"page": "1", "catId": "101001384668", "locale": "ru_RU", "region": "RU", "currency": "RUB"}
url = 'https://aliexpress-datahub.p.rapidapi.com/item_search_promotion_deals'

response = requests.get(url, headers=headers, params=querystring)
print(response.status_code)
print(response.json())





