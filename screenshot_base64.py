#!/usr/bin/env python3
"""
Screenshot Utility - Take screenshots and convert to base64

This module provides functions to capture screenshots of the screen
and convert them to base64 encoded strings for use with APIs.

Requirements:
- pyautogui: pip install pyautogui
- pillow: pip install pillow (usually installed with pyautogui)
"""

import os
import base64
import time
import pyautogui
from datetime import datetime
from PIL import Image
import io

def screenshot_to_base64(region=None, include_mime=False, save_to_file=False, file_dir="images"):
    """
    Take a screenshot and convert it directly to a base64 encoded string.
    
    Args:
        region (tuple, optional): Region to capture (left, top, width, height).
                                 If None, captures the entire screen.
        include_mime (bool): Whether to include the MIME type prefix in the output.
        save_to_file (bool): Whether to also save the screenshot to a file.
        file_dir (str): Directory to save the screenshot if save_to_file is True.
    
    Returns:
        str: Base64 encoded string of the screenshot (with MIME prefix if include_mime=True)
    """
    try:
        # Take the screenshot
        if region:
            screenshot = pyautogui.screenshot(region=region)
        else:
            screenshot = pyautogui.screenshot()
        
        # Save to file if requested
        filepath = None
        if save_to_file:
            # Ensure directory exists
            if not os.path.exists(file_dir):
                os.makedirs(file_dir)
                
            # Generate a filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{timestamp}.png"
            filepath = os.path.join(file_dir, filename)
            
            # Save the screenshot
            screenshot.save(filepath)
            print(f"Screenshot saved: {filepath}")
        
        # Convert to base64
        buffer = io.BytesIO()
        screenshot.save(buffer, format="PNG")
        img_bytes = buffer.getvalue()
        base64_encoded = base64.b64encode(img_bytes).decode('utf-8')
        
        # Add MIME prefix if requested
        if include_mime:
            base64_encoded = f"data:image/png;base64,{base64_encoded}"
        
        return base64_encoded
        
    except Exception as e:
        print(f"Error taking screenshot: {e}")
        return None

def screenshot_to_base64_with_delay(delay_seconds=3, region=None, include_mime=False, save_to_file=False):
    """
    Take a screenshot after a specified delay and convert to base64.
    
    Args:
        delay_seconds (int): Number of seconds to wait before taking the screenshot
        region (tuple, optional): Region to capture (left, top, width, height)
        include_mime (bool): Whether to include the MIME type prefix
        save_to_file (bool): Whether to also save the screenshot to a file
    
    Returns:
        str: Base64 encoded string of the screenshot
    """
    print(f"Taking screenshot in {delay_seconds} seconds...")
    time.sleep(delay_seconds)
    return screenshot_to_base64(region, include_mime, save_to_file)

# Example usage
if __name__ == "__main__":
    # Take a screenshot and convert to base64
    print("Taking a screenshot and converting to base64...")
    base64_str = screenshot_to_base64(save_to_file=True)
    
    if base64_str:
        print(f"Base64 encoded string (first 100 chars): {base64_str[:100]}...")
        print(f"Length of base64 string: {len(base64_str)} characters")
    else:
        print("Failed to take screenshot.") 