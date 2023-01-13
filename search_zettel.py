import sys
#from PyQt4.QtGui  import *
#from PyQt4.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *

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


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
    def initUI(self):
        
        self.le_search = QLineEdit()                            # self.   +++
        self.searchbar.textChanged.connect(self.update_display)
        
        se_btn    = QPushButton("Search")
        se_btn.clicked.connect(self.find_item)
        
        self.listwidget = QListWidget()
        self.total_list = zettel_list
        self.listwidget.addItems(self.total_list)        

        hbox      = QHBoxLayout()        
        hbox.addWidget(self.le_search)                          # self.   +++
        hbox.addWidget(se_btn)
        
        auto_search_vbox = QVBoxLayout(self)
        auto_search_vbox.addLayout(hbox)
        auto_search_vbox.addWidget(self.listwidget)

    def find_item(self):
#        out = self.listwidget.findItems("mac", QtCore.Qt.MatchExactly)          # ---
#        out = self.listwidget.findItems(self.le_search.text(), Qt.MatchExactly)  
        out = self.listwidget.findItems(self.le_search.text(), 
                                        Qt.MatchContains)      # +++
        
        print("out->", [ i.text() for i in out ] ) 
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())