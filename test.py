import base64
from PIL import Image
from io import BytesIO
import requests
import json


def generate_answer(base64_image: str):
    api_url = "http://localhost:11434/api/generate"
    headers = {
        "Content-Type": "application/json"
    }
    # Formatierung des Prompts
    prompt_text = f"Was ist auf diesem Bild zu sehen?: [image](data:image/png;base64,{base64_image})"

    data = {
        "model": "llama3.1",
        "prompt": prompt_text,
        "stream": False,
        "options": {
            "max_tokens": 200,
            "temperature": 0,
            "top_k": 50,
            #"device": "cuda"
        }
    }
    print(f"{data}")
    response = requests.post(api_url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"An error occurred: {response.status_code}")
        return None

    



def image_to_base64(image_path):
    with Image.open(image_path) as img:
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_base64

base64_image = image_to_base64("input.png")
result = generate_answer(base64_image)
print(result)