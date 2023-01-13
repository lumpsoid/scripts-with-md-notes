import os  # чтобы получить лист названия файлов
import re  # regex
import numpy as np
from tqdm import tqdm

dir_path = '/home/qq/Vault'

with os.scandir(dir_path) as it:
    for entry in tqdm(it):
        if not entry.name.startswith('.') and entry.is_file() and entry.name.endswith('.md') and not re.search(r'[0-9]{14}', entry.name):
            file_path = dir_path + '/' + entry.name
            with open(file_path, encoding='utf-8') as f:
                full_file = f.readlines()[:6]
            file_search = [1 if re.search(r'timestamp:: [0-9]+', i) else 0 for i in full_file]
            if any(file_search):
                timestamp_in = np.argmax(file_search)
                timestamp = re.search(r'[0-9]+', full_file[timestamp_in]).group(0)
                if len(timestamp) < 14:
                    timestamp = timestamp + str((int(timestamp[-1]) + int(timestamp[-2]))) + str((int(timestamp[-3]) + int(timestamp[-4])))
                    if len(timestamp) > 14:
                        timestamp = timestamp[:14]
                # формируем данные
                new_file_lines = [re.sub(r".md", '', entry.name) + '\n']
                new_file_name = dir_path + '/' + timestamp + '.md'
                old_link = re.sub(r".md", '', entry.name)
                # перед тем как записывать все окончательно, нужно проверить старые линки
                with os.scandir(dir_path) as vault:
                    for note in vault:
                        if not note.name.startswith('.') and note.is_file() and note.name.endswith('.md'):
                            note_path = dir_path + '/' + note.name
                            with open(note_path, encoding='utf-8') as n:
                                full_note = n.readlines()
                            note_search = [1 if re.search(f'\[\[{old_link}\]\]', i) else 0 for i in full_note]
                            if any(note_search):
                                transformed_note = []
                                for line in full_note:
                                    line = re.sub(f'\[\[{old_link}\]\]', f'{old_link} [[{timestamp}]]', line)
                                    transformed_note.append(line)
                                full_note.clear()
                                with open(note_path, 'w', encoding='utf-8') as n:
                                    n.write(''.join(transformed_note))
                                transformed_note.clear()          
                # заключительный этап
                with open(file_path, encoding='utf-8') as f:
                    full_file = f.readlines()
                full_file.pop(timestamp_in)
                new_file_lines.extend(full_file)
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(''.join(new_file_lines))
                os.rename(file_path, new_file_name)
print('Готово!')