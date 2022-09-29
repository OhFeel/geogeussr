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






class geoguessr:

  def __init__(self):
        self.delay = 1.5
        
  def get_url(self):
    print(f"{Fore.WHITE}[{Fore.RED}Console{Fore.WHITE}] How many times do you want to run the script?")
    self.num2 = int(input())
    print(f"{Fore.WHITE}[{Fore.RED}Console{Fore.WHITE}] Script will run {self.num2} times")
    print(f"{Fore.WHITE}[{Fore.RED}Console{Fore.WHITE}] Please follow every step carefully")

    print(f"{Fore.WHITE}[{Fore.RED}Console{Fore.WHITE}] Do you want a custom url or the default one?")
    print(f"{Fore.WHITE}[{Fore.RED}Console{Fore.WHITE}] 1. Default")
    print(f"{Fore.WHITE}[{Fore.RED}Console{Fore.WHITE}] 2. Custom")
    url = int(input())
    if url == 1:
      get_url = 'https://www.geoguessr.com/maps/623b4eed21380468d68ca6e6'

    if url == 2:
      print(f"{Fore.WHITE}[{Fore.RED}Console{Fore.WHITE}] Please enter the url")
      get_url = input()
      print(f"{Fore.WHITE}[{Fore.RED}Console{Fore.WHITE}] Url set to {get_url}")

    time.sleep(1)
    print(f"{Fore.WHITE}[{Fore.RED}Console{Fore.WHITE}] Opening Browser...")

    webbrowser.open(get_url)


  def get_positions(self):
    self.print_console("Move your mouse to 'play' and press 'X'")
    while True:
      if keyboard.is_pressed("X"):
        self.pos_play = pyautogui.position()
        pyautogui.click()
        time.sleep(1)
        break
    self.print_console("Move your mouse to 'start' and press 'X'")    
    while True:
      if keyboard.is_pressed("X"):
        self.pos_start = pyautogui.position()
        pyautogui.click()
        time.sleep(.5)
        break
    self.print_console("Move your mouse to 'the map' and press 'X'")
    while True:
      if keyboard.is_pressed("X"):
        self.pos_map = pyautogui.position()
        pyautogui.click()
        time.sleep(.5)
        break
    self.print_console("Move your mouse to 'geuss' and press 'X'")
    while True:
      if keyboard.is_pressed("X"):
        self.pos_geuss = pyautogui.position()
        pyautogui.click()
        time.sleep(.5)
        break
    self.print_console("Move your mouse to 'next round' and press 'X'") 
    while True:
      if keyboard.is_pressed("X"):
        self.pos_next = pyautogui.position()
        pyautogui.click()
        time.sleep(.5)
        break
    self.print_console("Now wait till it says 'view summary' and press 'X'")
    time.sleep(self.delay)
    pyautogui.moveTo(self.pos_map)
    pyautogui.click()
    pyautogui.moveTo(self.pos_geuss)
    pyautogui.click()
    time.sleep(self.delay)
    pyautogui.moveTo(self.pos_next)
    pyautogui.click()
    time.sleep(self.delay)
    pyautogui.moveTo(self.pos_map)
    pyautogui.click()
    pyautogui.moveTo(self.pos_geuss)
    pyautogui.click()
    time.sleep(self.delay)
    pyautogui.moveTo(self.pos_next)
    pyautogui.click()
    time.sleep(self.delay)
    pyautogui.moveTo(self.pos_map)
    pyautogui.click()
    pyautogui.moveTo(self.pos_geuss)
    pyautogui.click()
    time.sleep(self.delay)
    pyautogui.moveTo(self.pos_next)
    pyautogui.click()
    time.sleep(self.delay)
    pyautogui.moveTo(self.pos_map)
    pyautogui.click()
    pyautogui.moveTo(self.pos_geuss)
    pyautogui.click()
    time.sleep(self.delay)
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
    self.print_console(f"Estimated time: {self.num2 * 20} Seconds")


  def run(self):
    
    for x in range(self.num2): 
      time.sleep(self.delay)
      pyautogui.moveTo(self.pos_play)
      pyautogui.click()
      time.sleep(self.delay)
      pyautogui.moveTo(self.pos_start)
      pyautogui.click()
      time.sleep(self.delay)
      pyautogui.moveTo(self.pos_map)
      pyautogui.click()
      pyautogui.moveTo(self.pos_geuss)
      pyautogui.click()
      time.sleep(self.delay)
      pyautogui.moveTo(self.pos_next)
      pyautogui.click()
      time.sleep(self.delay)
      pyautogui.moveTo(self.pos_map)
      pyautogui.click()
      pyautogui.moveTo(self.pos_geuss)
      pyautogui.click()
      time.sleep(self.delay)
      pyautogui.moveTo(self.pos_next)
      pyautogui.click()
      time.sleep(self.delay)
      pyautogui.moveTo(self.pos_map)
      pyautogui.click()
      pyautogui.moveTo(self.pos_geuss)
      pyautogui.click()
      time.sleep(self.delay)
      pyautogui.moveTo(self.pos_next)
      pyautogui.click()
      time.sleep(self.delay)
      pyautogui.moveTo(self.pos_map)
      pyautogui.click()
      pyautogui.moveTo(self.pos_geuss)
      pyautogui.click()
      time.sleep(self.delay)
      pyautogui.moveTo(self.pos_next)
      pyautogui.click()
      time.sleep(self.delay)
      pyautogui.moveTo(self.pos_map)
      pyautogui.click()
      pyautogui.moveTo(self.pos_geuss)
      pyautogui.click()
      time.sleep(self.delay)
      pyautogui.moveTo(self.pos_sum)
      pyautogui.click()
      time.sleep(self.delay)
      pyautogui.moveTo(self.pos_again)
      pyautogui.click()
    


  def fast_slow(self):
    self.print_console("Do you have fast or slow internet?")
    self.print_console("1. Fast")
    self.print_console("2. Medium")
    self.print_console("3. Slow")
    self.print_console("4. Super Slow")

    num_fast_slow = int(input())
    if num_fast_slow == 3:
      self.delay = 5
    if num_fast_slow == 4:
      self.delay = 7.5 
    if num_fast_slow == 2:
      self.delay = 2.5





  def print_console(self, arg, status = "Console"):
        print(f"{Fore.WHITE}[{Fore.RED}{status}{Fore.WHITE}] {arg}")
  def main(self):
    
    os.system(f"title" + " Geoguessr Bot // @ohfeel on github // v 1.2")
    geoguessr.get_url(self)
    geoguessr.fast_slow(self)
    geoguessr.get_positions(self)
    geoguessr.run(self)
    
            
          

                




obj = geoguessr()
obj.main()
