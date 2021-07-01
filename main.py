import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import *
from widgets.canvas_widget import CanvasWidget
from widgets.image_list_widget import ImageListWidget
from config import get_config

from libs.version import __version__

__appname__ = 'Image Viewer'
form_class = uic.loadUiType("UI/image_viewer_main.ui")[0]

class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._initData()
        self._loadUiInit()
        self._setEvent()

    def _initData(self):
        '''
        Data 초기화
        :return:
        '''
        self._config = get_config()
        pass

    def _loadUiInit(self):
        '''
        UI 초기화
        :return: None
        '''
        self.setWindowTitle("{title} ({version})".format(title=__appname__, version=__version__))
        self.image_list_widget = ImageListWidget()
        self.canvas_widget = CanvasWidget()
        self.layout_canvas_layout_hbox = QHBoxLayout()
        self.layout_canvas_layout_hbox.addWidget(self.image_list_widget)
        self.layout_canvas_layout_hbox.addWidget(self.canvas_widget)
        self.layout_canvas_layout_hbox.setStretch(1, 3)
        self.layout_canvas.addLayout(self.layout_canvas_layout_hbox, 1, 1)
        pass


    def _setEvent(self):
        '''
        Event 설정
        :return: None
        '''
        self.action_openFile.triggered.connect(self.openFile)            # 메뉴바 - Open File
        self.action_openFile_2.triggered.connect(self.openFile)            # File - Open File
        self.action_openFiles.triggered.connect(self.openFiles)            # File - Open Files
        self.action_openFolder.triggered.connect(self.openFolder)          # File - Open Folder
        self.image_list_widget.setCurrentItemChanged(self.loadImage)
        pass

    def loadImage(self, current):
        '''
        canvase_widget에 이미지 Load
        :param current: TreeWidget에서 현재 선택된 Item
        :return: None
        '''
        print(current.text(0), current.text(1))
        path = current.text(1) # 파일 경로
        self.canvas_widget.setImage(path)

    def openFile(self):
        if self._config["debug"]:
            print('Debug : Open File')
        filePathTuple = QFileDialog.getOpenFileName(self, "Open File", "", "Images (*.png *.xpm *.jpg)")
        filePath = filePathTuple[0]
        if filePath:
            self.image_list_widget.addImage(filePath)
        #QMessageBox.information(self, "Open File", "Open file event")

    def openFiles(self):
        if self._config["debug"]:
            print('Debug : Open Files')
        filePathsTuple = QFileDialog.getOpenFileNames(self, "Open Files", "", "Images (*.png *.xpm *.jpg)")
        filePaths = filePathsTuple[0]
        self.image_list_widget.addImages(filePaths)

    def openFolder(self):
        if self._config["debug"]:
            print('Debug : Open Folder')
        dirName = QFileDialog.getExistingDirectory(self, 'Open Folder')
        self.image_list_widget.addFolder(dirName)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    exit(app.exec_())