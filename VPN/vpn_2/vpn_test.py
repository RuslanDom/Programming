# l = ['fsdfs', 'sdfsdfsd', 'dfsdfs']
# with open('test.txt', 'w') as f:
#     for i in l:
#         f.write(i + '\n')

import aiohttp
import asyncio
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests


def get_proxy():
    url_with_proxy = 'https://free-proxy-list.net/'
    fake_agent = UserAgent().random
    headers = {
        'User-Agent': fake_agent
    }
    response = requests.get(url_with_proxy, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')
    return soup.textarea.text.split('\n')[3:]


def check_proxy(proxy_list):
    url_for_test = 'http://www.google.com'
    print(f"Найдено {len(proxy_list)}")
    success_proxy = []

    for proxy in proxy_list:
        test_response = requests.get(url_for_test,
                                     proxies={"http": f"http://{proxy}", 'https': f'https://{proxy}'},
                                     timeout=3)
        if test_response.status_code == 200:
            success_proxy.append(proxy)
            print(f'Success proxy: {proxy}')
        if len(success_proxy) > 10:
            break
    with open('proxy.txt', 'w') as f:
        for proxy in success_proxy:
            f.write(proxy + '\n')


async def checking_proxy(proxy_list):
    url_for_test = 'http://www.google.com'
    success_proxy = []

    for proxy in proxy_list:
        proxy_dict = {"http": f"http://{proxy}", "https": f"https://{proxy}"}
        print(len(proxy_list))
        async with aiohttp.ClientSession() as session:
            test_response = await session.get(url=url_for_test)
            if test_response.status == 200:
                success_proxy.append(proxy)
                print(f'Working proxy: {proxy}')
        if len(success_proxy) > 10:
            break

    with open('proxy.txt', 'w') as f:
        for i_str in proxy_list:
            f.write(i_str + "\n")


async def main():
    task = asyncio.create_task(checking_proxy(get_proxy()))
    await task

if __name__ == '__main__':
    # check_proxy(get_proxy())
    asyncio.run(main())





















