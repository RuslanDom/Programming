# Telegram bot for the Skillbox platform 
## Финальная работа
## Описание
 Бот в мессенджере Telegram для поиска видео ресурсов с использованием 
 API сайта https://kinopoisk.dev<br>Данный проект имеет возможность двух типов
поиска:
- Поиск по ключевому слову в названии
- Поиск с использованием фильтра по году, стране производства и жанру

Также имеет возможность получение истории всех действий пользователя.
## Установка
Для корректной работы программы необходимо наличие данных библиотек,
установку возможно произвести через терминал:<br>
```
pip install aiogram==3.2.0
pip install requests==2.31.0
pip install python-dotenv==1.0.1
pip install loguru==0.7.2
pip install bs4==0.0.1
pip install peewee==3.17.6
```
## Запуск бота
Перейдите в файл `main.py` и запустите его, в PyCharm возможно сочетание клавиш
`Shift + F10`<br>Затем запустите Telegram и в поиске найдите `@SenseiCatPushbot`
или перейдите по этой [ссылке](https://t.me/SenseiCatPushbot).<br>
Так вы попадёте в диалоговое окно бота, нажмите снизу кнопку `ЗАПУСТИТЬ`. 
Поздравляю, вы только что запустили бота и он готов к работе.
## Команды и возможности бота
Для начала познакомимся с командами при помощи которых вы можете общаться 
с ботом.

| *command - команда*       | *description - описание*               |               
|---------------------------|----------------------------------------|
|  start                    | Начало работы                          |
|  help                     | Справка - помощь                       |
|  search                   | Поиск по фильтрам                      |
|  result_search_by_filters | Получить найденные по фильтрам фильмы  |
|  find                     | Поиск фильма по названию               |
|  result_search_by_word    | Получить найденные по названию фильмы  |
|  clear_data               | Очистить Базу Данных                   |
|  history                  | Получить историю запросов пользователя |
|  clear_history            | Очистить историю                       |

### /start
Команда для начала работы бота, приветствует пользователя по его `username`<br>
[screenshot_start](https://github.com/RuslanDom/scrennshots/blob/main/start.png)
### /help
Команда для получения справки по командам
[screenshot_help](https://github.com/RuslanDom/scrennshots/blob/main/help.png)
### /search
Команда использует API https://api.kinopoisk.dev/v1.4/movie для поиска фильмов и сериалов по фильтрам (год, жанр, страна производства),
по умолчанию фильтра установлены (2024, комедии, США).<br>Можно изменять фильтра выборочно или полностью.<br>
При выборе команды search появится вот такая inline keyboard [screenshot_search](https://github.com/RuslanDom/scrennshots/blob/main/search1.png)<br>
После выбора к примеру раздела фильм появятся фильтра [screenshot_search1](https://github.com/RuslanDom/scrennshots/blob/main/search2.png)<br>
Выбор года производства: [screenshot_search2](https://github.com/RuslanDom/scrennshots/blob/main/search_year.png)<br>
После выбора очередного фильтра бот спросит, хотите ли добавить ещё фильтра 
[screenshot_search_add](https://github.com/RuslanDom/scrennshots/blob/main/search_add.png)<br>
Если ответ `ДА`, тогда вновь появится окно с дополнительными фильтрами<br>
К примеру, можно добавить фильтр жанр
[screenshot_search_add](https://github.com/RuslanDom/scrennshots/blob/main/search_genres.png)<br>
После ответа `НЕТ`, база данных будет сформирована в соответствии с указанными фильтрами [screenshot_search_no](https://github.com/RuslanDom/scrennshots/blob/main/search_no.png)<br>
### /result_search_by_filters
Данная команда выведет сохранённые в базу данных результаты поиска [screenshot_search_result](https://github.com/RuslanDom/scrennshots/blob/main/search_result.png), между этой командой и командой 
`/get_result_search_by_word` практически нет, <br> за исключением того что при неправильном вводе фильтров выйдет подсказка о 
том что пользователь допустил ошибку [screenshot_error](https://github.com/RuslanDom/scrennshots/blob/main/get_response.png)<br>
### /find
При помощи этой команды вы можете использовать другое API https://api.kinopoisk.dev/v1.4/movie/search и произвести поиск по названию 
[screenshot_find](https://github.com/RuslanDom/scrennshots/blob/main/find.png)<br>
### /result_search_by_word
Получить результаты поиска по названию или последних данных из БД
[screenshot_find_result](https://github.com/RuslanDom/scrennshots/blob/main/find_result.png)<br>
### /clear_data
Очистить базу данных от старых результатов поиска [screenshot_clear_data](https://github.com/RuslanDom/scrennshots/blob/main/clear_data.png)<br>
### /history
Получить всю историю пользователя [screenshot_history](https://github.com/RuslanDom/scrennshots/blob/main/history.png)<br>
### /clear_history
Очистить историю пользователя [screenshot_clear_history](https://github.com/RuslanDom/scrennshots/blob/main/clear_history.png)<br>
### Другие возможности бота
Реализованы подсказки имеющихся команд при наведении на кнопку `meny`
[screenshot_set_commands](https://github.com/RuslanDom/scrennshots/blob/main/set_command.png), а также<br>
ЭХО - бот при получении неизвестных команд [screenshot_echo](https://github.com/RuslanDom/scrennshots/blob/main/echo.png)


















