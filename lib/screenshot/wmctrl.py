import subprocess


def activate_window(name: str):
    # You need to install wmctrl if it dose not work.
    command = f'wmctrl -a "{name}"'
    result = subprocess.check_output(command, shell=True, executable="/bin/bash")
    result = result.decode('utf-8')
    return result
