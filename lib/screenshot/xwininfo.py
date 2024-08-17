from dataclasses import dataclass
import re
import subprocess, sys


def _run_xwininfo_cmd(name: str) -> str:
    command = f'xwininfo -name "{name}"'
    result = subprocess.check_output(command, shell=True, executable="/bin/bash")
    result = result.decode('utf-8')
    return result


# Regular expressions to extract the desired fields
_patterns = {
    'window_id': r'Window id:\s+([0x0-9a-fA-F]+)',
    'absolute_upper_left_x': r'Absolute upper-left X:\s+(\d+)',
    'absolute_upper_left_y': r'Absolute upper-left Y:\s+(\d+)',
    'relative_upper_left_x': r'Relative upper-left X:\s+(\d+)',
    'relative_upper_left_y': r'Relative upper-left Y:\s+(\d+)',
    'width': r'Width:\s+(\d+)',
    'height': r'Height:\s+(\d+)',
    'depth': r'Depth:\s+(\d+)',
    'visual': r'Visual:\s+([0x0-9a-fA-F]+)',
    'visual_class': r'Visual Class:\s+(\w+)',
    'border_width': r'Border width:\s+(\d+)',
    'colormap': r'Colormap:\s+([0x0-9a-fA-F]+)',
    'bit_gravity_state': r'Bit Gravity State:\s+(\w+)',
    'window_gravity_state': r'Window Gravity State:\s+(\w+)',
    'backing_store_state': r'Backing Store State:\s+(\w+)',
    'save_under_state': r'Save Under State:\s+(\w+)',
    'map_state': r'Map State:\s+(\w+)',
    'override_redirect_state': r'Override Redirect State:\s+(\w+)',
    'corners': r'Corners:\s+([\+\-\d\s]+)',
    'geometry': r'-geometry\s+(\d+x\d+\+\d+\+\d+)'
}


@dataclass
class XWinInfo:
    window_id: int
    absolute_upper_left_x: int
    absolute_upper_left_y: int
    width: int
    height: int


def _parse_cmd_result(input_string: str) -> any:
    # Dictionary to hold extracted values
    extracted_info = {}

    # Extract values using regex
    for key, pattern in _patterns.items():
        match = re.search(pattern, input_string)
        if match:
            extracted_info[key] = match.group(1)

    # WinInfoClass = type('WinInfo', (object,), extracted_info)
    # wininfo = WinInfoClass()
    wininfo = XWinInfo(
        window_id=int(extracted_info["window_id"], 16),
        absolute_upper_left_x=int(extracted_info["absolute_upper_left_x"]),
        absolute_upper_left_y=int(extracted_info["absolute_upper_left_y"]),
        width=int(extracted_info["width"]),
        height=int(extracted_info["height"])
    )
    return wininfo


def xwininfo(name: str) -> any:
    cmd_res = _run_xwininfo_cmd(name=name)
    wininfo = _parse_cmd_result(cmd_res)
    return wininfo
