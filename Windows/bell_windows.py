import pystray
from pystray import MenuItem as item
from PIL import Image, ImageTk
import threading
import time
import os
import datetime


def quit_window(icon, item):
    icon.stop()


def start_icon():
    image = Image.open('icon.png')
    menu = (     item('Quit', quit_window),    )
    icon = pystray.Icon('name', image, 'Bell', menu)
    print('Starting icon')
    icon.run()


time_list = [
    [ 8, 50],
    [ 9, 35],
    [ 9, 50],
    [10, 35],
    [10, 40],
    [11, 25],
    [13, 30],
    [14, 15],
    [14, 20],
    [15,  5],
    [15, 20],
    [16,  5],
    [16, 10],
    [16, 55],
    [19, 20],
    [20,  5],
    [20, 10],
    [20, 55],
    [21,  0],
    [21, 45],
]

t1 = threading.Thread(target=start_icon)
t1.start()

while True:
    time.sleep(10)
    
    if not t1.is_alive():
        print('end')
        break
    
    current_time = datetime.datetime.now()
    print(current_time.hour, current_time.minute)
    check_result = False
    if [current_time.hour, current_time.minute] in time_list:
        check_result = True
        os.system('ffplay.exe -nodisp -autoexit sound.mp3')
        time.sleep(60)

print('FINISHED')




