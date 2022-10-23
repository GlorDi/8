import requests
from pprint import pprint

url = 'https://akabab.github.io/superhero-api/api/all.json'
res = requests.get(url)
heroes = res.json()
three_heroes = filter(lambda hero: hero['name'] in ['Hulk', 'Captain America', 'Thanos'], heroes)
heroes_res = {hero['name']:hero['powerstats']['intelligence'] for hero in three_heroes}
pprint(max(heroes_res, key=heroes_res.get))


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = ...
    token = ...
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)