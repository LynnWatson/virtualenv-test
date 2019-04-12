import cv2
import sys
import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from MainWindow import Ui_MainWindow


class MainCode(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainCode, self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle('图像处理软件')  # 窗口名字
        self.chooseImgBtn.clicked.connect(self.load_image)  # 一定要绑定这个信号，否则全局变量不能用
        self.chooseImgBtn.clicked.connect(self.onchooseImgBtnClicked)  # 信号函数的命名？？？
        self.histBtn.clicked.connect(self.onhistBtnClicked)
        self.binaryBtn.clicked.connect(self.onbinaryBtnClicked)
        self.zoomscale = 1  # 图片放缩尺度

    def load_image(self):
        # 加载图片，QFileDialog就是系统对话框的那个类
        # 第一个参数是上下文，第二个参数是弹框的名字，第三个参数是开始打开的路径，第四个参数是需要的格式
        src, _ = QFileDialog.getOpenFileName(self, '加载源图', 'F:\picture for lhr\\', 'Image files(*.jpg *.gif *.png)')

        # 使用OpenCV转换为灰度图
        global grayImg
        grayImg = cv2.imread(src, cv2.IMREAD_GRAYSCALE)  # 读取图片，第二个参数表示以灰度图像读入
        # print(img.shape)

    def onchooseImgBtnClicked(self, remark):
        # print(remark)
        # 提取图像的尺寸，用于将OpenCV下的grayImg转换成Qimage
        width = grayImg.shape[1]  # 获取图像尺寸
        height = grayImg.shape[0]
        frame = QImage(grayImg, width, height, QImage.Format_Grayscale8)  # 图像是使用一个8位灰度格式存储

        # 创建图元和场景，显示图片
        # pix = QPixmap.fromImage(frame)  # 下面的语句都可以
        pix = QPixmap(frame)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.sourceView.setScene(self.scene)  # 将场景添加至视图

    def onhistBtnClicked(self):
        # self.histView.setScene(self.scene)
        # 参数:原图像 通道[0]-灰度图 掩码 BINS为256 像素范围0-255
        hist = cv2.calcHist(grayImg, [0], None, [256], [0, 255])
        # print(type(hist))
        # print(hist.size)
        # print(hist.shape)
        # print(hist)
        # plt.plot(hist)
        # plt.show()

        # 第五步：定义MyFigure类的一个实例
        self.F = MyFigure(width=4, height=3, dpi=100)
        self.F.axes.plot(hist)
        self.F.fig.suptitle("hist")

        # 第六步：在GUI的QGraphicsView视图窗口显示图形
        self.scene = QGraphicsScene()  # 创建一个场景
        self.scene.addWidget(self.F)  # 将图形元素添加到场景中
        self.histView.setScene(self.scene)  # 将创建添加到图形视图显示窗口
        self.histView.show()

    def onbinaryBtnClicked(self):
        print('2')
        threshVal, dst = cv2.threshold(grayImg, 0, 255, cv2.THRESH_OTSU)
        # cv2.imshow("gray", grayImg)
        # cv2.imshow("dst", dst)
        # cv2.waitKey(0)
        print(threshVal)
        width = dst.shape[1]  # 获取图像尺寸
        height = dst.shape[0]
        frame = QImage(dst, width, height, QImage.Format_Grayscale8)  # 图像是使用一个8位灰度格式存储
        pix = QPixmap(frame)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.binaryView.setScene(self.scene)  # 将场景添加至视图

class MyFigure(FigureCanvas):
    def __init__(self, width=5, height=4, dpi=100):
        # 第一步：创建一个创建Figure
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        # 第二步：在父类中激活Figure窗口
        super(MyFigure, self).__init__(self.fig)  # 此句必不可少，否则不能显示图形/# 初始化父类
        # 第三步：创建一个子图，用于绘制图形用，111表示子图编号，如matlab的subplot(1,1,1)
        self.axes = self.fig.add_subplot(111)
        # 第四步：就是画图，【可以在此类中画，也可以在其它类中画】


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainCode()
    mainWindow.show()
    sys.exit(app.exec_())
