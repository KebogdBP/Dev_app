# Effective Mobile - Docker Web Application

Простое веб-приложение с использованием Docker, Nginx и Python HTTP сервера.

## 📋 Требования

- Docker 20.10+
- Docker Compose 2.0+
- Git

## 🏗 Архитектура
Internet → [Port 80] → Nginx (Reverse Proxy) → [Internal Network] → Backend (Python HTTP Server:8080)

### Схема взаимодействия:
1. Пользователь отправляет HTTP-запрос на `http://localhost`
2. Nginx принимает запрос и проверяет health endpoint
3. Nginx проксирует запрос на backend:8080 через внутреннюю сеть
4. Backend обрабатывает запрос и возвращает JSON-строку
5. Nginx передает ответ пользователю с правильными заголовками

## 🚀 Быстрый старт

### Клонирование и запуск
```bash
# Клонировать репозиторий
git clone https://github.com/your-username/effective-mobile-app.git
cd effective-mobile-app

# Запустить сервисы
docker compose up -d

# Проверить логи
docker compose logs -f

# Проверить
curl http://localhost
# Ответ: "Hello from Effective Mobile!"

# Остановка
docker compose down

# Структура проекта
.
├── backend/
│   ├── Dockerfile
│   └── app.py
├── nginx/
│   └── nginx.conf
├── docker-compose.yml
├── .env
├── .gitignore
└── README.md

# Технологии
- Python 3.11 Alpine

- Nginx 1.25 Alpine

- Docker & Docker Compose


## Создайте .env файл (шаблон)

```bash
cat > .env << 'EOF'
NGINX_PORT=80
BACKEND_PORT=8080
PYTHONUNBUFFERED=1
EOF

