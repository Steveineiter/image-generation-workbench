# stable-diffusion-workbench
Trying out stable diffusion for text to image and virtual try on (VTON)

## Current Tools / Frameworks
- Stable Diffusion 3.5 (as huggingface transformer)
- Hugging Face Diffusers (chaining to create pipelines)
  - Escpecially with black-forest-labs flux-kontext to edit images. (needed to quanititze)
- IDM-VTON for clothing try on. https://github.com/yisol/IDM-VTON?tab=readme-ov-file follow start local gradio demo

## ComfyUI
- Pretty much replaced stable diffusion UI for advanced image generation. 
- I guess this is better as an end-user and if I want to do more advanced stuff.
 
## Steps:
1. use `huggingface-cli login` with a Huggingface token to authorize.
2. run files to generate image given prompt. 