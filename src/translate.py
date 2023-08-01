import time
import requests
import argparse

from pathlib import Path


project_path = Path(__file__).resolve().parents[1]
api_url = 'https://api.openai.com/v1/chat/completions'


def arguments_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="API для GPT-3.5"
    )

    parser.add_argument('-t', '--token',
                        default='secret-key',
                        type=str,
                        help='Файл с токеном по пути src/prompt_api/tokens/')

    parser.add_argument('-m', '--model',
                        default="gpt-3.5-turbo",
                        type=str,
                        help='Название используемой модели')

    parser.add_argument('-p', '--prompt',
                        default="example",
                        type=str,
                        help='Текст используемой затравки')

    parser.add_argument('--text',
                        type=str,
                        help='Текст сообщения для затравки')

    return parser.parse_args()


def ask_gpt(token, model, content, sentence):
    """
    Отправляет единичный запрос в рамках затравки content языковой модели и возвращает ее ответ,
    без поддержки диалогового режима,
    в исходной затравке "TARGET" заменяется на значение переменной sentence

    :param token: токен от OpenAI API
    :param model: версия используемой модели
    :param content: текст затравки
    :param sentence: выражение для подстановки в контекст затравки
    :return:
        Ответ языковой модели на заданную затравку
    """
    retries = 0

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(token)
    }

    # temperature и top_p - вариативность ответов, указывать либо temperature, либо top_p, но не вместе
    # n - количество ответов, при низкой вариативности будет возвращать одинаковые ответы
    data = {
        "model": model,
        "temperature": 0.3,
        # "top_p": 0.9,
        # "n": 5,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": content.replace('TARGET', sentence)}
        ]
    }

    # При частых запросах появляется 503 код:
    # That model is currently overloaded with other requests.
    while retries <= 5:
        response = requests.post(api_url, headers=headers, json=data)

        if response.status_code == 503:
            retries += 1
            time.sleep(0.25)

        elif response.status_code == 200:
            retries = 10

    try:
        answer = {
            "status": "Code: {}, Status: {}".format(response.status_code, response.reason),
            "message": response.json()
        }
    except KeyError:
        answer = {
            "status": "Code: {}, Status: {}".format(response.status_code, response.reason),
            "message": response.json()
        }

    return answer


if __name__ == '__main__':
    args = arguments_parser()

    # читаем токен из файла
    secret_path = project_path.joinpath(f"token/{args.token}")
    with open(secret_path, 'r') as file:
        tok = file.read()

    # читаем текст затравки
    prompt_path = project_path.joinpath(f"prompt/{args.prompt}")
    with open(prompt_path, 'r') as file:
        prompt = file.read()

    mes = ask_gpt(tok, args.model, prompt, args.text)

    print(mes)
