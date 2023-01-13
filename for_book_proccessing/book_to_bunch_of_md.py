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
        if not re.search('{name_of_book}', parts[i]) is None:
            parts[i] = parts[i] + f' [[{chapters.get(parts[i])}]]\n'  # adding links