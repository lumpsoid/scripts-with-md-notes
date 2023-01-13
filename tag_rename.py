import os  # чтобы получить лист названия файлов
import re  # regex
import numpy as np
from tqdm import tqdm

dir_path = '/home/qq/Vault'
searched_hashtag = '#Daily'
new_hashtag = '#daily'

with os.scandir(dir_path) as vault:
    for note in vault:
        if not note.name.startswith('.') and note.is_file() and note.name.endswith('.md'):
            note_path = dir_path + '/' + note.name
            with open(note_path, encoding='utf-8') as n:
                full_note = n.readlines()
            note_search = np.array([1 if re.search(f'{searched_hashtag}', i) else 0 for i in full_note])
            if any(note_search):
                change_spot = np.argwhere(note_search == 1)
                print('note_search:', note_search)
                print('change_spot:', change_spot)
                transformed_note = []
                for line in full_note:
                    line = re.sub(f'{searched_hashtag}', f'{new_hashtag}', line)
                    transformed_note.append(line)
                full_note.clear()
                with open(note_path, 'w', encoding='utf-8') as n:
                    n.write(''.join(transformed_note))
                transformed_note.clear()    