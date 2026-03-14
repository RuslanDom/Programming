import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def get_proxyies():
    url = 'https://free-proxy-list.net/'
    user_agent = {'User-Agent': UserAgent().random}
    response = requests.get(url=url, headers=user_agent)
    soup = BeautifulSoup(response.content, 'lxml')
    return soup.textarea.text.split("\n")


def test_proxyies(proxyies: list):
    print(f"Найдено {len(proxyies)} на проверку")
    test_url = 'http://ip-api.com/json/google.ru?lang=ru'
    successfully_proxies = []
    for proxy in proxyies:
        try:
            req = requests.get(url=test_url, proxies={'http':f'http://{proxy}', 'https': f'https://{proxy}'}, timeout=3.5)
            if req.status_code == 200:
                print(f"{proxy} - рабочий прокси")
                successfully_proxies.append(proxy)
                if len(successfully_proxies) % 10 == 0:
                    user_choise = input("Продолжить: ")
                    if user_choise == 'n':
                        break
            else:
                print(f"{proxy} - не рабочий прокси")

        except:
            print(f"{proxy} - не рабочий прокси")
    with open('Proxyes.txt', 'w') as file:
        for i_proxy in successfully_proxies:
            file.write(i_proxy + '\n')


if __name__ == '__main__':
    test_proxyies(get_proxyies())
    # user_agent = {'User-Agent': UserAgent().random}
    # print(user_agent)