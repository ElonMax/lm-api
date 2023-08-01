# lm-api

API для языковой модели gpt-3.5

### Документация

Если настроен vpn: 
1. [инструкция к API](https://platform.openai.com/docs/api-reference/chat)
2. [инструкция к библиотеке openai](https://platform.openai.com/docs/guides/gpt)

Взаимодействие с gpt-3.5 при помощи POST запросов

На примере команды curl
```shell
curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [
      {
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "Hello!"
      }
    ]
  }'
```

### Установка
Вариант 1. Как пакет pip
```shell
pip install .
```
```python
# Использование в коде
from translate import ask_gpt
```

Вариант 2. Настроить переменную окружения
```shell
export PYTHONPATH=$PYTHONPATH:/путь/до/проекта/lm-api
```
```python
# Использование в коде
from src.translate import ask_gpt
```

### Как пользоваться

#### Настройка

1. Записать токен в файл [token/secret-key](token/secret-key)
2. Создать файл с затравкой, пример [prompt/example](prompt/example)

Основной файл [src/translate.py](src/translate.py), функция ask_gpt()

Запуск из консоли
```shell
python src/translate.py --token secret-key --model gpt-3.5-turbo --prompt example --text "python"
```

