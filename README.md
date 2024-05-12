<h1 align="center">Hi there, I'm Baizak 
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>

# Event Planning App Backend
Этот репозиторий содержит бэкенд для приложения "Event Planning App". Бэкенд разработан на основе фреймворка Django для обеспечения функциональности, связанной с управлением событиями, пользователями и другими аспектами приложения.

## Дизайн проекта (который был на мидтерм)
https://www.figma.com/file/a8s26D1PTFpggQCiYdek6H/Event-Planning-app?type=design&node-id=0-1&mode=design&t=mjNld7ocTICrXei5-0

## Особенности
* Управление пользователями: регистрация, авторизация.
* Управление событиями: создание, редактирование, удаление событий.
* Возможность отправлять сообщения (отправитель/получатель)
* Управление профилем (редактирование, личный кабинет)
* Возможность добавить шаблон/открытку к мероприятию с названием, описанием, фото
* Обработка запросов на основе REST API.

## Технологии
* Язык программирования: Python
* Фреймворк: Django
* База данных: PostgreSQL
* Аутентификация и авторизация: Django REST Framework (DRF)
* Другие библиотеки: Django REST framework, Django ORM

## Установка
1. Клонируйте репозиторий на свой компьютер:
```bash
git clone https://github.com/Baizaknew/FinalSoftwareEngineering.git
```

2. Создайте базу данных PostgreSQL и настройте подключение в файле settings.py.

3. Примените миграции:
```
python manage.py migrate
```
4. Запустите сервер:
```
python manage.py runserver
```

## Документация API
API документировано с помощью Swagger UI. После запуска сервера вы можете получить доступ к документации по адресу http://127.0.0.1:8000/

## Screenshots
![](../../Screenshot_22.png)
![](../../Screenshot_23.png)
![](../../Screenshot_24.png)
![](../../Screenshot_25.png)
![](../../Screenshot_26.png)
![](../../Screenshot_27.png)
![](../../Screenshot_28.png)
![](../../Screenshot_29.png)

## Tutorial
link