import pyautogui as pg

pg.PAUSE = 0


def bind_mouse(minerl_action: dict, action: str, button: str):
    if minerl_action[action] == 1:
        pg.mouseDown(button=button)
    else:
        pg.mouseUp(button=button)


def bind_key(minerl_action: dict, action: str, key: str):
    if minerl_action[action] == 1:
        pg.keyDown(key=key)
    elif minerl_action[action] == 0:
        pg.keyUp(key=key)


def minerl_action_to_env(minerl_action: dict):
    bind_mouse(minerl_action=minerl_action, action="attack", button="left")
    bind_key(minerl_action=minerl_action, action="back", key="s")
    bind_key(minerl_action=minerl_action, action="forward", key="w")
    bind_key(minerl_action=minerl_action, action="jump", key="space")
    bind_key(minerl_action=minerl_action, action="left", key="a")
    bind_key(minerl_action=minerl_action, action="right", key="d")
    bind_key(minerl_action=minerl_action, action="sneak", key="shift")
    bind_key(minerl_action=minerl_action, action="sprint", key="ctrl")
    bind_mouse(minerl_action=minerl_action, action="use", button="right")
    bind_key(minerl_action=minerl_action, action="drop", key="q")
    bind_key(minerl_action=minerl_action, action="inventory", key="e")
    for i in range(1, 10):
        bind_key(minerl_action=minerl_action, action=f"hotbar.{i}", key=f"f{i}")

    x_offset = minerl_action["camera"][0][0]
    y_offset = minerl_action["camera"][0][1]
    k = 30.0
    pg.moveRel(xOffset=x_offset * k, yOffset=y_offset * k)
