import pyautogui as pg
import numpy as np
import torch as th
from wmctrl import activate_window
from xwininfo import xwininfo

def capture(name="Minecraft 1.21.1 - 单人游戏") -> th.Tensor:
    activate_window(name=name)
    wininfo = xwininfo(name=name)
    top = wininfo.absolute_upper_left_x
    left = wininfo.absolute_upper_left_y
    width = wininfo.width
    height = wininfo.height
    img = pg.screenshot(region=(top, left, width, height))
    img_np = np.array(img)
    img_tensor = th.from_numpy(img_np).permute(2, 0, 1).float()
    # Channels Height Width
    return img_tensor

import time

time.sleep(1)
capture()