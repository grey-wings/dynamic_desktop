# -*- coding: utf-8 -*-
import os
import sys
import win32gui

if __name__ == "__main__":
    hwnd = win32gui.FindWindow("Progman", "Program Manager")
    print(hwnd)