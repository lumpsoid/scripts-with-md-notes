import os  # чтобы получить лист названия файлов
import re  # regex
import codecs  # чтобы сохранять данные в utf-8 (русский язык)

path_folder = '/home/qq/i'

all_in_one = []
count_entries = 0
for entry in sorted(os.scandir(path_folder), key=lambda x: x.name):
    if not entry.name.startswith('.') and entry.is_file() and entry.name.endswith('.md'):
        text = []
        count_entries += 1
        file_path = f'{path_folder}/{entry.name}'
        file_name = re.sub('.md', '', entry.name)
        with open(file_path, encoding='utf-8') as f:
            text = f.readlines()
        try:
            all_in_one.append(f'{file_name} {text[0]}')
            all_in_one.extend(text)
            all_in_one.append('\n---\n')
        except: 
            pass
# export
with codecs.open(r'/home/qq/i/all_in_one.md', 'w', encoding='utf-8') as file:
    file.write(''.join(all_in_one))