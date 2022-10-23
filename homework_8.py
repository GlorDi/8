import requests
import yadisk
from pprint import pprint
import posixpath
import os

url = 'https://akabab.github.io/superhero-api/api/all.json'
res = requests.get(url)
heroes = res.json()
three_heroes = filter(lambda hero: hero['name'] in ['Hulk', 'Captain America', 'Thanos'], heroes)
heroes_res = {hero['name']:hero['powerstats']['intelligence'] for hero in three_heroes}
pprint(max(heroes_res, key=heroes_res.get))



def recursive_upload(y, from_dir, to_dir):
     for root, dirs, files in os.walk(from_dir):
         p = root.split(from_dir)[1].strip(os.path.sep)
         dir_path = posixpath.join(to_dir, p)

         try:
             y.mkdir(dir_path)
         except yadisk.exceptions.PathExistsError:
             pass

         for file in files:
             file_path = posixpath.join(dir_path, file)
             p_sys = p.replace("/", os.path.sep)
             in_path = os.path.join(from_dir, p_sys, file)
             try:
                 y.upload(in_path, file_path)
             except yadisk.exceptions.PathExistsError:
                 pass

y = yadisk.YaDisk(token="токен")
to_dir = "/тестирование"
from_dir = "C:\\Users\\Dima\\Documents\\Python_home_work\\8\\test"
recursive_upload(y, from_dir, to_dir)