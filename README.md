![Yamdb Workflow Status](https://github.com/ragecodemode/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg?branch=master&event=push)

## Развёрнутый проект на сервер доступен по ссылке:

 https://158.160.21.158
----

### Описание
Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории:«Книги», «Фильмы», «Музыка». Список категорий может быть расширен. Настроика для приложения Continuous Integration и Continuous Deployment, реализация:
---

### Технологии
Pytho, Rest API, Docker, Nginx, Yandex.Cloud 

автоматический запуск тестов;
обновление образов на Docker Hub;
автоматический деплой на боевой сервер при пуше в главную ветку main.
---

### Запустк проекта

```
Склонировать репозиторий:

git clone: git@github.com:ragecodemode/yamdb_final.git

cd yamdb_final

Создаем и активируем виртуальное окружение:

python -m venv venv

source venv/Scripts/activate

Ставим зависимости из requirements.txt:

pip install -r api_yamdb/requirements.txt 

В папке infra создаем файл .env с следующим содержимом:

DB_ENGINE=django.db.backends.postgresql 
DB_NAME=postgres 
POSTGRES_USER=postgres 
POSTGRES_PASSWORD=postgres 
DB_HOST=db 
DB_PORT=5432

В settings.py добавляем следующее:

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.postgresql'),
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT')
    }
}

Переходим в папку с файлом docker-compose.yaml:

cd infra

Собираем контейнеры, выполняем миграции и собираем статику:

docker-compose up -d --build

docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input

Создаем дамп базы данных:

docker-compose exec web python manage.py dumpdata > fixtures.json

Теперь проект доступен по адресу: http://localhost/.
```