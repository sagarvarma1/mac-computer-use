#taken from https://github.com/e2b-dev/open-computer-use/blob/master/os_computer_use/grounding.py

from PIL import ImageDraw
import re
import os
from gradio_client import Client, handle_file
from os_computer_use.logging import logger
from os_computer_use.grounding import extract_bbox_midpoint
OSATLAS_HUGGINGFACE_SOURCE = "maxiw/OS-ATLAS"
OSATLAS_HUGGINGFACE_MODEL = "OS-Copilot/OS-Atlas-Base-7B"
OSATLAS_HUGGINGFACE_API = "/run_example"

HF_TOKEN = os.getenv("HF_TOKEN")


def draw_big_dot(image, coordinates, color="red", radius=12):
    draw = ImageDraw.Draw(image)
    x, y = coordinates
    bounding_box = [x - radius, y - radius, x + radius, y + radius]
    draw.ellipse(bounding_box, fill=color, outline=color)
    return image


def extract_bbox_midpoint(bbox_response):
    match = re.search(r"<\|box_start\|>(.*?)<\|box_end\|>", bbox_response)
    inner_text = match.group(1) if match else bbox_response
    numbers = [float(num) for num in re.findall(r"\d+\.\d+|\d+", inner_text)]
    if len(numbers) == 2:
        return numbers[0], numbers[1]
    elif len(numbers) >= 4:
        return (numbers[0] + numbers[2]) // 2, (numbers[1] + numbers[3]) // 2
    else:
        return None
    

class OSAtlasProvider:
    """
    The OS-Atlas provider is used to make calls to OS-Atlas.
    """

    def __init__(self):
        self.client = Client(OSATLAS_HUGGINGFACE_SOURCE, hf_token=HF_TOKEN)

    def call(self, prompt, image_data):
        result = self.client.predict(
            image=handle_file(image_data),
            text_input=prompt + "\nReturn the response in the form of a bbox",
            model_id=OSATLAS_HUGGINGFACE_MODEL,
            api_name=OSATLAS_HUGGINGFACE_API,
        )
        position = extract_bbox_midpoint(result[1])
        image_url = result[2]
        logger.log(f"bbox {image_url}", "gray")
        return position