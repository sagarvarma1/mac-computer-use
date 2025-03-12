import os
import base64
import requests
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def encode_image_to_base64(image_path):
    """
    Encode an image file to base64 string
    """
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def analyze_image_from_file(image_path, prompt="What's in this image?"):
    """
    Send an image from a file path to OpenAI's GPT-4 Vision model
    """
    # Encode the image
    base64_image = encode_image_to_base64(image_path)
    
    # Create the API request
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",  # Use the vision-capable model
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
                            "detail": "high"  # Options: "low", "high", "auto"
                        }
                    }
                ]
            }
        ],
        max_tokens=300
    )
    
    return response.choices[0].message.content

def analyze_image_from_url(image_url, prompt="What's in this image?"):
    """
    Send an image from a URL to OpenAI's GPT-4 Vision model
    """
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_url,
                            "detail": "high"
                        }
                    }
                ]
            }
        ],
        max_tokens=300
    )
    
    return response.choices[0].message.content

def analyze_image_from_base64(base64_string, prompt="What's in this image?"):
    """
    Send an image as a base64 string to OpenAI's GPT-4 Vision model
    """
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_string}",
                            "detail": "high"
                        }
                    }
                ]
            }
        ],
        max_tokens=300
    )
    
    return response.choices[0].message.content

# Example usage
if __name__ == "__main__":
    # Example 1: Analyze an image from a file path
    image_path = "workday.png"  # Update with your image path
    result = analyze_image_from_file(image_path, "Describe this image in detail")
    print("Analysis from file:")
    print(result)
    print("\n" + "-"*50 + "\n")
    
    # Example 2: Analyze an image from a URL
    # image_url = "https://example.com/image.jpg"  # Update with a real image URL
    # result = analyze_image_from_url(image_url, "What objects do you see in this image?")
    # print("Analysis from URL:")
    # print(result)
    # print("\n" + "-"*50 + "\n")
    
    # Example 3: If you already have a base64 string
    # with open("path/to/your/base64.txt", "r") as f:
    #     base64_string = f.read().strip()
    # result = analyze_image_from_base64(base64_string, "What's happening in this image?")
    # print("Analysis from base64:")
    # print(result) 