# image-generation-workbench

Trying out stable diffusion for text to image and virtual try on (VTON)

## Conclusion:
- Use IDM-VTON for **clothing try on,** if i draw a mask this works very well and is actually a nice usecase.
- For the rest it would need more time investment aka just use services for that (eg finding new styles). Also I think its unnecessary, because also if I find cool things they might not exist in the real world xD Or look much worse since models optimize the shape etc for it to look better. 

## Current Tools / Frameworks

- Stable Diffusion 3.5 (as huggingface transformer)
- Hugging Face Diffusers (chaining to create pipelines)
  - Escpecially with black-forest-labs flux-kontext to edit images. (needed to quanititze)
- IDM-VTON for clothing try on. https://github.com/yisol/IDM-VTON?tab=readme-ov-file follow start local gradio demo

## ComfyUI

- Pretty much replaced stable diffusion UI for advanced image generation.
- I guess this is better as an end-user and if I want to do more advanced stuff.
- https://www.youtube.com/watch?v=pjW9KfZ1VY4 nice source / worklows. I think IDM-VTON worked as well tho xD
- https://docs.comfy.org/tutorials/basic/inpaint this one works ok-ish for generating new styles of myself. But its still quite bad - I think if i want to really use that i would need to do built a LoRA of myself and then just generate new images and go much deeper with that. So probably its smarter to just pay for this service lol xD 
  
## Steps:

1. use `huggingface-cli login` with a Huggingface token to authorize.
2. run files to generate image given prompt.
