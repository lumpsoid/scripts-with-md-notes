import os  # чтобы получить лист названия файлов
import re  # regex
import codecs  # чтобы сохранять данные в utf-8 (русский язык)
from tkinter import Tk

# скопировать из клипборда
r = Tk()
r.withdraw()
clipboard = r.clipboard_get()
r.update() # now it stays on the clipboard after the window is closed
r.destroy()

def difference(list1, list2):
   list_dif = [i for i in list1 + list2 if i not in list1 or i not in list2]
   return list_dif

search_for_it = re.sub('.md', '', clipboard)  # id который нужно искать в файлах

zettel_backlinks = []

with os.scandir('C:\\Users\\mmgee\\Dropbox\\Obsidian') as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file():
            file_path = 'C:\\Users\\mmgee\\Dropbox\\Obsidian\\' + entry.name
            # поиск id в других файлах
            with open(file_path, 'r', encoding='utf-8') as searchfile:
                for line in searchfile:
                    if re.search(rf'\[\[{search_for_it}\]\]', line, re.M|re.I):
                        zettel_backlinks.append(re.sub('.md', '', entry.name))
# проверка на наличие этих бэклинков в начальном файле
links_in_file = []
with open(f'C:\\Users\\mmgee\\Dropbox\\Obsidian\\{clipboard}', 'r', encoding='utf-8') as f:
    for line in f:
        if re.search('\[\[[0-9]+\]\]', line, re.M|re.I):
            links_in_file.append(re.search('[0-9]+', line).group(0))
# удаляем повторения в целевом листе и получаем хеадер
for i in links_in_file:
    try:
        zettel_backlinks.remove(i)
    except:
        pass
# находим хеадеры и формируем линки
end_list = []
for i in zettel_backlinks:
    with open(f'C:\\Users\\mmgee\\Dropbox\\Obsidian\\{i}.md', 'r', encoding='utf-8') as f:
        first_line = f.readline().rstrip('\n')
        first_line = re.sub('#\s', '', first_line)
        end_list.append(f'{first_line} [[{i}]]\n')
# export
r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(end_list)
r.update() # now it stays on the clipboard after the window is closed
r.destroy()