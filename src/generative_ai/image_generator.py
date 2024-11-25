import torch
from diffusers import StableDiffusionPipeline

# Loading a stable diffusion pipeline from a pre-trained model
pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")

if torch.cuda.is_available():
    pipe = pipe.to("cuda")  # Only if you have a GPU from Nvidia

# generate an image
prompt = "A funny looking gnome with big eyes. It has a hat and is working on a garden."
image = pipe(prompt).images[0]
image.save("gnome.png")