
import time

import win32api
import win32con
import win32gui
from config import config as conf
from config import setting
from log import ACOLogger

# Params

log = ACOLogger()


# window.list

# 过滤可显示或允许窗口显示的窗口
def filter(hwnd, title):

    # log.logger.debug("\t\tfilter->\t%d\t%s", hwnd, title)
    if False == win32gui.IsWindowVisible(hwnd) or False == win32gui.IsWindowEnabled(hwnd):
        return False

    return True

# 过滤窗口的相关信息


def handler(hwnd, windows):

    # log.logger.debug("\t\thandler-> %d", hwnd)
    ps = windows
    p = []
    p.append(hex(hwnd))
    p.append(win32gui.GetClassName(hwnd))
    p.append(win32gui.GetWindowText(hwnd))
    if filter(hwnd, p[2]):
        # log.logger.debug("\t\thandler<-\t%d\t%s", hwnd, p)
        ps[hwnd] = p

# 输出窗口列表


def lst():
    windows = {}
    win32gui.EnumWindows(handler, windows)

    log.logger.info("list->\tsize= %d", len(windows))
    for p in windows:
        log.logger.debug("\tlist<-\t%s", windows[p])

    log.flush()

# window.close

# 过滤窗口名称


def filterTitle(hwnd):
    if 0 == hwnd:
        return False
    t = win32gui.GetWindowText(hwnd)
    for p in setting.titles:
        if t.startswith(p):
            return True
    return False


# 关闭窗口
def close(hwnd, idx):

    typeName = setting.types[idx]
    log.logger.debug("close->\t%s\t%s\t%s", hex(hwnd), idx, typeName)

    if 0 != hwnd:
        log.logger.info("close<-\t%s\t%s", hex(hwnd),
                        win32gui.GetWindowText(hwnd))
        try:
            win32gui.PostMessage(
                hwnd, win32con.WM_KEYDOWN, win32con.VK_ESCAPE, 0)
            win32gui.PostMessage(
                hwnd, win32con.WM_KEYUP, win32con.VK_ESCAPE, 0)
            # time.sleep(0.05)
        except Exception as e:
            log.logger.error("close.fail\t%s\t%s\t%s", typeName, e.args)
        else:
            log.logger.info("close\t%s", typeName)

# 递归搜索


def search(hwnd, lst):

    size = len(lst)
    if 0 == size:
        return hwnd

    for idx in range(size):
        claze = lst[idx]
        log.logger.debug("search->\t%s\t%s", hex(hwnd), claze)
        try:
            exHwnd = win32gui.FindWindowEx(hwnd, None, claze, None)
            log.logger.debug("search<-\t%s\t%s\t%s", hex(hwnd), claze, exHwnd)
            if 0 != exHwnd:
                hwnd = exHwnd
                log.logger.debug("search=\t%s\t%s\t%s", idx, claze, hwnd)
                return hwnd
        except Exception as e:
            log.logger.debug(
                "fail to findWindow(hwnd=%s, class=%s): %s", hwnd, className, str(e))

    return hwnd


# 监控
def handle():

    counter = 0
    while True:

        counter = counter + 1

        if conf.logList and counter % 100 == 1:
            lst()

        for idx in range(len(setting.classes)):
            className = [*setting.classes][idx]
            try:
                hwnd = win32gui.FindWindow(className, None)
                log.logger.debug("handle->\t%s\t%s", className, hex(hwnd))
                if filterTitle(hwnd):
                    log.logger.debug("handle<-\t%s\t%s", className, hex(hwnd))
                    win32gui.SetForegroundWindow(hwnd)
                    close(search(hwnd, setting.classes[className]), idx)
            except Exception as e:
                log.logger.debug(
                    "fail to findWindow(class=%s): %s", className, str(e))

        log.flush()
        time.sleep(int(conf.duration))
