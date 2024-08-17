import functools
import time
from pynput import keyboard
from pynput.keyboard import Key, KeyCode
from loguru import logger
import multiprocessing as mp
import threading


class KeyBoardInterruptListener:

    def __init__(self, exit_key: Key | KeyCode, max_pressed: int = 3, max_interval: float = 1.) -> None:
        self.exit_key = exit_key
        self.exit_flag = False
        self.on_press_event = threading.Event()
        self.times = 0
        self.last_pressed_time = None
        self.max_pressed = max_pressed
        self.max_interval = max_interval

    def on_press(self, key: Key | KeyCode):
        if isinstance(key, Key):
            if self.exit_key == key:
                now = time.time()
                if self.last_pressed_time is None:
                    self.last_pressed_time = now
                if now - self.last_pressed_time < self.max_interval:
                    self.times += 1
                else:
                    self.times = 0
                    self.last_pressed_time = now
                if self.times >= self.max_pressed:
                    self.exit_flag = True
                logger.warning(
                    f"Press {self.exit_key} for {self.max_pressed} times within {self.max_interval} second will terminate the process and exit the program.")
                self.on_press_event.set()


def listen_exit_key(exit_key: Key | KeyCode, max_pressed: int = 3, max_interval: float = 1.):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            keyboard_interrupt_listener = KeyBoardInterruptListener(exit_key=exit_key, max_pressed=max_pressed,
                                                                    max_interval=max_interval)
            keyboard_listener = keyboard.Listener(on_press=keyboard_interrupt_listener.on_press)
            with keyboard_listener:
                process = mp.Process(target=func, args=args, kwargs=kwargs)
                process.start()
                while True:
                    keyboard_interrupt_listener.on_press_event.wait()
                    keyboard_interrupt_listener.on_press_event.clear()
                    if keyboard_interrupt_listener.exit_flag:
                        process.kill()
                        raise KeyboardInterrupt()

        return wrapper

    return decorator
