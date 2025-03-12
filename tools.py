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
