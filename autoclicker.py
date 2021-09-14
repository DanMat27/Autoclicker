import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
 
# Delay time between clicks
delay = 0.005
# Mouse key
button = Button.left
# Start/stop autoclicker key
start_stop_key = KeyCode(char='n')
# Kill autoclicker thread key
exit_key = KeyCode(char='m')
 
# Make click mouse button with delay time repeatedly
class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_run = True
 
    def start_clicking(self):
        self.running = True
 
    def stop_clicking(self):
        self.running = False
 
    def exit(self):
        self.stop_clicking()
        self.program_run = False
 
    def run(self):
        while self.program_run:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)
 
# Hears which key user pressed
def on_press(key):
    if key == start_stop_key:
        if thread.running:
            thread.stop_clicking()
        else:
            thread.start_clicking()
    elif key == exit_key:
        thread.exit()
        listener.stop()


# Mouse controller
mouse = Controller()
# Mouse thread
thread = ClickMouse(delay, button)
# Start mouse thread
thread.start()


# Hears if user presses a key
with Listener(on_press=on_press) as listener:
    listener.join()