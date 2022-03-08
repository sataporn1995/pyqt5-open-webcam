from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap, QImage
import sys
import cv2
from PyQt5.QtCore import Qt
import numpy as np
from PyQt5.uic import loadUi

import imutils


class WindowApp(QMainWindow):
    def __init__(self):
        super(WindowApp, self).__init__()
        loadUi('mainwindow.ui', self)

        self.state = False

        self.openCamera.clicked.connect(self.webcame)
        self.stopCamera.clicked.connect(self.stop)

    def stop(self):
        self.state = True
        sys.exit(app.exec_())

    def webcame(self):
    	video = cv2.VideoCapture(0)

    	while(video.isOpened()):
    		ret, frame = video.read()
    		resized = imutils.resize(frame.copy() ,height = 480 )

    		self.setImage(self.lblImage, resized)
    		cv2.waitKey(1)
    		if self.state:
    			break

    	video.release()

    def setImage(self, box, img):
        qformat = QImage.Format_Indexed8
        if len(img.shape) == 3:
            if(img.shape[2]) == 4:
                qformat = QImage.Format_RGBA888
            else:
                qformat = QImage.Format_RGB888
        h, w = img.shape[:2]
        img = QImage(img, w, h, qformat)
        img = img.rgbSwapped()
        box.setPixmap(QPixmap.fromImage(img))
        box.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WindowApp()
    window.show()
    app.exec_()
