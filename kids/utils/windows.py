import sys
import win32.win32gui as win32gui
import win32.win32process as win32process

windows = []

def get_all_windows():
    win32gui.EnumWindows(construct_windows_list, windows)
    return windows

def construct_windows_list(hwnd, strings): # checks to see if a window is visible if not it is skipped.
    if win32gui.IsWindowVisible(hwnd): # some apps like discord, still run in the background so this is disable for such cases.
        title = win32gui.GetWindowText(hwnd)#.split(" - ")[-1]
        short_title = win32gui.GetWindowText(hwnd).split(" - ")[-1]
        pid = get_window_pid(title)
        left, top, right, bottom = win32gui.GetWindowRect(hwnd) # was used to verify that the window actually had dimension or else it did not have a window
        if title and right - left and bottom - top and {"title": short_title, "pid": pid} not in strings:
            strings.append({"title": short_title, "pid": pid})   
    return True

def get_window_pid(title): # this returns  all  windows PID's
    hwnd = win32gui.FindWindow(None, title)
    _, pid = win32process.GetWindowThreadProcessId(hwnd)
    return pid
