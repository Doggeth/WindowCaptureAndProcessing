import win32gui
import win32ui
from ctypes import windll
import numpy as np
import re


# Return list of windows hwnd (handle to a window) and titles
def get_window_names():

    def window_info(hwnd, results):
        title = win32gui.GetWindowText(hwnd)
        if title: results.append((hwnd,title))

    windows_info = []
    win32gui.EnumWindows(window_info, windows_info)

    return windows_info


# Return titles matching pattern
def match_titles(windows: list[tuple], pattern: re.Pattern):
    return [window for window in windows if re.match(pattern, window[1])]


# Get bitmap from window
def capture_window(hwnd):
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    width = right - left
    height = bottom - top

    win_dc_handle = win32gui.GetWindowDC(hwnd)
    win_dc = win32ui.CreateDCFromHandle(win_dc_handle)
    mem_dc = win_dc.CreateCompatibleDC()

    img_bitmap = win32ui.CreateBitmap()
    img_bitmap.CreateCompatibleBitmap(win_dc, width, height)
    mem_dc.SelectObject(img_bitmap)

    windll.user32.PrintWindow(hwnd, mem_dc.GetSafeHdc(),2)

    bmp_info = img_bitmap.GetInfo()
    bmp_data = img_bitmap.GetBitmapBits(True)
    img_array = np.frombuffer(bmp_data, dtype=np.uint8).reshape(bmp_info["bmHeight"], bmp_info["bmWidth"], 4)

    win_dc.DeleteDC()
    mem_dc.DeleteDC()
    win32gui.ReleaseDC(hwnd, win_dc_handle)
    win32gui.DeleteObject(img_bitmap.GetHandle())

    return img_array



