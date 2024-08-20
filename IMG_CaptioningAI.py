#######################################################################
# IMG_CaptioningAI.py
#######################################################################

import gradio as gr
import numpy as np
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration



# Load the pretrained processor and model
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Load 
img_path = "test_data/lion.jpg"
img_path = "test_data/img3.jpg"
image = Image.open(img_path).convert('RGB') # convert it into an RGB format 


text = "the image of"
inputs = processor(images=image, text=text, return_tensors="pt")

# Generate a caption for the image
outputs = model.generate(**inputs, max_length=50)

# Decode the generated tokens to text
caption = processor.decode(outputs[0], skip_special_tokens=True)
# Print the caption
print(caption)