import subprocess


def activate_window(name: str):
    command = f'wmctrl -a "{name}"'
    result = subprocess.check_output(command, shell = True, executable="/bin/bash")
    result = result.decode('utf-8')
    return result
