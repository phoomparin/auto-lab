#!/usr/bin/env python3

import pyautogui
import time

print("Ready...")

time.sleep(5)

print("Activating...")
pyautogui.click()

distance = 200

while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.2)
    distance = distance - 5
    pyautogui.dragRel(0, distance, duration=0.2)
    pyautogui.dragRel(-distance, 0, duration=0.2)
    distance = distance - 5
    pyautogui.dragRel(0, -distance, duration=0.2)
