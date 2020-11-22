import sys
import win32.win32gui as win32gui
import win32.win32process as win32process


def get_all_windows():
    windows = []
    win32gui.EnumWindows(construct_windows_list, windows)
    return windows

def construct_windows_list(hwnd, strings): # checks to see if a window is visible if not it is skipped.
    #if win32gui.IsWindowVisible(hwnd): # some apps like discord, still run in the background so this is disable for such cases.
    title = win32gui.GetWindowText(hwnd)
    pid = get_window_pid(title)
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    if title and right - left and bottom - top:
        strings.append({"title": title, "pid": pid})
    return True

def get_window_pid(title): # this returns  all  windows PID's
    hwnd = win32gui.FindWindow(None, title)
    _, pid = win32process.GetWindowThreadProcessId(hwnd)
    return pid
