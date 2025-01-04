<p align="center">
  <img src="resources/wordmark.png" style="display: block; margin-left: auto; margin-right: auto; max-width: 50%;" />
</p>

## How to generate images
1. First you need to generate an API Key directly from your [RetroDiffusion account](https://www.retrodiffusion.ai/app/devtools)
2. Make sure you have available credits in your account
3. We currently support two main models: `RD_CLASSIC` and `RD_FLUX`. Classic is our SD v1.5 based model targeting a more traditional look and smaller resolution, while Flux works great with bigger resolutions.
Take in mind that each model supports different styles.
4. Prepare your request, in this example we will use Python and make simple request to generate one image with RD_CLASSIC model and no styles:
```python
import requests

url = "https://api.retrodiffusion.ai/v1/inferences"
method = "POST"

headers = {
    "X-RD-Token": "YOUR_API_KEY",
}

payload = {
    "model": "RD_CLASSIC",
    "width": 64,
    "height": 64,
    "prompt": "A really cool corgi",
    "num_images": 1
}

response = requests.request(method, url, headers=headers, json=payload)
print(response.text)
```
5. The response should look like this:
```json
{
	"created_at": 1733425519,
	"credit_cost": 1,
	"base64_images": ["..."],
	"model": "RDModel.RD_CLASSIC",
	"type": "txt2img",
	"remaining_credits": 999
}
```

## Using RD_FLUX
1. Based on the example above, we only need to adjust the model to `RD_FLUX`:
```python
import requests

url = "https://api.retrodiffusion.ai/v1/inferences"
method = "POST"

headers = {
    "X-RD-Token": "YOUR_API_KEY",
}

payload = {
    "model": "RD_FLUX",
    "width": 256,
    "height": 256,
    "prompt": "A really cool corgi wearing sunglasses and a party hat",
    "num_images": 1
}

response = requests.request(method, url, headers=headers, json=payload)
print(response.text)
```

## Using styles
### RD_CLASSIC
- `RD_CLASSIC` expects their styles in the parameter named `loras`
- It's a dictionary with the style name as the key and the value as the weight of the style:
```python
payload = {
    "model": "RD_CLASSIC",
    "width": 64,
    "height": 64,
    "prompt": "A really cool corgi wearing sunglasses and a party hat",
    "num_images": 1,
    "loras": {
        "1bit": 50
    }
}
```
#### Available styles:
- 1bit
- flatshading
- frontfacing
- gameboy
- gameboyadvance
- gamecharacters
- gameicons
- isometric
- nashorkimitems
- neogeo
- nes
- playstation
- snes
- tiling
- topdown
- gamecharactersanime
- gamecharactersretro
- uipanel
- simplegeometric
- industrial
- modern
- segagenesis

### RD_FLUX
- `RD_FLUX` only support one style at a time, and it's passed as a parameter named `prompt_style`:
```python
payload = {
    "model": "RD_FLUX",
    "width": 256,
    "height": 256,
    "prompt": "A really cool corgi wearing sunglasses and a party hat",
    "num_images": 1,
    "prompt_style": "simple"
}
```

#### Available styles:
- default
- simple
- detailed
- anime
- game_asset
- portrait
- texture
- ui
- spritesheet
- no_style

## Using img2img
- For now, only `RD_CLASSIC` and `RD_FLUX` supports img2img
- Just send a **base64** image in the `input_image` parameter and adjust `strength` to your liking:
- No need to include `data:image/png;base64,` in the base64 image or similar stuff.
- Send your image as a base64 string, it should be a RGB image with no transparency.

```python
with Image.open(input_image_path) as img:
    rgb_img = img.convert('RGB')
    buffer = BytesIO()
    rgb_img.save(buffer, format='PNG')
    base64_input_image = base64.b64encode(buffer.getvalue()).decode('utf-8')

# RD_CLASSIC img2img
payload = {
    "prompt": "A really cool corgi wearing sunglasses and a party hat",
    "model": "RD_CLASSIC",
    "width": 64,
    "height": 64,
    "input_image": base64_input_image,
    "strength": 0.5
}

# RD_FLUX img2img
payload = {
    "prompt": "A really cool corgi wearing sunglasses and a party hat",
    "model": "RD_FLUX",
    "width": 256,
    "height": 256,
    "input_image": base64_input_image,
    "strength": 0.8
}
```

## FAQ
- **How much does it cost?**
  - Cost is calculated based on the model and resolution you choose. You can check the cost of each request in our [web app](https://www.retrodiffusion.ai/)
- **How can I check my remaining credits?**
    - You can check your remaining credits in our [web app](https://www.retrodiffusion.ai/)