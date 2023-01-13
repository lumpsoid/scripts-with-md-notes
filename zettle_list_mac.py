#!/usr/local/bin/python3

import os  # чтобы получить лист названия файлов 
import re  # regex 
import json  # для экспорта 
import codecs  # чтобы сохранять данные в utf-8 (русский язык)
import pathlib  # для получения даты создания
import datetime  # для работы со временем


zettel_list = []
with os.scandir('/Users/qq/Dropbox/Obsidian') as it:  # выводит список всех файлов в директории
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file():  # проверяет файл на скрытый
            file_path = '/Users/qq/Dropbox/Obsidian/' + entry.name
            # проверка на новые изменения в файле
            file_date_check = pathlib.Path(file_path)
            delta_change_to_current = datetime.datetime.today() - datetime.datetime.fromtimestamp(file_date_check.stat().st_mtime)
            if delta_change_to_current < datetime.timedelta(days=6):
                # забор первой строки
                with open(file_path, encoding='utf-8') as f:
                    first_line = f.readline()
                    first_line = first_line.rstrip('\n')
                first_line = re.sub('#\s', '', first_line)
                first_line = re.sub('-\s', '', first_line)
                # забор id
                zettle_id = re.search('[0-9]+', entry.name)  # забираем из названия id
                # перенос в контейнер
                if not zettle_id is None:
                    zettel_list.append(f'{first_line} [[{zettle_id[0]}]]')
# export
with codecs.open('/Users/qq/Dropbox/Obsidian/zettel_list.txt', 'a', encoding='utf-8') as file:
    file.write('\n'.join(zettel_list))