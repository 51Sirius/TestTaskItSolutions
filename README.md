# Тестовое задание для ItSolution

Требуется разработать API-сервис для получения данных о первых 10 объявлениях по
ссылке https://www.farpost.ru/vladivostok/service/construction/guard/+/Системы+видеонаблюдения/.
Для решения задачи необходимо:

1. Разработать модели при помощи фреймворка Django/FastAPI со `следующими полями:

- заголовок объявления;
- id объявления;
- автор объявления;
- количество просмотров объявления;
- позиция, на которой стоит объявление.\
  Данные могут быть добавлены в БД вручную или любым удобным для вас способом.

2. Разработать методы API для обращения к данным моделям. Запрос к API должен иметь параметр ID. При обращении, API
   должен возвращать информации об объявлении с ID, переданным в запросе, в формате JSON.

### Требования к реализации API:

1. При разработке должен быть использован язык Python и фреймворк Django/FAST Api.
2. В качестве результата должен быть предоставлен репозиторий на GitHub;
3. Сервис должен использовать принципы ООП.

#### Дополнительные требования, не обязательны к выполнению, но будут являться большим плюсом:

1. Реализована система регистрации и входа (верификации аккаунта) для подключения к API (без функционала смены и/или
   восстановления пароля);
2. Все обращения к базе данных должны быть реализованы при помощи ORM запросов.

## Запуск 

```
python -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt
cd TestTaskItSolution
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```



