#!/usr/local/bin/python3

import re
import os  # чтобы получить лист названия файлов
import re  # regex
import codecs  # чтобы сохранять данные в utf-8 (русский язык)
from tkinter import Tk

def difference(list1, list2):
   list_dif = [i for i in list1 + list2 if i not in list1 or i not in list2]
   return list_dif

# скопировать из клипборда
r = Tk()
r.withdraw()
clipboard = r.clipboard_get()
r.update() # now it stays on the clipboard after the window is closed
r.destroy()

search_for_it = re.search('[0-9]+', clipboard).group(0)  # id который нужно искать в файлах

zettel_backlinks = []
links_in_file = []
# поиск id в файлах vault
with os.scandir('/Users/qq/Dropbox/Obsidian') as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file():
            file_path = '/Users/qq/Dropbox/Obsidian/' + entry.name
            # поиск id в других файлах
            with open(file_path, 'r', encoding='utf-8') as searchfile:
                for line in searchfile:
                    if re.search(rf'\[\[{search_for_it}\]\]', line, re.M|re.I):
                        zettel_backlinks.append(re.sub('.md', '', entry.name))
# проверка на наличие этих бэклинков в начальном файле
with open(f'/Users/qq/Dropbox/Obsidian/{search_for_it}.md', 'r', encoding='utf-8') as f:
    for line in f:
        if re.search('\[\[[0-9]+\]\]', line, re.M|re.I):
            links_in_file.append(re.search('[0-9]+', line).group(0))
# удаляем повторения в целевом листе и получаем хеадер и принтим
for i in difference(links_in_file, zettel_backlinks):
    with open(f'/Users/qq/Dropbox/Obsidian/{i}.md', 'r', encoding='utf-8') as f:
            first_line = f.readline().rstrip('\n')
            first_line = re.sub('#\s', '', first_line)
            print(f'{first_line} [[{i}]]')