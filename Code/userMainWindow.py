import os
import sys
from subprocess import call
from cv2 import VideoCapture, cvtColor, COLOR_BGR2RGB
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QSystemTrayIcon, \
    QAction, QMenu, QMessageBox
import mainWindow


class MainWindow(QMainWindow):

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, '提示',
                                               "是否要退出程序？",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

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
        print('最大化：{}'.format(big))
        if not big:
            self.setWindowState(Qt.WindowMaximized)
            big = True
        elif big:
            self.setWindowState(Qt.WindowNoState)
            big = False

    def mini(self):

        self.showMinimized()


class userUI(QtWidgets.QMainWindow, mainWindow.Ui_MainWindow):
    path = ''
    timer_camera = QTimer()

    def __init__(self, parent=None):
        super(userUI, self).__init__(parent)
        self.setupUi(self)
        self.icon_quit()

        self.resize(675, 590)
        self.setWindowFlags(Qt.FramelessWindowHint)
        # 去掉窗口边框，不在任务栏显示图标
        self.toolButton.clicked.connect(self.openmp4)
        self.minimizeButton.clicked.connect(self.mini)
        self.applyButton.clicked.connect(self.play)
        self.closeButton.clicked.connect(self.quitApp)

    def icon_quit(self):
        self.mini_icon = QSystemTrayIcon(self)  # 为应用程序在系统托盘中提供一个图标
        self.mini_icon.setIcon(QIcon('./favicon.ico'))
        quit_menu = QAction('退出软件', self, triggered=self.quitApp)
        quit_menu2 = QAction('关闭壁纸', self, triggered=self.close_wall)
        quit_menu3 = QAction('主界面', self, triggered=self.normal_window)
        tpMenu = QMenu(self)
        tpMenu.setStyleSheet("background:#222225;color:white")
        tpMenu.addAction(quit_menu3)
        tpMenu.addAction(quit_menu2)
        tpMenu.addAction(quit_menu)
        self.mini_icon.showMessage('动态桌面', '打开动态桌面软件', icon=QSystemTrayIcon.NoIcon)
        self.mini_icon.setContextMenu(tpMenu)  # 设置右键菜单
        self.mini_icon.show()
        # self.mini_icon.messageClicked.connect(self.message)
        self.mini_icon.activated.connect(self.act)

    def act(self, reason):
        if reason == 2 or reason == 3:
            self.normal_window()

    def mini(self):
        self.showMinimized()
        self.mini_icon.show()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)

    def normal_window(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.showNormal()

    def quitApp(self):
        self.close_wall()
        sys.exit()

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
            self.path, filetype = QFileDialog.getOpenFileName(None, "选择文件", '.',
                                                              "视频文件(*.AVI;*.mov;*.rmvb;*.rm;*.FLV;"
                                                              "*.mp4;*.3GP)")
            # ;;All Files (*)
            if self.path == "":  # 未选择文件
                return

            self.slotStart()
            # t = Thread(target=self.Stop)
            # t.start()  # 启动线程，即让线程开始执行
        except Exception as e:
            print(e)

    def play(self):
        if self.path == '':
            reply = QtWidgets.QMessageBox.question(self, '提示',
                                                   "未加载选择视频",
                                                   QtWidgets.QMessageBox.Yes)
            return
        with open("./filename.txt", 'w', encoding='utf-8') as f:
            f.truncate(0)
            print(f.write(str(self.path)))
        try:
            try:
                call(r'taskkill /F /IM myplay.exe')  # /F强制终止；/IM表示指定的进程名称
            except:
                pass
            os.system(r'start myplay.exe')
            # 执行命令行
        except:
            pass
        try:
            if self.cap:
                self.cap.release()
                self.timer_camera.stop()  # 停止计时器
            else:
                Warming = QMessageBox.warning(self, "Warming", "Push the left upper corner button to Quit.",
                                              QMessageBox.Yes)
        except:
            pass

    def close_wall(self):
        try:
            call('taskkill /F /IM play.exe')
        except:
            pass

    def close(self):
        self.hide()
        self.mini_icon.showMessage('动态壁纸', '动态壁纸已经最小化到系统托盘', QIcon('./2.ico'))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = userUI()
    win.show()
    sys.exit(app.exec_())
