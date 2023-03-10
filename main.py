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

# call pet's action .gif to an array
idle = [tk.PhotoImage(file = impath + 'idle.gif', format = 'gif -index %i' %(i)) for i in range(5)] # idle gif, 5 frames
idle_to_sleep = [tk.PhotoImage(file = impath + 'idle-to-sleep.gif', format = 'gif -index %i' %(i)) for i in range(8)]   # idle to sleep gif, 8 frames
sleep = [tk.PhotoImage(file = impath + 'sleeping.gif', format = 'gif -index %i' %(i)) for i in range(3)]    # sleep gif, 3 frames
sleep_to_idle = [tk.PhotoImage(file = impath + 'wake-up.gif', format = 'gif -index %i' %(i)) for i in range(8)] # sleep to idle gif, 8 frames
walk_positive = [tk.PhotoImage(file = impath + 'move-right.gif', format = 'gif -index %i' %(i)) for i in range(8)]  # walk to left gif, 8 frames
walk_negative = [tk.PhotoImage(file = impath + 'move-left.gif', format = 'gif -index %i' %(i)) for i in range(8)]   # walk to right gif, 8 frames

# make black background to transparent
window.config(highlightbackground='black')
window.overrideredirect(True)
window.wm_attributes('-transparentcolor','black')

# let the pet be movable and showing animation
label = tk.Label(window, bd=0, bg='black')
label.pack()
window.mainloop()