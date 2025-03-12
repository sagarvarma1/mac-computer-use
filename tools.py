#!/usr/bin/env python3
"""
Mac Control Tools - Simple mouse and keyboard control for macOS

This module provides basic functions to control mouse movement and keyboard input
on macOS systems, designed to be used by AI models.

Requirements:
- pyautogui: pip install pyautogui
"""

import pyautogui
import time

# Configure PyAutoGUI settings
pyautogui.FAILSAFE = True  # Move mouse to upper-left corner to abort
pyautogui.PAUSE = 0.1  # Add small pause between PyAutoGUI commands

# ===== MOUSE FUNCTIONS =====

def move_mouse(x, y, duration=0.2):
    """
    Move the mouse cursor to the specified coordinates.
    
    Args:
        x (int): X-coordinate on screen
        y (int): Y-coordinate on screen
        duration (float): Time in seconds the movement should take
    
    Returns:
        tuple: The new position (x, y) of the mouse
    """
    pyautogui.moveTo(x, y, duration=duration)
    return pyautogui.position()

def click_mouse(button='left', x=None, y=None):
    """
    Click the mouse at the current position or at specified coordinates.
    
    Args:
        button (str): Mouse button to click ('left', 'right', or 'middle')
        x (int, optional): X-coordinate to move to before clicking
        y (int, optional): Y-coordinate to move to before clicking
    """
    if x is not None and y is not None:
        move_mouse(x, y)
    
    pyautogui.click(button=button)

def double_click(x=None, y=None):
    """
    Double-click the left mouse button.
    
    Args:
        x (int, optional): X-coordinate to move to before clicking
        y (int, optional): Y-coordinate to move to before clicking
    """
    if x is not None and y is not None:
        move_mouse(x, y)
    
    pyautogui.doubleClick()

def drag_mouse(start_x, start_y, end_x, end_y, duration=0.2):
    """
    Click and drag from one position to another.
    
    Args:
        start_x (int): Starting X-coordinate
        start_y (int): Starting Y-coordinate
        end_x (int): Ending X-coordinate
        end_y (int): Ending Y-coordinate
        duration (float): Time in seconds the drag should take
    """
    pyautogui.moveTo(start_x, start_y)
    pyautogui.dragTo(end_x, end_y, duration=duration)

def get_mouse_position():
    """
    Get the current mouse cursor position.
    
    Returns:
        tuple: Current (x, y) position of the mouse
    """
    return pyautogui.position()

# ===== SCROLLING FUNCTIONS =====

def scroll(clicks, x=None, y=None):
    """
    Scroll the mouse wheel by the specified number of "clicks".
    Positive values scroll up, negative values scroll down.
    
    Args:
        clicks (int): Number of "clicks" to scroll. Positive scrolls up, negative scrolls down.
        x (int, optional): X-coordinate to move to before scrolling
        y (int, optional): Y-coordinate to move to before scrolling
    """
    if x is not None and y is not None:
        move_mouse(x, y)
    
    pyautogui.scroll(clicks)

def scroll_down(amount=3, x=None, y=None):
    """
    Scroll down by a specified amount.
    
    Args:
        amount (int): Number of "clicks" to scroll down (default: 3)
        x (int, optional): X-coordinate to move to before scrolling
        y (int, optional): Y-coordinate to move to before scrolling
    """
    scroll(-amount, x, y)

def scroll_up(amount=3, x=None, y=None):
    """
    Scroll up by a specified amount.
    
    Args:
        amount (int): Number of "clicks" to scroll up (default: 3)
        x (int, optional): X-coordinate to move to before scrolling
        y (int, optional): Y-coordinate to move to before scrolling
    """
    scroll(amount, x, y)

def page_down(x=None, y=None):
    """
    Scroll down by a larger amount (equivalent to Page Down).
    
    Args:
        x (int, optional): X-coordinate to move to before scrolling
        y (int, optional): Y-coordinate to move to before scrolling
    """
    scroll_down(10, x, y)

def page_up(x=None, y=None):
    """
    Scroll up by a larger amount (equivalent to Page Up).
    
    Args:
        x (int, optional): X-coordinate to move to before scrolling
        y (int, optional): Y-coordinate to move to before scrolling
    """
    scroll_up(10, x, y)

def scroll_to_top():
    """
    Attempt to scroll to the top of the current view.
    This uses keyboard shortcut Command+Home or Home depending on context.
    """
    try:
        pyautogui.hotkey('command', 'home')
    except:
        pyautogui.press('home')

def scroll_to_bottom():
    """
    Attempt to scroll to the bottom of the current view.
    This uses keyboard shortcut Command+End or End depending on context.
    """
    try:
        pyautogui.hotkey('command', 'end')
    except:
        pyautogui.press('end')

# ===== KEYBOARD FUNCTIONS =====

def type_text(text, interval=0.05):
    """
    Type the given text with a specified interval between keystrokes.
    
    Args:
        text (str): The text to type
        interval (float): Seconds between keystrokes
    """
    pyautogui.write(text, interval=interval)

def press_key(key):
    """
    Press and release a single key.
    
    Args:
        key (str): Key to press (e.g., 'a', 'enter', 'space', 'f1')
    """
    pyautogui.press(key)

def press_hotkey(*keys):
    """
    Press a combination of keys (hotkey).
    
    Args:
        *keys: Variable length list of keys to press simultaneously
               (e.g., 'command', 'c' for copy)
    """
    pyautogui.hotkey(*keys)

def key_down(key):
    """
    Press and hold a key.
    
    Args:
        key (str): Key to press down
    """
    pyautogui.keyDown(key)

def key_up(key):
    """
    Release a previously pressed key.
    
    Args:
        key (str): Key to release
    """
    pyautogui.keyUp(key)

# Example usage (for reference, not to be executed)
if __name__ == "__main__":
    # This is just an example and won't run when imported as a module
    print("Screen size:", pyautogui.size())
    print("Current mouse position:", get_mouse_position())
    
    # Example: Move mouse to center of screen
    # screen_width, screen_height = pyautogui.size()
    # move_mouse(screen_width // 2, screen_height // 2)
    
    # Example: Type text
    # type_text("Hello, world!")
    
    # Example: Scroll down
    # scroll_down()
    
    # Example: Page down
    # page_down()

    # how it should work: take screenshot of the current screen, then the llm analyzes it and decides what element to 
    #look for. the it passes that as its output into the grounding model, which finds the coordinates for that element
    #then it passes those coordinates into the tools to click on the elemnt, suppose i want to do scrolling:
    #for scrolling, we do not need the grounding model, the llm can just issue the tool call direcrlt. 
    #actually, it would be a good idea for the grounding model to be a tool call. the click and the grounding model can be embedded one.
    #a good idea would be to make it so anytime that i click, i need to use the grounding model.
    #okay so i will use the grounding model anytime that i need to click on something and everytime or use the keyboard
    #yeah i only need the grounding model for clicking.
    #everything else should be doable otherwise
    #ccol i am on my way to make an agent!
