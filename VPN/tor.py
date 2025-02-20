import requests

proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://172.0.0.1:9050'
}

url = 'http://flibustaongezhld6dibs2dps6vm4nvqg2kp7vgowbu76tzopgnhazqd.onion/'

r = requests.get(url, proxies=proxies, verify=False)  # using TOR network
print(r.text)

