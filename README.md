# Тестовое задание (кодовое имя проекта - good_deeds)

## Задание проекта
Разработайте API веб-приложения для создания объявлений о безвозмездной передаче вещей, где владелец может выбирать претендентов на основе заявок. В заявке можно указать финансовое вознаграждение за вещь или комментарий.

## Шаблон наполнения .env
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с
postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД

## Инструкция по установке и запуску проекта

1. Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone https://github.com/rusinovada/good_deeds
```

```bash
cd cd good_deeds
```

Создать и активировать виртуальное окружение:

```bash
python3 -m venv env
```
Linux и MacOS:
```bash
source env/bin/activate
```
Windows:
```bash
source env/Scripts/activate
```
Установить зависимости из файла requirements.txt:

```bash
python3 -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

Выполнить миграции:

```bash
python3 manage.py migrate
```

Запустить проект:

```bash
python3 manage.py runserver
```
