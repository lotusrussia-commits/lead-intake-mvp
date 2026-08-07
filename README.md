# Lead Intake MVP

## Описание

Backend-сервис для автоматизированного приёма заявок через REST API.

Клиент отправляет данные на endpoint `POST /lead`. Сервис валидирует входные данные, сохраняет заявку в SQLite и записывает событие в журнал.

Репозиторий: [github.com/lotusrussia-commits/lead-intake-mvp](https://github.com/lotusrussia-commits/lead-intake-mvp)

## Возможности

- REST API на FastAPI
- приём заявок через `POST /lead`
- валидация входных данных (Pydantic)
- сохранение заявок в SQLite (SQLAlchemy)
- автоматическое создание таблицы `leads` при запуске
- обработка ошибок (HTTP 400, HTTP 500)
- логирование успешных заявок и ошибок
- интерактивная документация Swagger/OpenAPI

## Технологии

- Python 3.12
- FastAPI
- Pydantic
- SQLAlchemy
- SQLite
- Uvicorn
- Git / GitHub

## Структура проекта

```text
lead-intake-mvp/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI-приложение и маршруты
│   ├── database.py      # подключение к SQLite
│   ├── models.py        # SQLAlchemy-модель Lead
│   ├── schemas.py       # Pydantic-схема для валидации
│   └── logger.py        # журнал событий
├── .gitignore
├── requirements.txt
└── README.md
```

При работе локально создаются файлы `leads.db` и `events.log` (они не попадают в Git).

## Установка

Клонировать репозиторий:

```bash
git clone https://github.com/lotusrussia-commits/lead-intake-mvp.git
cd lead-intake-mvp
```

Создать и активировать виртуальное окружение:

```bash
python3 -m venv venv
source venv/bin/activate
```

Установить зависимости:

```bash
pip install -r requirements.txt
```

## Запуск

```bash
uvicorn app.main:app --reload
```

Сервис будет доступен по адресу `http://127.0.0.1:8000`.

## API

### GET /

Проверка работоспособности сервиса.

**Ответ:**

```json
{
  "message": "Lead Intake MVP работает!"
}
```

### POST /lead

Создание новой заявки.

**Тело запроса** (все поля обязательны):

```json
{
  "name": "Иван Петров",
  "contact": "ivan@example.com",
  "source": "website",
  "comment": "Хочу узнать стоимость услуги"
}
```

**Успешный ответ** (HTTP 200):

```json
{
  "status": "success",
  "message": "Заявка сохранена",
  "id": 1
}
```

## Swagger

Интерактивная документация API:

```
http://127.0.0.1:8000/docs
```

## Хранение данных

Данные сохраняются в SQLite-файл `leads.db` в корне проекта.

Таблица `leads`:

| Поле       | Описание              |
|------------|-----------------------|
| id         | первичный ключ        |
| created_at | дата и время создания |
| name       | имя клиента           |
| contact    | контакт (email/телефон) |
| source     | источник заявки       |
| comment    | комментарий           |

## Логирование

События записываются в файл `events.log` в корне проекта.

Формат записи:

```text
2026-07-28 22:59:51,123 - New lead saved: 1
```

При ошибке сохранения в лог добавляется запись вида:

```text
2026-07-28 23:00:00,456 - ERROR: <описание ошибки>
```

## Обработка ошибок

**HTTP 400** — некорректные или неполные данные запроса:

```json
{
  "error": "Некорректные данные заявки",
  "details": [...]
}
```

**HTTP 500** — ошибка при сохранении в базу данных:

```json
{
  "detail": "Ошибка сохранения заявки"
}
```

## Возможные улучшения

- миграция на PostgreSQL
- авторизация API-ключом или JWT
- контейнеризация (Docker)
- автоматические тесты (pytest)

## Демо

Проект развернут на VPS с использованием **Coolify** и доступен через публичный URL.

**Работающее приложение:**
http://hlyhk4al5aos38uofcm6rxau.194.67.74.131.sslip.io

**Swagger / API документация:**
http://hlyhk4al5aos38uofcm6rxau.194.67.74.131.sslip.io/docs

### Проверка API

Главная страница:

```text
GET /
```

Ответ:

```json
{
  "message": "Lead Intake MVP работает!"
}
```

Создание лида:

```text
POST /lead
```

Пример запроса:

```json
{
  "name": "Иван Петров",
  "contact": "ivan@example.com",
  "source": "website",
  "comment": "Тестовый лид с VPS"
}
```

Пример успешного ответа:

```json
{
  "status": "success",
  "message": "Заявка сохранена",
  "id": 2
}
```

### Деплой

Приложение запущено на VPS:

* **OS:** Ubuntu 24.04 LTS
* **CPU:** 2 vCPU
* **RAM:** 2 GB
* **Диск:** 40 GB
* **Платформа деплоя:** Coolify
* **Web-сервер:** Uvicorn
* **Порт приложения:** 8000
* **Состояние:** Running
