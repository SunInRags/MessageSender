# Тестовый проект для автоматической рассылки

## Используемый стек:

* `django + drf`
* `postgresql`
* `celery`
* `redis`
* `docker`
* `swagger`

## Для развёртывания приложения необходимо:

* установить docker: https://www.docker.com/
* клонировать репозиторий: git clone https://github.com/SunInRags/MessageSender.git
* в корневой папке выполнить команду `docker-compose up -d --build`
* сервер должен быть доступен на https://localhost:8000

## Доступные API:
* swagger доступен по адресу http://localhost:8000/docs/ там вы найдёте все используемые в проекте эндпоинты
* админка доступна по адресу http://localhost:8000/admin/ для логина под суперюзером можно использовать djangosender - comlicatedpassword
* получить список всех очередей можно по адресу GET http://localhost:8000/sender/api/queue/
* получить информацию по конкретной очереди можно по адресу GET http://localhost:8000/sender/api/queue/{queue_id}/. При подобном запросе вы так же получите подробный список сообщений в рамках данной очереди
* запустить новую очередь можно по адресу POST http://localhost:8000/sender/api/queue/
* запросы PUT, PATCH, DELETE доступны по адресу http://localhost:8000/sender/api/queue/{queue_id}/
* все запросы выше доступны и для таблицы клиентов по адресам http://localhost:8000/sender/api/client/ и http://localhost:8000/sender/api/client/{client_id}/
## Дополнительные задания
* пункт 3 - проект запускается при помощи docker-compose
* пункт 5 - в проекте доступен swagger
* пункт 6 - по адресу http://localhost:8000/admin/ можно управлять рассылками и адресной книгой