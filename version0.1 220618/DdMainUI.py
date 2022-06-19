from os import system as os_system
from sys import exit as sysexit
from sys import argv as sysargv
from subprocess import call
from cv2 import VideoCapture, cvtColor, COLOR_BGR2RGB
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap, QIcon
from PyQt5.QtWidgets import QFileDialog, QSystemTrayIcon, \
    QAction, QMenu, QMessageBox, QMainWindow, QApplication
from mainWindow import Ui_MainWindow

# 对于要生成exe文件的程序，应避免导入整个库，否则会打包这个库内的所有函数
# 补充：上面一句话针对pyinstaller，nuitka是不是这样不知道
# imports文件夹中是自己编写的py程序，这部分在nuitka打包中编译成C语言，库函数则不编译
# 由于ddplay.py中的videoPlayWindow类继承了本文件的userUI类，因此对本文件的改动需同样改动imports中的对应文件

isDebug = True  # 标记是否需要debug（是否在pycharm中调试），如果是则为True，相对路径定位会有区别


class DdMainUI(QMainWindow, Ui_MainWindow):
    path = ''
    timer_camera = QTimer()

    def __init__(self, parent=None):
        super(DdMainUI, self).__init__(parent)
        self.mini_icon = QSystemTrayIcon(self)  # 为应用程序在系统托盘中提供一个图标
        self.setupUi(self)
        self.icon_init()

        self.resize(675, 590)

        # self.msgbox = QMessageBox()
        # self.msgbox.setStyleSheet("background-color: #222225; color: white")

        # self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowSystemMenuHint |
        #                     Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)
        self.setWindowFlags(Qt.Tool | Qt.FramelessWindowHint | Qt.WindowSystemMenuHint)
        # 去掉窗口边框，不在任务栏显示图标
        self.toolButton.clicked.connect(self.openmp4)
        self.minimizeButton.clicked.connect(self.mini)
        self.applyButton.clicked.connect(self.play)
        self.closeButton.clicked.connect(self.quitApp)

    def icon_init(self):
        if isDebug:
            self.mini_icon.setIcon(QIcon('./favicon.ico'))
            # 上面这句在pycharm中debug用
        else:
            self.mini_icon.setIcon(QIcon('../../../favicon.ico'))
        menu_quit = QAction('退出软件', self)
        menu_quit.triggered.connect(self.quitApp)
        menu_closeDd = QAction('关闭壁纸', self)
        menu_closeDd.triggered.connect(self.close_wall)
        menu_main = QAction('主界面', self)
        menu_main.triggered.connect(self.normal_window)
        tpMenu = QMenu(self)
        tpMenu.setStyleSheet("background:#222225;color:white")
        tpMenu.addAction(menu_main)
        tpMenu.addAction(menu_closeDd)
        tpMenu.addAction(menu_quit)
        self.mini_icon.showMessage('动态桌面', '打开动态桌面软件', icon=QSystemTrayIcon.NoIcon)
        self.mini_icon.setContextMenu(tpMenu)  # 设置右键菜单
        self.mini_icon.show()
        # self.mini_icon.messageClicked.connect(self.message)
        self.mini_icon.activated.connect(self.act)

    def act(self, reason):
        if reason == 2 or reason == 3:
            self.normal_window()

    def normal_window(self):
        # self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowSystemMenuHint |
        #                     Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)
        self.setWindowFlags(Qt.Tool | Qt.FramelessWindowHint | Qt.WindowSystemMenuHint)
        # self.setWindowFlags(Qt.Tool)
        self.showNormal()
        self.setAttribute(Qt.WA_Mapped)

    def mini(self):
        # self.msgbox.question("确定要退出吗")
        self.stop_preview()
        self.showMinimized()
        self.mini_icon.show()
        # self.setWindowFlags(Qt.Tool | Qt.WindowStaysOnTopHint)

    def quitApp(self):
        self.close_wall()
        sysexit()

    def stop_preview(self):
        """
        停止桌面预览。
        :return:
        """
        try:
            if self.cap:
                self.cap.release()
                self.timer_camera.stop()  # 停止计时器
            else:
                Warming = QMessageBox.warning(self, "Warming", "Push the left upper corner button to Quit.",
                                              QMessageBox.Yes)
        except:
            pass

    def slotStart(self):
        videoName = self.path
        if videoName != "":  # “”为用户取消
            self.cap = VideoCapture(videoName)
            self.timer_camera.start(50)
            self.timer_camera.timeout.connect(self.openFrame)

    def openFrame(self):
        if self.cap.isOpened():

            ret, self.frame = self.cap.read()
            if ret:
                frame = cvtColor(self.frame, COLOR_BGR2RGB)
                # if self.detectFlag:
                #     # 检测代码self.frame
                #     self.label_num.setText("There are " + str(5) + " people.")
                height, width, bytesPerComponent = frame.shape
                bytesPerLine = bytesPerComponent * width
                q_image = QImage(frame.data, width, height, bytesPerLine,
                                 QImage.Format_RGB888).scaled(self.groupBox.width(),
                                                              self.groupBox.height(),
                                                              aspectRatioMode=Qt.KeepAspectRatioByExpanding)
                self.label.setPixmap(QPixmap.fromImage(q_image))
            else:
                self.cap.release()
                self.timer_camera.stop()

    def openmp4(self):
        try:
            # 下面第一个参数不能是None，否则有可能程序崩溃
            self.path, filetype = QFileDialog.getOpenFileName(self, "选择文件", '.',
                                                              "视频文件(*.AVI;*.mov;*.rmvb;*.rm;*.FLV;"
                                                              "*.mp4;*.3GP)")
            # ;;All Files (*)
            if self.path != "":  # 未选择文件
                self.slotStart()
            # t = Thread(target=self.Stop)
            # t.start()  # 启动线程，即让线程开始执行
        except Exception as e:
            print(e)

    def play(self):
        if self.path == '':
            # reply = QMessageBox.question(self, '提示',
            #                              "未加载选择视频",
            #                              QMessageBox.Yes)
            return
        with open("./filename.txt", 'w+', encoding='utf-8') as f:
            f.truncate(0)
            f.write(self.path)
        try:
            try:
                call(r'taskkill /F /IM ddplay.exe')  # /F强制终止；/IM表示指定的进程名称
            except:
                pass
            if isDebug:
                os_system(r'start ./release/ddplay/ddplay.dist/ddplay/ddplay.exe')
                # 上面这句在pycharm中debug用
            else:
                os_system(r'start ../../../ddplay/ddplay.dist/ddplay/ddplay.exe')
            # 执行命令行
        except:
            pass
        self.stop_preview()

    def close_wall(self):
        try:
            call('taskkill /F /IM ddplay.exe')
        except:
            pass

    # def close(self):
    #     self.hide()
    #     self.mini_icon.showMessage('动态壁纸', '动态壁纸已经最小化到系统托盘', QIcon('./2.ico'))

    # def closeEvent(self, event):
    #     reply = QMessageBox.question(self, '提示',
    #                                            "是否要退出程序？",
    #                                            QMessageBox.Yes | QMessageBox.No,
    #                                            QMessageBox.No)
    #     if reply == QMessageBox.Yes:
    #         event.accept()
    #     else:
    #         event.ignore()

    def mousePressEvent(self, event):
        global big
        big = False
        self.setWindowState(Qt.WindowNoState)
        self.m_flag = True
        self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
        event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        global big
        big = False
        self.setWindowState(Qt.WindowNoState)
        self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
        QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        global big
        big = False
        self.setWindowState(Qt.WindowNoState)
        self.m_flag = False

    def big(self):
        global big
        if not big:
            self.setWindowState(Qt.WindowMaximized)
            big = True
        elif big:
            self.setWindowState(Qt.WindowNoState)
            big = False


if __name__ == "__main__":
    app = QApplication(sysargv)
    win = DdMainUI()
    win.show()
    sysexit(app.exec_())
