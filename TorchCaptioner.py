#######################################################################
# TorchCaptioner.py :: Image Classification in PyTorch
#     - Using a pretrained Resnet-18 model
#     - Using Gradio as web interface
#######################################################################

import torch
import requests
from PIL import Image
from torchvision import transforms
import gradio as gr

#model = None
#labels = None

#######################################################################
# main()
#######################################################################

def main():
    global model, labels
    model = torch.hub.load('pytorch/vision:v0.6.0', 'resnet18', pretrained=True).eval()
    if model is None:
        raise ValueError("Error al cargar el modelo ResNet-18.")

    
    # Download human-readable labels for ImageNet.
    response = requests.get("https://git.io/JJkYN")
    if response.status_code != 200:
        raise ValueError("Error al descargar las etiquetas de ImageNet.")
    labels = response.text.split("\n")

    # Create gradio interface
    gr.Interface(fn=predict,
       inputs=gr.Image(type="pil"),
       outputs=gr.Label(num_top_classes=3),
       examples=["test_data/lion.jpg", "test_data/cheetah.jpg"]).launch()

#######################################################################
# predict()  
#  1 - Converts the input image into a PIL Image and subsequently into a PyTorch tensor
#  2 - Process the tensor through the MLmodel and returns the predictions in the dict confidences
#######################################################################
def predict(inp):
    inp = transforms.ToTensor()(inp).unsqueeze(0)
    global model, labels
    if model is None:
        raise ValueError("El modelo no está cargado correctamente.")
    
    with torch.no_grad():
        prediction = torch.nn.functional.softmax(model(inp)[0], dim=0)
        confidences = {labels[i]: float(prediction[i]) for i in range(1000)}
        # keys are the class labels
        # values are the corresponding confidence probabilities (calculated with softmax)
    return confidences


if __name__ == '__main__':
    main()