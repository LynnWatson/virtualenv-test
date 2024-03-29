import cv2
import sys
import numpy as np
import matplotlib

matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from PyQt5 import QtWidgets, QtGui, QtCore
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
        self.chooseImgBtn.clicked.connect(self.chooseImgBtn_clicked)
        self.histBtn.clicked.connect(self.histBtn_clicked)
        self.otsuBtn.clicked.connect(self.otsuBtn_clicked)
        self.entBtn.clicked.connect(self.entBtn_clicked)
        self.threshSlider = 1  # 图片放缩尺度
        self.tab3.setWhatsThis("联系方式")

    def load_image(self):
        # 加载图片，QFileDialog就是系统对话框的那个类,得到的是文件路径
        # 第一个参数是上下文，第二个参数是弹框的名字，第三个参数是开始打开的路径，第四个参数是需要的格式
        src, _ = QFileDialog.getOpenFileName(self, '加载源图', 'F:\picture for lhr\\', 'Image files(*.jpg *.gif *.png)')

        # 使用OpenCV转换为灰度图
        global grayImg
        grayImg = cv2.imread(src, cv2.IMREAD_GRAYSCALE)  # 读取图片，第二个参数表示以灰度图像读入
        # print(img.shape)

    def show_image(self, img):
        # 提取图像的尺寸，用于将OpenCV下的grayImg转换成Qimage
        width = img.shape[1]  # 获取图像尺寸
        height = img.shape[0]
        frame = QImage(img, width, height, QImage.Format_Grayscale8)  # 图像是使用一个8位灰度格式存储

        # 创建图元和场景，显示图片
        # pix = QPixmap.fromImage(frame)  # 下面的语句都可以
        pix = QPixmap(frame)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        # self.view.setScene(self.scene)  # 将场景添加至视图,每个场景单独写这句代码

    def chooseImgBtn_clicked(self, remark):
        # print(remark)
        self.show_image(grayImg)
        self.sourceView.setScene(self.scene)  # 将场景添加至视图

    def histBtn_clicked(self):
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

    def otsuBtn_clicked(self):
        otsuThresh, otsuImg = cv2.threshold(grayImg, 0, 255, cv2.THRESH_OTSU)
        # cv2.imshow("gray", grayImg)
        print('otsuThresh is ', otsuThresh)  # 后面需要显示在界面上面!!!
        # self.otsuThreshlb.setText(otsuThresh)
        self.show_image(otsuImg)
        self.otsuView.setScene(self.scene)  # 将场景添加至视图

    def entBtn_clicked(self):
        self.entropyView.setScene(self.scene)  # 将场景添加至视图
        entThresh, entImg = self.max_entropy_segmentation(grayImg)
        # cv2.imshow("dst", entImg)
        print('entThresh is ', entThresh)
        self.show_image(entImg)
        self.entropyView.setScene(self.scene)  # 将场景添加至视图

    # 最大熵阈值分割 - 计算当前熵
    def calculate_current_entropy(self, hist, threshold):
        data_hist = hist.copy()
        background_sum = 0.
        target_sum = 0.
        for i in range(256):
            if i < threshold:  # 累积背景
                background_sum += data_hist[i]
            else:  # 累积目标
                target_sum += data_hist[i]
        background_ent = 0.
        target_ent = 0.
        for i in range(256):
            if i < threshold:  # 计算背景熵
                if data_hist[i] == 0:
                    continue
                ratio1 = data_hist[i] / background_sum
                background_ent -= ratio1 * np.log2(ratio1)
            else:
                if data_hist[i] == 0:
                    continue
                ratio2 = data_hist[i] / target_sum
                target_ent -= ratio2 * np.log2(ratio2)
        return target_ent + background_ent

    # 最大熵阈值分割 - 遍历计算最大熵
    def max_entropy_segmentation(self, img):
        channels = [0]
        hist_size = [256]
        prange = [0, 256]
        hist = cv2.calcHist(img, channels, None, hist_size, prange)
        hist = np.reshape(hist, [-1])
        max_ent = 0.
        max_index = 0
        for i in range(256):
            cur_ent = self.calculate_current_entropy(hist, i)
            if cur_ent > max_ent:
                max_ent = cur_ent
                max_index = i
        entThresh, entImg = cv2.threshold(grayImg, max_index, 255, cv2.THRESH_BINARY)
        return entThresh, entImg


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
