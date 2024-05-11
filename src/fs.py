from ctypes import windll
import win32gui
user32 = windll.user32
user32.SetProcessDPIAware() # optional, makes functions return real pixel numbers instead of scaled values

max_y = user32.GetSystemMetrics(1)

# Compares if current height of screen is equal to max_height of screen
def is_full_screen():
    try:
        hWnd = user32.GetForegroundWindow()
        _,_,_,y = win32gui.GetWindowRect(hWnd)
        return y == max_y
    except:
        return False
