import os
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
parentDir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
widget_class = uic.loadUiType(os.path.join(parentDir, "UI/image_list_widget.ui"))[0]

class ImageListWidget(QWidget, widget_class):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self._loadUiInit()
        self._setEvent()

    def _loadUiInit(self):

        '''
        UI 초기화
        :return: None
        '''
        self.image_list.hideColumn(1)
        pass

    def _setEvent(self):
        '''
        Event 설정
        :return: None
        '''
        #self.image_list.currentItemChanged.connect(self.itemChanged)
        pass

    def setCurrentItemChanged(self, func):
        '''
        main에서 currentItemChanged를 설정하기 위한 함수
        :param func:
        :return:
        '''
        self.image_list.currentItemChanged.connect(func)

    def addImage(self, filePath):
        newItem = QTreeWidgetItem(self.image_list)
        fileName = filePath.split("/")[-1]
        newItem.setText(0, fileName)
        newItem.setText(1, filePath)

    def addImages(self, filePaths):
        for filePath in filePaths:
            fileName = filePath.split("/")[-1]
            newItem = QTreeWidgetItem(self.image_list)
            newItem.setText(0, fileName)
            newItem.setText(1, filePath)

    def addFolder(self, path):
        parentItem = QTreeWidgetItem(self.image_list)
        parentItem.setText(0, path.split("/")[-1])
        parentItem.setText(1, path)
        if path:
            for element in os.listdir(path):
                item = QTreeWidgetItem(parentItem, [element, path+"/"+element])