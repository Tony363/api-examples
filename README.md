<p align="center">
  <img src="resources/wordmark.png" style="display: block; margin-left: auto; margin-right: auto; max-width: 50%;" />
</p>

## How to generate images

1. First you need to generate an API Key directly from your [RetroDiffusion account](https://www.retrodiffusion.ai/app/devtools)
2. Make sure you have available credits in your account
   Take in mind that each model supports different styles.
3. Prepare your request, in this example we will use Python and make simple request to generate one image with RD_FLUX model and no styles:

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
  "model": "RDModel.RD_FLUX",
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
- retro
- simple
- detailed
- anime
- game_asset
- portrait
- texture
- ui
- item_sheet
- mc_texture
- mc_item
- character_turnaround
- 1_bit
- animation_four_angle_walking
- no_style

## Animations

We now support animations using the `animation_four_angle_walking` style.

Some important notes:

- Animations are only supported in `RD_FLUX` model.
- Animations currently only support 48x48 resolution. (Bigger or smaller resolutions will be ignored and default to 48x48)
- Animations only support generating one image at a time.
- Outputs are 48x48 transparent GIF images also encoded in base64.

Example payload:

```python
{
	"prompt": "corgi wearing a party hat",
	"width": 48,
	"height": 48,
	"model": "RD_FLUX",
	"num_images": 1,
	"seed": 123,
	"prompt_style": "animation_four_angle_walking"
}
```

## Using img2img

- For now, only `RD_FLUX` supports img2img
- Just send a **base64** image in the `input_image` parameter and adjust `strength` to your liking:
- No need to include `data:image/png;base64,` in the base64 image or similar stuff.
- Send your image as a base64 string, it should be a RGB image with no transparency.

```python
with Image.open(input_image_path) as img:
    rgb_img = img.convert('RGB')
    buffer = BytesIO()
    rgb_img.save(buffer, format='PNG')
    base64_input_image = base64.b64encode(buffer.getvalue()).decode('utf-8')

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
- **What happened to RD_CLASSIC?**
  - We just dropped support for RD_CLASSIC in the future, please use RD_FLUX instead.
