#!/usr/bin/env python3
"""
Image Utilities - Functions for working with images

This module provides utility functions for working with images,
including converting images to base64 encoded strings.
"""

import os
import base64
from PIL import Image
import io

def image_to_base64(image_path):
    """
    Convert an image file to a base64 encoded string.
    
    Args:
        image_path (str): Path to the image file
        
    Returns:
        str: Base64 encoded string of the image
        
    Raises:
        FileNotFoundError: If the image file doesn't exist
        Exception: For other errors during conversion
    """
    try:
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image file not found: {image_path}")
        
        # Get the file extension
        _, file_extension = os.path.splitext(image_path)
        file_extension = file_extension.lower().replace('.', '')
        
        # Default to jpeg if extension is not recognized
        if file_extension not in ['png', 'jpg', 'jpeg', 'gif', 'webp', 'bmp']:
            file_extension = 'jpeg'
        
        # Open the image and convert to bytes
        with Image.open(image_path) as img:
            buffer = io.BytesIO()
            img.save(buffer, format=file_extension.upper())
            img_bytes = buffer.getvalue()
        
        # Encode to base64
        base64_encoded = base64.b64encode(img_bytes).decode('utf-8')
        
        return base64_encoded
    
    except FileNotFoundError as e:
        raise e
    except Exception as e:
        raise Exception(f"Error converting image to base64: {str(e)}")

def image_to_base64_with_mime(image_path):
    """
    Convert an image file to a base64 encoded string with MIME type prefix.
    This format is often required for embedding in HTML or sending to APIs.
    
    Args:
        image_path (str): Path to the image file
        
    Returns:
        str: Base64 encoded string with MIME type prefix
        
    Raises:
        FileNotFoundError: If the image file doesn't exist
        Exception: For other errors during conversion
    """
    try:
        # Get the base64 encoded string
        base64_encoded = image_to_base64(image_path)
        
        # Get the file extension for MIME type
        _, file_extension = os.path.splitext(image_path)
        file_extension = file_extension.lower().replace('.', '')
        
        # Default to jpeg if extension is not recognized
        if file_extension not in ['png', 'jpg', 'jpeg', 'gif', 'webp', 'bmp']:
            file_extension = 'jpeg'
        
        # Handle jpg extension for MIME type
        if file_extension == 'jpg':
            file_extension = 'jpeg'
        
        # Create the data URL with MIME type
        mime_prefix = f"data:image/{file_extension};base64,"
        data_url = mime_prefix + base64_encoded
        
        return data_url
    
    except Exception as e:
        raise Exception(f"Error creating base64 data URL: {str(e)}")

def pil_image_to_base64(pil_image, format='PNG'):
    """
    Convert a PIL Image object to a base64 encoded string.
    
    Args:
        pil_image (PIL.Image): PIL Image object
        format (str): Image format (PNG, JPEG, etc.)
        
    Returns:
        str: Base64 encoded string of the image
        
    Raises:
        Exception: For errors during conversion
    """
    try:
        buffer = io.BytesIO()
        pil_image.save(buffer, format=format)
        img_bytes = buffer.getvalue()
        
        # Encode to base64
        base64_encoded = base64.b64encode(img_bytes).decode('utf-8')
        
        return base64_encoded
    
    except Exception as e:
        raise Exception(f"Error converting PIL image to base64: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Example: Convert an image to base64
    try:
        # Replace with your image path
        image_path = "images/screenshot_20250311_151934.png"
        
        # Get base64 encoded string
        base64_str = image_to_base64(image_path)
        print(f"Base64 encoded string (first 100 chars): {base64_str[:100]}...")
        
        # Get base64 with MIME type
        data_url = image_to_base64_with_mime(image_path)
        print(f"Data URL (first 100 chars): {data_url[:100]}...")
        
    except Exception as e:
        print(f"Error: {e}") 