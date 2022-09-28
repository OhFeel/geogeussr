print("loading...")
import os
os.system("cls")
from colorama import Fore
from colorama import Style
import colorama
colorama.init()
print(Fore.RED + """  ▄████ ▓█████  ▒█████       ▄████ ▓█████  █    ██   ██████   ██████  ██▀███  
 ██▒ ▀█▒▓█   ▀ ▒██▒  ██▒    ██▒ ▀█▒▓█   ▀  ██  ▓██▒▒██    ▒ ▒██    ▒ ▓██ ▒ ██▒
▒██░▄▄▄░▒███   ▒██░  ██▒   ▒██░▄▄▄░▒███   ▓██  ▒██░░ ▓██▄   ░ ▓██▄   ▓██ ░▄█ ▒
░▓█  ██▓▒▓█  ▄ ▒██   ██░   ░▓█  ██▓▒▓█  ▄ ▓▓█  ░██░  ▒   ██▒  ▒   ██▒▒██▀▀█▄  
░▒▓███▀▒░▒████▒░ ████▓▒░   ░▒▓███▀▒░▒████▒▒▒█████▓ ▒██████▒▒▒██████▒▒░██▓ ▒██▒
 ░▒   ▒ ░░ ▒░ ░░ ▒░▒░▒░     ░▒   ▒ ░░ ▒░ ░░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░░ ▒▓ ░▒▓░
  ░   ░  ░ ░  ░  ░ ▒ ▒░      ░   ░  ░ ░  ░░░▒░ ░ ░ ░ ░▒  ░ ░░ ░▒  ░ ░  ░▒ ░ ▒░
░ ░   ░    ░   ░ ░ ░ ▒     ░ ░   ░    ░    ░░░ ░ ░ ░  ░  ░  ░  ░  ░    ░░   ░ 
      ░    ░  ░    ░ ░           ░    ░  ░   ░           ░        ░     ░     """)
print(Style.RESET_ALL)





import keyboard
from os import system
import os
import requests
import webbrowser
import time
from screen_search import *
import pyautogui




print(f"{Fore.WHITE}[{Fore.RED}Console{Fore.WHITE}] How many times do you want to run the script?")
num2 = int(input())
print(f"{Fore.WHITE}[{Fore.RED}Console{Fore.WHITE}] Script will run {num2} times")
print(f"{Fore.WHITE}[{Fore.RED}Console{Fore.WHITE}] Please follow every step carefully")
print(f"{Fore.WHITE}[{Fore.RED}Console{Fore.WHITE}] Opening Browser...")

webbrowser.open('https://www.geoguessr.com/maps/623b4eed21380468d68ca6e6')


class geoguessr:

  def __init__(self):
        self.x = 0
        self.y = 0


  def get_positions(self):
    self.print_console("Move your mouse to 'play' and press 'X'")
    while True:
      if keyboard.is_pressed("X"):
        self.pos_play = pyautogui.position()
        pyautogui.click()
        break
    self.print_console("Move your mouse to 'start' and press 'X'")    
    while True:
      if keyboard.is_pressed("X"):
        self.pos_start = pyautogui.position()
        pyautogui.click()
        break
    self.print_console("Move your mouse to 'the map' and press 'X'")
    while True:
      if keyboard.is_pressed("X"):
        self.pos_map = pyautogui.position()
        pyautogui.click()
        break
    self.print_console("Move your mouse to 'geuss' and press 'X'")
    while True:
      if keyboard.is_pressed("X"):
        self.pos_geuss = pyautogui.position()
        pyautogui.click()
        break
    self.print_console("Move your mouse to 'next round' and press 'X'") 
    while True:
      if keyboard.is_pressed("X"):
        self.pos_next = pyautogui.position()
        pyautogui.click()
        break
    self.print_console("Now wait till it says 'view summary' and press 'X'")
    time.sleep(1.5)
    pyautogui.moveTo(self.pos_map)
    pyautogui.click()
    pyautogui.moveTo(self.pos_geuss)
    pyautogui.click()
    time.sleep(1.5)
    pyautogui.moveTo(self.pos_next)
    pyautogui.click()
    time.sleep(1.5)
    pyautogui.moveTo(self.pos_map)
    pyautogui.click()
    pyautogui.moveTo(self.pos_geuss)
    pyautogui.click()
    time.sleep(1.5)
    pyautogui.moveTo(self.pos_next)
    pyautogui.click()
    time.sleep(1.5)
    pyautogui.moveTo(self.pos_map)
    pyautogui.click()
    pyautogui.moveTo(self.pos_geuss)
    pyautogui.click()
    time.sleep(1.5)
    pyautogui.moveTo(self.pos_next)
    pyautogui.click()
    time.sleep(1.5)
    pyautogui.moveTo(self.pos_map)
    pyautogui.click()
    pyautogui.moveTo(self.pos_geuss)
    pyautogui.click()
    time.sleep(1.5)
    while True:
      if keyboard.is_pressed("X"):
        self.pos_sum = pyautogui.position()
        pyautogui.click()
        break
    self.print_console("Move your mouse to 'play again' and press 'X'")    
    while True:
      if keyboard.is_pressed("X"):
        self.pos_again = pyautogui.position()
        pyautogui.click()
        break
    self.print_console("Done!")
    self.print_console("Setup is complete, the script will run automatically in 5 seconds")
    self.print_console(f"Estimated time: {num2 * 20} Seconds")


  def run(self):
    
    for x in range(num2): 
      time.sleep(1.5)
      pyautogui.moveTo(self.pos_play)
      pyautogui.click()
      time.sleep(1.5)
      pyautogui.moveTo(self.pos_start)
      pyautogui.click()
      time.sleep(1.5)
      pyautogui.moveTo(self.pos_map)
      pyautogui.click()
      pyautogui.moveTo(self.pos_geuss)
      pyautogui.click()
      time.sleep(1.5)
      pyautogui.moveTo(self.pos_next)
      pyautogui.click()
      time.sleep(1.5)
      pyautogui.moveTo(self.pos_map)
      pyautogui.click()
      pyautogui.moveTo(self.pos_geuss)
      pyautogui.click()
      time.sleep(1.5)
      pyautogui.moveTo(self.pos_next)
      pyautogui.click()
      time.sleep(1.5)
      pyautogui.moveTo(self.pos_map)
      pyautogui.click()
      pyautogui.moveTo(self.pos_geuss)
      pyautogui.click()
      time.sleep(1.5)
      pyautogui.moveTo(self.pos_next)
      pyautogui.click()
      time.sleep(1.5)
      pyautogui.moveTo(self.pos_map)
      pyautogui.click()
      pyautogui.moveTo(self.pos_geuss)
      pyautogui.click()
      time.sleep(1.5)
      pyautogui.moveTo(self.pos_next)
      pyautogui.click()
      time.sleep(1.5)
      pyautogui.moveTo(self.pos_map)
      pyautogui.click()
      pyautogui.moveTo(self.pos_geuss)
      pyautogui.click()
      time.sleep(1.5)
      pyautogui.moveTo(self.pos_sum)
      pyautogui.click()
      time.sleep(1.5)
      pyautogui.moveTo(self.pos_again)
      pyautogui.click()
    


  

  def print_console(self, arg, status = "Console"):
        print(f"{Fore.WHITE}[{Fore.RED}{status}{Fore.WHITE}] {arg}")
  def main(self):
    os.system(f"title" + " Geoguessr Bot // @ohfeel on github // v 1.0")
    geoguessr.get_positions(self)
    geoguessr.run(self)
    
            
          

                




obj = geoguessr()
obj.main()