import argparse
import json
import shutil
import os
import pandas as pd

import win32api
import win32con
import win32gui


def click(x, y):
    hwnd = win32gui.FindWindow(None, 'BlueStacks App Player')
    lParam = win32api.MAKELONG(x, y)
    hWnd1 = win32gui.FindWindowEx(hwnd, None, None, None)
    win32gui.SendMessage(hWnd1, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
    win32gui.SendMessage(hWnd1, win32con.WM_LBUTTONUP, None, lParam)
    return


def copy_and_rename(src_path, dest_path, new_name):
    # Copy the file
    shutil.copy(src_path, dest_path)
    # Rename the copied file
    new_path = f"{dest_path}/{new_name}"
    shutil.move(f"{dest_path}/{src_path}", new_path)


def read_json(file):
    with open(file) as f:
        events = json.load(f)["Events"]
    return events


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Bluestacks to python ADB script convertor',
                                    description='What it says on the tin',
                                    epilog='Text at the bottom of help')
    parser.add_argument('filename')
    args = parser.parse_args()
    macro_json = args.filename
    copy_and_rename(os.path.join(os.getcwd(), "macro.py"), os.getcwd(), macro_json.replace(".json", ".py"))
    #json_dict = read_json(macro_json)
    data = json.loads(macro_json)
    df = pd.json_normalize(data['results'])




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
