import platform

import numpy as np
import pyautogui as pg
import torch as th

system = platform.system()


def capture(name="Minecraft 1.21.1 - 单人游戏", size=(128, 128)) -> th.Tensor:
    if system == "Linux":
        from lib.screenshot.xwininfo import xwininfo
        from lib.screenshot.wmctrl import activate_window
        activate_window(name=name)
        wininfo = xwininfo(name=name)
        top = wininfo.absolute_upper_left_x
        left = wininfo.absolute_upper_left_y
        width = wininfo.width
        height = wininfo.height
        img = pg.screenshot(region=(top, left, width, height))
    elif system == "Windows":
        from lib.screenshot.win_capture import capture
        img = capture(name)
    else:
        raise Exception("System not supported.")

    img = img.resize(size=size)
    img_np = np.array(img)
    img_tensor = th.from_numpy(img_np).unsqueeze(0).float()
    # [1, Height, Width, Channels]
    # [1,  128,    128,     3    ]
    return img_tensor
