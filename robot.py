import pyautogui

def send_keys():
    #pyautogui.press('enter') #Presses enter
    pyautogui.hotkey('ctrl', 'alt', 'a') #Performs ctrl+shift+esc
    #pyautogui.typewrite('Hello world!\n', interval=secs_between_keys)  #Useful

send_keys()