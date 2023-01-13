#!/usr/bin/python3

import re  # regex
import codecs  # чтобы сохранять данные в utf-8 (русский язык)
from datetime import datetime  # для работы со временем
from datetime import timedelta

path_to_book = '/Users/qq/Библиотека Calibre/Riu Murakami/Miso-sup/Miso-sup - Riu Murakami.txt'
name_of_book = 'Miso-sup - Riu Murakami'
path_to_book_zettel = '/Users/qq/Dropbox/Obsidian/20220227220307.md'

book_sentences = []
with open(path_to_book, 'r', encoding='utf-8') as file:
    book_sentences.extend(file)  # creating list of sentences

n = 50  # how much sentensec in one chunk
book_parts = [book_sentences[i:i+n] for i in range(0, len(book_sentences), n)]  #spliting book in chunks of given lenght(n)
chapters = {}

# inserting serial number of a chunk at top of it
# and links to previous and next in bottom of a file
for i in range(len(book_parts)):
    now = datetime.now() + timedelta(seconds=i)
    chapters.update({f'{name_of_book} {i}': now.strftime("%Y%m%d%H%M%S")})
    book_parts[i].insert(0, f'{name_of_book} {i}')
    book_parts[i].extend(['\n', '\n', '\n', f'{name_of_book} {i-1}', f'{name_of_book} {i+1}'])
for parts in book_parts:
    for i in range(len(parts)):
        if not re.search(f'{name_of_book}', parts[i]) is None:
            parts[i] = parts[i] + f' [[{chapters.get(parts[i])}]]\n'  # adding links
toc_file = [f'- [ ] {k} [[{v}]]\n' for k,v in chapters.items()]
toc_file.insert(0, f'{name_of_book}\n')  # adding header to the toc file with name of the book
toc_file.extend(['\n', '\n', '\n', 'Книги [[20220227220307]]'])  # adding link to the Book zettel

#export
for i in range(len(book_parts)):
    file_id = re.search('[0-9]{14}', book_parts[i][0])
    if file_id:
        with codecs.open(f'/Users/qq/Dropbox/Obsidian/{file_id.group(0)}.md', 'w', encoding='utf-8') as file:
            file.write(''.join(book_parts[i]))
toc_file_id = datetime.now() - timedelta(seconds=3)
with codecs.open(f'/Users/qq/Dropbox/Obsidian/{toc_file_id.strftime("%Y%m%d%H%M%S")}.md', 'w', encoding='utf-8') as file:
        file.write(''.join(toc_file))

#modifing Book zettel with link to toc file of the book
book_zettel = []
with open(path_to_book_zettel, 'r', encoding='utf-8') as file:
    book_zettel.extend(file)
line_to_insert = 0
for i in range(len(book_zettel)):
    if not re.search(r'- ', book_zettel[i]) is None:
        line_to_insert = i + 1
new_book_zettel = book_zettel[:line_to_insert]
new_book_zettel.append(f'- {name_of_book} [[{toc_file_id.strftime("%Y%m%d%H%M%S")}]]\n')
new_book_zettel.extend(book_zettel[line_to_insert:])
with codecs.open(path_to_book_zettel, 'w', encoding='utf-8') as file:
    file.write(''.join(new_book_zettel))
