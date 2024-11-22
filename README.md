# lm-api

API для GPT

P.S.: Работает только с VPN

### Установка
```shell
python -m venv venv
source venv/bin/activate
pip install -r requierements.txt
pip install -e .
```

### Как пользоваться

#### Настройка

1. Записать токен [token/secret-key](token/secret-key-info)
2. Создать файл с затравкой, пример [prompt/example](prompt/example)

Основной файл [src/translate.py](src/translate.py), функция ask_gpt()
```shell
python -m translate --token secret-key-info --model gpt-3.5-turbo --prompt example --text "python"
```

На примере команды curl [инструкция к API](https://platform.openai.com/docs/api-reference/chat)
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

Или через библиотеку openai [инструкция к библиотеке](https://platform.openai.com/docs/guides/gpt)
```python
from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message)
```
