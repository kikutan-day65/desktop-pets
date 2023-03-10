import random   # a pet is moving in random motion
import tkinter as tk
import pyautogui

x = 1400
cycle = 0
check = 1
idle_num = [1, 2, 3, 4]
sleep_num = [10, 11, 12, 13, 15]
walk_left = [6, 7]
walk_right = [8, 9]
event_number = random.randrange(1, 3, 1)
impath = './images/'    # set the image path here

# create a tkinter window which we are going to place our pet
window = tk.TK()
