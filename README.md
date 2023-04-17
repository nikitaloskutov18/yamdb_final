![Yamdb Workflow Status](https://github.com/ragecodemode/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg?branch=master&event=push)

### Описание
Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории:«Книги», «Фильмы», «Музыка». Список категорий может быть расширен. Настроика для приложения Continuous Integration и Continuous Deployment, реализация:

```
автоматический запуск тестов,
обновление образов на Docker Hub,
автоматический деплой на боевой сервер при пуше в главную ветку main.
```
```
Как запустить проект:
```
Все описанное ниже относится к ОС Linux.

Клонируем репозиторий и и переходим в него:

git clone git@github.com:themasterid/yamdb_final.git
cd yamdb_final
Создаем и активируем виртуальное окружение:
python3 -m venv venv
Windows:
source venv/Scripts/activate
Linux:
source venv/bin/activate
Обновим pip:
python -m pip install --upgrade pip 
Ставим зависимости из requirements.txt:
pip install -r api_yamdb/requirements.txt 
Переходим в папку с файлом docker-compose.yaml:
cd infra

Предварительно установим Docker на ПК под управлением Linux (Ubuntu 22.10), для Windows немного иная установка, тут не рассматриваем:

sudo apt update && apt upgrade -y

Удаляем старый Docker:
sudo apt remove docker
Устанавливаем Docker:
sudo apt install docker.io
Смотрим версию Docker (должно выдать Docker version 20.10.16, build 20.10.16-0ubuntu1):
docker --version
Активируем Docker в системе, что бы при перезагрузке запускался автоматом:
sudo systemctl enable docker
Запускаем Docker:
sudo systemctl start docker
Смотрим статус (выдаст статус, много букв):
sudo systemctl status docker


Перезапустим систему:

sudo reboot

```
Установка PostgreSQL:
```
sudo apt install postgresql postgresql-contrib -y
Управляем БД:
Остановить
sudo systemctl stop postgresql
