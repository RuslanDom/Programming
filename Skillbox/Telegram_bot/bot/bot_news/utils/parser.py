import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time


def first_news():
    url = 'https://www.securitylab.ru/news/'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) '
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    articles = soup.find_all('a', class_='article-card inline-card')
    news_dict = {}
    for article in articles:

        title = article.find('h2', class_='article-card-title').text.strip()
        description = article.find('p').text.strip()
        link = url + article.get('href')[6:]
        article_id = link.split('/')[-1][:-4]
        site_date = article.find('time').get('datetime')
        date_format = datetime.fromisoformat(site_date)
        date = datetime.strftime(date_format, "%d-%m-%Y %H:%M:%S")
        date_time = time.mktime(datetime.strptime(date, "%d-%m-%Y %H:%M:%S").timetuple())

        news_dict[article_id] = {
            'datetime': date_time,
            "title": title,
            "description": description,
            "link": link
        }


def last_news():
    url = 'https://www.securitylab.ru/news/'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) '
    }
    with open('news_dict.json', encoding='utf-8') as file:
        news_dict = json.load(file)

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    articles = soup.find_all('a', class_='article-card inline-card')
    fresh_news = {}
    for article in articles:

        article_id = article.get('href')[:-4][6:]
        if article_id in news_dict:
            continue
        else:
            title = article.find('h2', class_='article-card-title').text.strip()
            description = article.find('p').text.strip()
            link = url + article.get('href')[6:]
            article_id = link.split('/')[-1][:-4]
            site_date = article.find('time').get('datetime')
            date_format = datetime.fromisoformat(site_date)
            date = datetime.strftime(date_format, "%d-%m-%Y %H:%M:%S")
            date_time = time.mktime(datetime.strptime(date, "%d-%m-%Y %H:%M:%S").timetuple())

            news_dict[article_id] = {
                'datetime': date_time,
                "title": title,
                "description": description,
                "link": link
            }

            fresh_news[article_id] = {
                'datetime': date_time,
                "title": title,
                "description": description,
                "link": link
            }

    with open('news_dict.json', 'w', encoding='utf-8') as file:
        json.dump(news_dict, file, indent=4, ensure_ascii=False)

    with open('update_list.json', 'w', encoding='utf-8') as file:
        json.dump(fresh_news, file, indent=4, ensure_ascii=False)

    return fresh_news


def main():
    first_news()
    last_news()


if __name__ == "__main__":
    main()