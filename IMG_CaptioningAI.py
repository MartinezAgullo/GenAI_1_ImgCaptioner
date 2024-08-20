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

img_path = "test_data/img3.jpg"
input_image = Image.open(img_path)

def caption_image(input_image: np.ndarray): 
    raw_image = Image.fromarray(input_image).convert('RGB')
    text = "the image of"
    inputs = processor(images=image, text=text, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=50)
    caption = processor.decode(outputs[0], skip_special_tokens=True)

    return caption


iface = gr.Interface(
    fn=caption_image, 
    inputs=gr.Image(), 
    outputs="text",
    title="Image Captioning",
    description="This is a simple web app for generating captions for images using a trained model."
)

iface.launch()
