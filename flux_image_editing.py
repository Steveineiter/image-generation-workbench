import torch
from diffusers import FluxKontextPipeline
from diffusers.quantizers import PipelineQuantizationConfig
from diffusers.utils import load_image

pipeline_quant_config = PipelineQuantizationConfig(
    quant_backend="bitsandbytes_8bit",
    # 4 Bit actually worked better lol xD mby because of nf4
    quant_kwargs={"load_in_4bit": True, "bnb_4bit_quant_type": "nf4", "bnb_4bit_compute_dtype": torch.bfloat16},
    # quant_kwargs={"load_in_8bit": True, "bnb_4bit_compute_dtype": torch.bfloat16},
    components_to_quantize=["transformer", "text_encoder_2"],
)

pipe = FluxKontextPipeline.from_pretrained("black-forest-labs/FLUX.1-Kontext-dev", quantization_config=pipeline_quant_config,torch_dtype=torch.bfloat16)
pipe.to("cuda")

input_image = load_image("inputs/myself.jpg")

image = pipe(
  image=input_image,
  prompt="Change the suite color to blue. Also make it look more classy.",
  guidance_scale=2.5
).images[0]
image.save("generations/flux_8bit_change_suite_color.png")
