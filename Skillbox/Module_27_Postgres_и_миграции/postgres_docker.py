# --- Запустить Postgres через docker ---

# Запускаем контейнер, image postgres скачается с DockerHub автоматически

# docker run --name skillbox-postgres --rm -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres
# -v /tmp:/var/lib/postgresql/data/pgdata -p 55432:5432 -it postgres

# Заходим с другой вкладки - консоли и подключаемся к терминалу
# docker exec -it skillbox-postgres /bin/sh

# Заходим в psql на юзера postgres
# psql -U postgres

# COMMANDS in psql

# \l - доступные БД
# \с <nameDB> - подключение к БД
# \dt - список таблиц

# Создание таблицы пример: create table test_table (id integer primary key, name varchar(255));
# Вставка пример: insert into test_table (id, name) values (1, 'Adam');
# Получение пример: select * from test_table;
# Обновление данных пример:  update test_table set name='Alex' where id=1;


# --- Запуск postgres через docker-compose ---
# Команда на запуск выполняем из директории с .yaml файлом который хотим запустить
# docker-compose up
#