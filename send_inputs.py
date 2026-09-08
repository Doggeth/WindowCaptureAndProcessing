import pydirectinput
import ctypes
import win32gui
import time

user32 = ctypes.windll.user32

def mouse_click(title: str):
    cur_hwnd = win32gui.GetForegroundWindow()
    cur_child = win32gui.FindWindowEx(cur_hwnd, 0, "Edit", None)

    user32.BlockInput(True)
    start_x, start_y = pydirectinput.position()
    pydirectinput.moveTo(500,500)
    pydirectinput.click()
    time.sleep(0.1)
    pydirectinput.mouseDown()
    pydirectinput.mouseUp()
    pydirectinput.moveTo(start_x, start_y)
    win32gui.SetForegroundWindow(cur_hwnd)
    win32gui.SetFocus(cur_child)
    user32.BlockInput(False)