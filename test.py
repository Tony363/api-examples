import requests
from dotenv import load_dotenv
import os

load_dotenv()

url = "https://api.retrodiffusion.ai/v1/inferences"
method = "POST"

headers = {
    "X-RD-Token": os.getenv("RETRO_DIFFUSION_APIKEY"),
}

payload = {
    "width": 256,
    "height": 256,
    "prompt": "A really cool corgi",
    "num_images": 1,
}

response = requests.request(method, url, headers=headers, json=payload)
print(response.text)
