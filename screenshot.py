#!/usr/bin/env python3
"""
Screenshot Tool - Take screenshots of the screen and save to images folder

This module provides functions to capture screenshots of the screen and save them
to an 'images' folder. It maintains only the most recent screenshot by deleting
previous ones.

Requirements:
- pyautogui: pip install pyautogui
- pillow: pip install pillow (usually installed with pyautogui)
"""

import os
import glob
import time
import pyautogui
from datetime import datetime

# Define the directory to save screenshots
IMAGES_DIR = "images"

def ensure_images_dir():
    """
    Ensure the images directory exists.
    """
    if not os.path.exists(IMAGES_DIR):
        os.makedirs(IMAGES_DIR)
        print(f"Created directory: {IMAGES_DIR}")

def delete_previous_screenshots():
    """
    Delete all existing screenshots in the images directory.
    """
    screenshot_files = glob.glob(os.path.join(IMAGES_DIR, "*.png"))
    for file in screenshot_files:
        try:
            os.remove(file)
            print(f"Deleted previous screenshot: {file}")
        except Exception as e:
            print(f"Error deleting {file}: {e}")

def take_screenshot(region=None):
    """
    Take a screenshot of the screen or a specific region and save it to the images directory.
    
    Args:
        region (tuple, optional): Region to capture (left, top, width, height).
                                 If None, captures the entire screen.
    
    Returns:
        str: Path to the saved screenshot
    """
    # Ensure images directory exists
    ensure_images_dir()
    
    # Delete previous screenshots
    delete_previous_screenshots()
    
    # Generate a filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"screenshot_{timestamp}.png"
    filepath = os.path.join(IMAGES_DIR, filename)
    
    # Take the screenshot
    try:
        if region:
            screenshot = pyautogui.screenshot(region=region)
        else:
            screenshot = pyautogui.screenshot()
        
        # Save the screenshot
        screenshot.save(filepath)
        print(f"Screenshot saved: {filepath}")
        return filepath
    except Exception as e:
        print(f"Error taking screenshot: {e}")
        return None

def take_screenshot_with_delay(delay_seconds=3, region=None):
    """
    Take a screenshot after a specified delay.
    
    Args:
        delay_seconds (int): Number of seconds to wait before taking the screenshot
        region (tuple, optional): Region to capture (left, top, width, height)
    
    Returns:
        str: Path to the saved screenshot
    """
    print(f"Taking screenshot in {delay_seconds} seconds...")
    time.sleep(delay_seconds)
    return take_screenshot(region)

def get_latest_screenshot():
    """
    Get the path to the most recent screenshot.
    
    Returns:
        str: Path to the most recent screenshot or None if no screenshots exist
    """
    screenshot_files = glob.glob(os.path.join(IMAGES_DIR, "*.png"))
    if not screenshot_files:
        return None
    
    # Sort files by modification time (newest first)
    latest_screenshot = max(screenshot_files, key=os.path.getmtime)
    return latest_screenshot

if __name__ == "__main__":
    # Take a full screen screenshot immediately
    print("Taking a full screen screenshot...")
    screenshot_path = take_screenshot()
    
    if screenshot_path:
        print(f"Screenshot saved to: {screenshot_path}")
    else:
        print("Failed to take screenshot.") 