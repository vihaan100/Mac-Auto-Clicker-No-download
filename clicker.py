import os
import sys
import time
import threading
from pynput import keyboard

# --- CONFIGURATION ---
interval = 0.01  # Starting interval (0.01 seconds = 100 clicks/sec)
step = 0.005     # How much to change the speed per key press
is_clicking = False
cliclick_path = ""

# Locate cliclick automatically
for path in ["/opt/homebrew/bin/cliclick", "/usr/local/bin/cliclick"]:
    if os.path.exists(path):
        cliclick_path = path
        break
if not cliclick_path:
    print("Error: 'cliclick' not found. Install it via homebrew.")
    sys.exit(1)

print("=== MAC DYNAMIC AUTO-CLICKER ===")
print("Press '`' (Backtick) -> Toggle On/Off")
print("Press 'UP ARROW'    -> Make Clicks FASTER")
print("Press 'DOWN ARROW'  -> Make Clicks SLOWER")
print("Press 'ESC'         -> Fully Exit Script")
print(f"Current Interval: {interval}s\n")

def clicking_loop():
    global is_clicking, interval
    while True:
        if is_clicking:
            # "c:." tells cliclick to click exactly where the mouse cursor is
            os.system(f"{cliclick_path} c:.")
            time.sleep(interval)
        else:
            time.sleep(0.1)

def on_press(key):
    global is_clicking, interval, step
    
    try:
        # Check if the pressed key is the backtick/tilde character
        if hasattr(key, 'char') and key.char == '`':
            is_clicking = not is_clicking
            state = "STARTED" if is_clicking else "STOPPED"
            print(f"[{state}] Auto-clicker is now {state.lower()}.")
            
        elif key == keyboard.Key.up:
            if is_clicking:
                interval = max(0.001, interval - step)
                print(f"[SPEED UP] New Interval: {interval:.3f}s (~{int(1/interval)} clicks/sec)")
                
        elif key == keyboard.Key.down:
            if is_clicking:
                interval = interval + step
                print(f"[SLOW DOWN] New Interval: {interval:.3f}s (~{int(1/interval)} clicks/sec)")
                
        elif key == keyboard.Key.esc:
            print("\nExiting script. Goodbye!")
            os._exit(0)
            
    except Exception as e:
        pass

# Start the clicker in a background thread
click_thread = threading.Thread(target=clicking_loop, daemon=True)
click_thread.start()

# Start the global keyboard listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

