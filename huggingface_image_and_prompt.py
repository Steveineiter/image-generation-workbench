from diffusers import StableDiffusionImg2ImgPipeline
from PIL import Image
import torch


pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
    # "stabilityai/stable-diffusion-3.5-medium", # Not available with this model
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.bfloat16
).to("cuda")

input_image = Image.open("generations/medium_capybara.png").convert("RGB")
input_image = input_image.resize((512, 512))

prompt = "Add a hat to the capybara"

output = pipe(
    prompt=prompt,
    image=input_image,
    strength=0.75,
    guidance_scale=7.5,
    num_inference_steps=50
)

output.images[0].save("generations/change_add_hat.jpg")
output.images[0].show()
