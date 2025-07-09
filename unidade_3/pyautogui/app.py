import pyautogui

print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        # positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        # print(positionStr, end='')
        # print('\b' * len(positionStr), end='', flush=True)
        pyautogui.dragTo((x+1), (y+1), button='left')
        x, y = pyautogui.position()
        pyautogui.dragTo((x+1), (y+1), button='left')
        x, y = pyautogui.position()
        pyautogui.dragTo(x, (y-15), button='left')
        x, y = pyautogui.position()
        pyautogui.dragTo((x-15), y, button='left')
        x, y = pyautogui.position()
        if y >= 1000:
            break
        else:
            pass
except KeyboardInterrupt:
    print('\n')