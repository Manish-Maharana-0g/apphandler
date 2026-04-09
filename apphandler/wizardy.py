import os
import sys
import winshell
import win32com.client

def _build_shortcut(shortcut_path, exe_path):
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(shortcut_path)
    if exe_path.endswith(".py"):
        shortcut.Targetpath = sys.executable
        shortcut.Arguments = f'"{exe_path}"'
    else:
        shortcut.Targetpath = exe_path
        shortcut.Arguments = ""
    shortcut.WorkingDirectory = os.path.dirname(exe_path)
    shortcut.save()

def create_shortcut(app_name, exe_path=None):
    if exe_path is None:
        exe_path = os.path.abspath(sys.argv[0])
    desktop = winshell.desktop()
    shortcut_path = os.path.join(desktop, f"{app_name}.lnk")
    _build_shortcut(shortcut_path, exe_path)

def create_start_menu(app_name, exe_path=None):
    if exe_path is None:
        exe_path = os.path.abspath(sys.argv[0])
    start_menu = winshell.start_menu()
    shortcut_path = os.path.join(start_menu, f"{app_name}.lnk")
    _build_shortcut(shortcut_path, exe_path)

def first_launch(exe_path=None, flag=None):
    if exe_path is None:
        exe_path = os.path.abspath(sys.argv[0])
    if flag is None:
        flag = os.path.join(os.path.dirname(exe_path), "installed.flag")
    if not os.path.exists(flag):
        open(flag, "w").close()
        return True
    else:
        return False