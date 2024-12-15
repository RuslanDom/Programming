import asyncio
import sqlite3
import json
from sys import stdout
import os
import requests
from loguru import logger
from bs4 import BeautifulSoup
from utils.converter import converter_webp_in_jpg

logger.add(sink=stdout, format='{time} {level} {message}', level='DEBUG')
User_Agent_Chrome = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
User_Agent_Firefox = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
    'User-Agent': User_Agent_Firefox
}


path = os.path.join(r'..\images')
path_data = os.path.join(r'..\database\content_data.db')


def create_content_data(user_country: str):
    user_country = str(user_country.replace('-', '_'))
    with sqlite3.connect(path_data) as conn:
        cur = conn.cursor()
        try:
            print('СОЗДАЮ БД')
            cur.execute(
                f"CREATE TABLE IF NOT EXISTS {user_country} (name TEXT, link TEXT, price TEXT, location TEXT, photo BLOB)"
            )
            conn.commit()
            print("УСПЕХ")
        except sqlite3.Error as error:
            print("Ошибка при создании базы данных", error)


def select_all_name(user_country: str):
    user_country = str(user_country.replace('-', '_'))
    with sqlite3.connect(path_data) as conn:
        cur = conn.cursor()
        cur.execute(f'SELECT name FROM {user_country}')
        all_name = cur.fetchall()
        return str(all_name)


# Запись данных в БД
def insert_data(name: str, value, user_country: str):
    user_country = str(user_country.replace('-', '_'))
    with sqlite3.connect(path_data) as conn:
        cur = conn.cursor()
        link = value['link']
        price = value['price']
        location = value['location']
        table = select_all_name(user_country)
        try:
            if name not in table:
                sql = f"""
                    INSERT INTO {user_country} (name, link, price, location) VALUES(?, ?, ?, ?)
                      """
                cur.execute(sql, (name, link, price, json.dumps(location)))
                conn.commit()

            else:
                print('Такое объявление уже есть')
        except sqlite3.Error as error:
            print("Ошибка при заполнении базы данных", error)


# Сохранение изображения
def save_image(key, link, number, country):
    """
    Функция, которая скачивает изображение в формате webp, затем конвертирует его в jpg и записывает в БД
    :param key: ключ-название объявления
    :param link: файл изображения content с сайта
    :param number: номер страницы
    :return: None
    """
    with open(fr"{path}\{number}.webp", 'wb') as img:
        img.write(link)
    converter_webp_in_jpg(filename=str(number) + '.webp', path=path + r"\\")

    with sqlite3.connect(path_data) as conn:
        cur = conn.cursor()
        try:
            sql = f"""
                    UPDATE {country} SET photo = ? WHERE name = ?
                  """
            with open(fr"{path}\{number}.jpg", 'rb') as file:
                img_file = file.read()
                cur.execute(sql, (img_file, key))
                conn.commit()
        except sqlite3.Error as error:
            print('Ошибка при сохранении изображения', error)
        finally:
            os.remove(fr"{path}\{number}.jpg")


# Получение изображений
def get_image(key, n, country):
    """
    Функция для получения изображений из БД
    :param key: ключ-название объявления
    :param n: страница сайта которую получаем
    :return: None
    """
    with sqlite3.connect(path_data) as conn:
        cur = conn.cursor()
        sql = f"""
          SELECT photo FROM {country} WHERE name = ?  
        """
        photos = cur.execute(sql, (key,))

        for photo in photos:
            with open(fr"{path}\{str(n)}.jpg", 'wb') as file:
                file.write(photo[0])


def get_site(user_country: str, page: str):
    s = requests.Session()
    url = f'https://realting.com/en/{user_country}/property?page={page}'

    response = s.get(url=url, headers=headers)

    if response.status_code == 200:
        logger.debug(f"Status code: {response.status_code}")
        soup = BeautifulSoup(response.text, 'lxml')

        block_property = soup.find('div', class_='objects-list')
        blocks = block_property.find_all('div', class_='col-sm-6 col-md-4 col-lg-6 col-xl-4')
        info_about_objects = {}
        number = 0
        # logger.debug(blocks)
        for block in blocks:
            result = {}
            result_location = {}

            link_obj = block.find('a').get('href')
            logger.debug(link_obj)
            response_obj = s.get(link_obj)
            soup_obj = BeautifulSoup(response_obj.text, 'lxml')
            obj_page = soup_obj.find('div', class_='container')

            # Получение названия объявления
            title = obj_page.find('div', class_='col-md').find('h1')
            result_title = str(title.text.strip().replace(' ', '_'))
            logger.debug(result_title)
            # Ссылки на объявление
            result['link'] = str(link_obj)

            # Получение цены в $
            price = obj_page.find('div', class_='col col-md-auto').find('div', class_='price-item').get(
                "data-price-usd")
            logger.debug(price)
            # Получение локации
            location = obj_page.find('div', class_='tags-block-content pb-0').find_all('div', class_='lh-small')

            for i_loc in location:
                place = i_loc.find_all('div')
                count = 0
                key1 = ''
                for i_place in place:
                    count += 1
                    if count % 2 != 0:
                        result_location.setdefault(i_place.text)
                        key1 = i_place.text
                    else:
                        result_location[key1] = i_place.text

            result['price'] = str(price)
            result['location'] = result_location
            logger.debug(result_location)

            if result_title not in info_about_objects.keys():
                info_about_objects[result_title] = result
            else:
                info_about_objects[result_title + '*'] = result

            # Создание папки для изображений и скачивание их в .webp
            # image = obj_page.find('div', class_='image newb-gallery').find('img', class_='d-block w-100p').get('src')
            # image_download = s.get(image).content
            # number += 1

            # Сохранение картинок
            # logger.debug('Сохраняем картинку')
            # save_image(key=result_title, link=image_download, number=str(number) + page)
            # logger.debug('Сохранил картинку')
            # Получение картинок
            # get_image(result_title, str(number) + page)

        for key, value in info_about_objects.items():
            insert_data(name=str(key), value=value, user_country=user_country)

            # filename = r"\1.webp"
            # path = os.path.join(fr"..\images")


def main(country, user_page):
    create_content_data(user_country=str(country))
    try:
        get_site(user_country=str(country), page=str(user_page))
    except:
        print('Error')


if __name__ == "__main__":
    try:
        main(input('Введите страну: '), input('Введите кол-во строк: '))
    except KeyboardInterrupt:
        print('THE END')

