from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys

import os  # чтобы получить лист названия файлов
import re  # regex
import json  # для экспорта
import codecs  # чтобы сохранять данные в utf-8 (русский язык)

zettel_list = []
# рабочая версия
with os.scandir('C:\\Users\\mmgee\\Dropbox\\Obsidian') as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file():
            # забор первой строки
            file_path = 'C:\\Users\\mmgee\\Dropbox\\Obsidian\\' + entry.name
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

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)

        # auto complete options                                                 
        names = ['пирог', 'Пирог']
        self.completer = QCompleter(names)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)

        # create line edit and add auto complete                                
        self.lineedit = QLineEdit()
        self.lineedit.setCompleter(self.completer)
        layout.addWidget(self.lineedit, 0, 0)

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())