from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

# keyboard.press('a')
# keyboard.release('a')
# keyboard.press(Key.cmd)
# keyboard.release(Key.cmda)

for char in "\n# This is a sentence written in Python!":
    keyboard.press(char)
    keyboard.release(char)
    time.sleep(0.2)
# 在光标所在处打印这段文字
# This is a sentence written in Python!
