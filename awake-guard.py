import pyautogui
import time
import random

pyautogui.FAILSAFE = False  # Disables emergency stop at (0,0)

def get_safe_mouse_position():
    """Returns a random safe position within the primary screen."""
    screen_width, screen_height = pyautogui.size()
    x, y = pyautogui.position()

    dx, dy = random.randint(-20, 20), random.randint(-20, 20)
    safe_margin = 100
    new_x = max(safe_margin, min(x + dx, screen_width - safe_margin))
    new_y = max(safe_margin, min(y + dy, screen_height - safe_margin))

    return new_x, new_y

def keep_awake(interval=1):  # Move every 5 minutes
    """Moves the mouse and presses Shift key to prevent idle state."""
    try:
        while True:
            new_x, new_y = get_safe_mouse_position()
            print(f"Moving mouse to ({new_x}, {new_y})")

            pyautogui.moveTo(new_x, new_y, duration=5)  # Move mouse
            pyautogui.press("shift")  # Simulate key press to prevent lock

            time.sleep(interval)  # Wait before moving again
    except KeyboardInterrupt:
        print("\nStopped.")

if __name__ == "__main__":
    keep_awake()