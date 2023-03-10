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
window = tk.Tk()

# call pet's action .gif to an array
idle = [tk.PhotoImage(file = impath + 'idle.gif', format = 'gif -index %i' %(i)) for i in range(5)] # idle gif, 5 frames
idle_to_sleep = [tk.PhotoImage(file = impath + 'idle-to-sleep.gif', format = 'gif -index %i' %(i)) for i in range(8)]   # idle to sleep gif, 8 frames
sleep = [tk.PhotoImage(file = impath + 'sleeping.gif', format = 'gif -index %i' %(i)) for i in range(3)]    # sleep gif, 3 frames
sleep_to_idle = [tk.PhotoImage(file = impath + 'wake-up.gif', format = 'gif -index %i' %(i)) for i in range(8)] # sleep to idle gif, 8 frames
walk_positive = [tk.PhotoImage(file = impath + 'move-left.gif', format = 'gif -index %i' %(i)) for i in range(8)]  # walk to left gif, 8 frames
walk_negative = [tk.PhotoImage(file = impath + 'move-right.gif', format = 'gif -index %i' %(i)) for i in range(8)]   # walk to right gif, 8 frames

# make black background to transparent
window.config(highlightbackground='black')
window.overrideredirect(True)
window.wm_attributes('-transparentcolor','black')

# let a pet be movable and showing animation
label = tk.Label(window, bd=0, bg='black')
label.pack()
window.mainloop()

# want a pet to change its action everytime the .gif have loop once
def gif_work(cycle, frames, event_number, first_num, last_num):
    if cycle < len(frames) - 1:
        cycle += 1
    else:
        cycle = 0
        event_number = random.randrange(first_num, last_num + 1, 1)
    return cycle, event_number


def update(cycle, check, event_number, x):
    # idle
    if check == 0:
        frame = idle[cycle]
        cycle, event_number = gif_work(cycle, idle, event_number, 1, 9)
    
    # idle to sleep
    elif check == 1:
        frame = idle_to_sleep[cycle]
        cycle, event_number = gif_work(cycle, idle_to_sleep, event_number, 10, 10)
    
    # sleep
    elif check == 2:
        frame = sleep[cycle]
        cycle, event_number = gif_work(cycle, sleep, event_number, 10, 15)
    
    # sleep to idle
    elif check ==3:
        frame = sleep_to_idle[cycle]
        cycle, event_number = gif_work(cycle, sleep_to_idle, event_number, 1, 1)

    # move left
    elif check == 4:
        frame = walk_positive[cycle]
        cycle, event_number = gif_work(cycle, walk_positive, event_number, 1, 9)
        x -= 3

    # move right
    elif check == 5:
        frame = walk_negative[cycle]
        cycle , event_number = gif_work(cycle, walk_negative, event_number, 1, 9)
        x -= -3
        
    window.geometry('100x100+' + str(x) + '+1050')
    label.configure(image=frame)
    window.after(1, event, cycle, check, event_number, x)