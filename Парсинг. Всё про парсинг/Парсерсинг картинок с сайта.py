import requests
from bs4 import BeautifulSoup
import fake_useragent
import os

user = fake_useragent.UserAgent().random
header_ = {
    'user-agent': user
}
path_dict = os.path.abspath(os.path.join('../Python',
                                         '..',
                                         '..',
                                         '..', 'Desktop\\image_data'))
# print(path_dict)

url = 'https://wallscloud.net/ru/wallpapers/latest?page=2'


def save_image(path, link, num):
    with open(f'{path}/{num}.jpg', 'wb') as file:
        file.write(link)
    print(f'Изображение {num} успешно скачено!')


def download(link, header, path):
    image_number = 26
    for storage in range(5, 7):
        response = requests.get(f'{link}', headers=header).text
        soup = BeautifulSoup(response, 'lxml')

        block = soup.find('div', class_='items').find('div', class_='grid-row walls_data')

        image_block = block.findAll('figure')
        for image in image_block:
            image_link = image.find('a').get('href')
            download_storage = requests.get(f'{image_link}', headers=header).text
            download_soup = BeautifulSoup(download_storage, 'lxml')
            container = download_soup.find('div', class_='container-right').find('div', class_='dw-btns')
            link_download = container.find('button', class_='btn waves btn-block search_available_res dl_original starting_download').get('href')
            # print(link_download)
            image_download = requests.get(link_download, headers=header).content
            save_image(path, image_download, image_number)
            image_number += 1


download(url, header_, path_dict)
