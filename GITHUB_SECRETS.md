# GitHub Secrets Configuration

Добавьте эти секреты в Settings → Secrets and variables → Actions:

## Существующие (у вас уже настроены):
- `SERVER_IP` - IP адрес сервера
- `SERVER_USER` - имя пользователя на сервере
- `SERVER_SSH_KEY` - приватный SSH ключ для доступа

## Новые секреты (нужно добавить):

### База данных
- `POSTGRES_USER`: resume_user
- `POSTGRES_PASSWORD`: [создайте надежный пароль]
- `POSTGRES_DB`: resume_db

### Приложение
- `APP_SECRET_KEY`: [сгенерируйте случайную строку минимум 32 символа]
- `DOMAIN_NAME`: ruvpnservice.ru
- `ALLOWED_ORIGINS`: https://ruvpnservice.ru

### Генерация APP_SECRET_KEY:
```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

### Генерация надежного пароля для PostgreSQL:
```bash
openssl rand -base64 32
```

## Важно:
После добавления секретов, pipeline автоматически создаст `.env` файл на сервере при следующем деплое.