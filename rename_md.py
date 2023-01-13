import os  # чтобы получить лист названия файлов
import re  # regex

dir_path = '/home/qq/Vault'

with os.scandir(dir_path) as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file() and entry.name.endswith('.md') and re.search(r'[0-9]{14} [а-яёА-ЯЁa-zA-Z0-9 ]+', entry.name):
            file_path = dir_path + '/' + entry.name
            new_file_name = dir_path + '/' + re.search(r'[0-9]{14}', entry.name).group(0) + '.md'
            new_file = re.sub(r"[0-9 ]{15}", '', entry.name)  # сначала здесь будет новая первая строка
            new_file = [re.sub(r".md", '', new_file) + '\n']
            with open(file_path, encoding='utf-8') as f:
                full_file = f.readlines()
            if len(full_file) > 0 and re.search(f'{new_file[0]}', full_file[0]):  # если файл не пустой
                full_file.pop(0)
                new_file.extend(full_file)
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(''.join(new_file))
                os.rename(file_path, new_file_name)
            else:  # если пустой
                new_file.extend(full_file)  # теперь здесь весь файл, который нужно записать
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(''.join(new_file))
                os.rename(file_path, new_file_name)