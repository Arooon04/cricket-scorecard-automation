import pyautogui
import time
import os

pyautogui.FAILSAFE = True
time.sleep(2)

pyautogui.hotkey('win', 'r')
time.sleep(1)
pyautogui.write('msedge')
time.sleep(1)
pyautogui.press('enter')
pyautogui.sleep(3)

pyautogui.hotkey("ctrl", "t")
time.sleep(1)

pyautogui.write('https://www.cricbuzz.com/live-cricket-scorecard/161245/nz-vs-ind-1st-odi-india-tour-of-new-zealand-2026')  
pyautogui.press('enter')
pyautogui.sleep(5)

pyautogui.hotkey("ctrl", "shift", "i")
time.sleep(2)

pyautogui.hotkey("ctrl", "f")
time.sleep(2)
pyautogui.write("scard-team-13-innings-1", interval=0.05)
pyautogui.press('enter')
time.sleep(2)

pyautogui.press('f2')
time.sleep(1)

pyautogui.hotkey("ctrl", "a")
pyautogui.hotkey("ctrl", "c")
pyautogui.press('esc')
time.sleep(0.5)

output_path = "C:\\GenAI Course\\desktopautomation\\cricket_score.html"
if os.path.exists(output_path):
  os.remove(output_path)
  print("Existing file deleted to prevent overwrite prompts.")

pyautogui.hotkey("win", "r")
pyautogui.write('notepad')
pyautogui.press('enter')
pyautogui.sleep(1)
pyautogui.hotkey("ctrl", "n")
time.sleep(1)

pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("ctrl", "s")
time.sleep(1)
pyautogui.write(f'"{output_path}"')
pyautogui.press('enter')
time.sleep(2)
pyautogui.hotkey("alt", "f4")

pyautogui.hotkey("win", "r")
pyautogui.write(f'"{output_path}"')
pyautogui.press('enter')
time.sleep(2)




