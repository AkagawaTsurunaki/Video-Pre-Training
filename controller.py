import pyautogui as pg

pg.PAUSE = 0

def minerl_action_to_env(minerl_action: dict):
    
    def bind_mouse(action: str, button: str):
        if minerl_action[action] == 1:
            pg.mouseDown(button=button, duration=1)
        else:
            pg.mouseUp(button=button, duration=1)

    def bind_key(action: str, key: str):
        if minerl_action[action] == 1:
            pg.keyDown(key=key)
        elif minerl_action[action] == 0:
            pg.keyUp(key=key)


    bind_mouse(action="attack", button="left")
    bind_key(action="back", key="s")
    bind_key(action="forward", key="w")
    bind_key(action="jump", key="space")
    bind_key(action="left", key="a")
    bind_key(action="right", key="d")
    bind_key(action="sneak", key="shift")
    bind_key(action="sprint", key="ctrl")
    bind_mouse(action="use", button="right")
    bind_key(action="drop", key="q")
    bind_key(action="inventory", key="e")
    for i in range(1, 10):
        bind_key(action=f"hotbar.{i}", key=f"f{i}")

    x_offset = minerl_action["camera"][0][0]
    y_offset = minerl_action["camera"][0][1] 
    pg.moveRel(xOffset=x_offset, yOffset=y_offset)