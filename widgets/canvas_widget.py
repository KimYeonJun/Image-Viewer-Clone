import os
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
parentDir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
widget_class = uic.loadUiType(os.path.join(parentDir, "UI/canvas_widget.ui"))[0]

class CanvasWidget(QWidget, widget_class):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self._loadUiInit()
        self._setEvent()

    def _loadUiInit(self):
        '''
        UI 초기화
        :return: None
        '''
        pass


    def _setEvent(self):
        '''
        Event 설정
        :return: None
        '''
        pass

    def setImage(self, path):
        ext = path.split(".")[-1].lower()
        if ext == 'jpg' or ext=='png':
            qPixmapOrigin = QPixmap()
            qPixmapOrigin.load(path)
            self.lbl_image.setPixmap(qPixmapOrigin.scaled(self.lbl_image.width(), self.lbl_image.height(), Qt.KeepAspectRatio))




if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    canvas_widget = CanvasWidget()
    canvas_widget.show()
    exit(app.exec_())