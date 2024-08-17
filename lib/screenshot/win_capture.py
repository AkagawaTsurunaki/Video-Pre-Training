import pyautogui
import pygetwindow as gw
from PIL.Image import Image


def capture(name: str) -> Image:
    # 获取窗口
    win_list = gw.getWindowsWithTitle(name)
    assert len(win_list) != 0, f'无法捕获窗口：找不到 {name}'
    w = win_list[0]
    # 激活窗口
    w.activate()
    # 计算屏幕位置
    region = (w.centerx, w.centery, w.height, w.width)

    # 截图
    assert hasattr(pyautogui, "screenshot")
    # 注意: 如果出现找不到 screenshot 的问题, 请尝试更新 pyautogui 库
    img = pyautogui.screenshot(region=region)
    return img

