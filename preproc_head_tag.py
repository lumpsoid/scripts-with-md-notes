import os  # чтобы получить лист названия файлов
import re  # regex

dir_path = '/home/qq/Documents/i'

with os.scandir(dir_path) as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file() and entry.name.endswith('.md'):
            file_path = dir_path + '/' + entry.name
            with open(file_path, encoding='utf-8') as f:
                full_file = f.readlines()
            
            if len(full_file) < 2:
                continue
            
            if full_file[0][0] == "#" and "tag" in full_file[1]:
                continue

            if not full_file[0][0] == "#":
                full_file[0] = '# ' + full_file[0]

            if re.search('^#[a-zA-Zа-яА-Я]+', full_file[1]):
                full_file[1] = 'tag: ' + full_file[1]
            
            with open(file_path, mode="w", encoding='utf-8') as f:
                f.write("".join(full_file))