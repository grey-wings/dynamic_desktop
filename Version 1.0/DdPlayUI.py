# -*- coding: utf-8 -*-
from os.path import exists as os_path_exists
from os.path import abspath
from sys import exit as sysexit
from sys import argv as sysargv

from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from win32gui import FindWindow, FindWindowEx, SendMessageTimeout, SetParent
from qt_uis.mainWindow import Ui_MainWindow

"""
动态桌面执行程序，用于生成exe
"""


class videoPlayWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(videoPlayWindow, self).__init__(parent)

        super().__init__(parent)
        self.setupUi(self)
        self.workW2 = self.pretreatmentHandle()
        self.player = QMediaPlayer(flags=QMediaPlayer.VideoSurface)
        # self.player.setNotifyInterval(10000)
        self.player.setVideoOutput(self.videowidget)
        # self.player.setMuted(bool(1 - self.player.isMuted()))
        self.player.setMuted(True)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 去掉窗口边框
        self.go()

    def go(self):
        # self.ui.videowidget.setFullScreen(True)
        self.setMaximumWidth(1920)
        self.setMaximumHeight(1080)
        self.setGeometry(0, 0, 1920, 1080)
        # self.ui.videowidget.setGeometry(0, 0, 1920, 1030)
        # self.ui.videowidget.raise_()
        self.videowidget.setGeometry(0, 0, 1920, 1080)
        self.videowidget.raise_()

        with open(abspath("./filename.txt"), 'r', encoding='utf-8') as f:
            file_name = f.read()
            if file_name == '':
                file_name = 'lkf.mp4'
        print(file_name)
        if not os_path_exists(file_name):
            sysexit()

        media = QMediaContent(QUrl(file_name))
        self.player.setMedia(media)

        self.mplayList = QMediaPlaylist()
        self.mplayList.addMedia(QMediaContent(QUrl.fromLocalFile(file_name)))
        self.player.setPlaylist(self.mplayList)
        self.mplayList.setPlaybackMode(QMediaPlaylist.CurrentItemInLoop)

        win_hwnd = int(self.winId())
        video_h = int(self.videowidget.winId())
        SetParent(win_hwnd, self.workW2)  # 将参数2设为参数1的父亲
        SetParent(video_h, self.workW2)
        SetParent(video_h, win_hwnd)

        self.player.play()

    def pretreatmentHandle(self):
        """

        :return: hwnd_WorkW_next: 动态桌面播放窗口需要挂的父窗口
        """
        hwnd = FindWindow("Progman", "Program Manager")  # 句柄值会变
        SendMessageTimeout(hwnd, 0x052C, 0, None, 0, 0x03E8)
        hwnd_WorkW = None
        hwnd_WorkW_next = None
        # WorkW有很多个，需要寻找挂着SHELLDLL_DefView的WorkW的下一个窗口
        while 1:
            # 寻找Z序在hwnd_Window之后的一个WorkerW窗口
            hwnd_WorkW = FindWindowEx(None, hwnd_WorkW, "WorkerW", None)
            # print('hwmd_workw: ', hwnd_WorkW)
            if not hwnd_WorkW:
                continue
            hView = FindWindowEx(hwnd_WorkW, None, "SHELLDLL_DefView", None)
            # print('hwmd_hView: ', hView)
            if not hView:
                continue
            h = FindWindowEx(None, hwnd_WorkW, "WorkerW", None)
            if h:
                hwnd_WorkW_next = h
                # while h:
                #     SendMessage(h, 0x0010, 0, 0)  # WM_CLOSE
                #     # 把挂着SHELLDLL_DefView的WorkW之后的所有workerW全部关掉
                #     h = FindWindowEx(None, hwnd_WorkW, "WorkerW", None)
                #     # print(h)
            break
        return hwnd_WorkW_next


if __name__ == "__main__":
    app = QApplication(sysargv)
    myWin = videoPlayWindow()
    myWin.show()
    sysexit(app.exec_())
