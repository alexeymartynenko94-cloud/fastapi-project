# FastAPI Microservices

Проект состоит из двух микросервисов:
- ToDo-сервис для управления задачами
- Сервис сокращения URL

---

## Локальный запуск

### ToDo-сервис

```bash
cd todo_service

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

uvicorn main:app --reload --port 8000
```

Swagger: http://localhost:8000/docs

---

### URL Shortener

```bash
cd shortener_service

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

uvicorn main:app --reload --port 8001
```

Swagger: http://localhost:8001/docs

---

## Эндпоинты

### ToDo Service

| Метод | URL | Описание |
|-----|-----|---------|
| POST | `/items` | Создание задачи |
| GET | `/items` | Получение всех задач |
| GET | `/items/{item_id}` | Получение задачи по ID |
| PUT | `/items/{item_id}` | Обновление задачи |
| DELETE | `/items/{item_id}` | Удаление задачи |

---


### URL Shortener

| Метод | URL | Описание |
|-----|-----|----------|
| POST | /shorten | Создать короткую ссылку |
| GET | /{code} | Редирект |
| GET | /stats/{code} | Информация о ссылке |

---

## Docker-запуск

```bash
docker build -t friend-todo ./todo_service
docker build -t friend-shorturl ./shortener_service

docker run -d -p 8000:80 -v todo_data:/app/data friend-todo
docker run -d -p 8001:80 -v shorturl_data:/app/data friend-shorturl
```
