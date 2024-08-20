# GenerativeAI-based image captioner

## Automated Captioner
 - scrapping_AutoCaption.py: Automated image captioning tool with web scrapping. The user provides the URL, and the code generates captions for the images found on the webpage.
 - localFiles_AutoCaption.py: Automatic image captioning for local files

  

<!--
## IMG Captioning AI project

 Image captioning tool using the BLIP model from Hugging Face's Transformers. It stands from *Bootstrapping Language-Image Pre-training*.

 Create a `vevn`:

    pip3 install virtualenv 
    virtualenv my_env # create a virtual environment my_env
    source my_env/bin/activate # activate my_env
     # installing required libraries in my_env
    pip install langchain==0.1.11 gradio==4.21.0 transformers==4.38.2 bs4==0.0.2 requests==2.31.0 torch==2.2.1

Execute:
>     python3.9 IMG_CaptioningAI.py

 - AutoProcessor: Class used for preprocessing data for the BLIP model. . It wraps a BLIP image processor and an OPT/T5 tokenizer into a single processor. This means it can handle both image and text data, preparing it for input into the BLIP model.
 - BlipForConditionalGeneration: Used for conditional text generation given an image and an optional text prompt.

The argument `max_new_tokens=50` specifies that the model should generate a caption of up to 50 tokens in length.


-->

## Other simple models
 - [VisualQuestionAnswering.py](https://github.com/MartinezAgullo/GenAI_1_ImgCaptioner/blob/main/VisualQuestionAnswering.py): Provides conditional and not-conditioned image captioning.
 - [AutomatedPhotoCaptioning.py](https://github.com/MartinezAgullo/GenAI_1_ImgCaptioner/blob/main/AutomatedPhotoCaptioning.py): Provides caption for a given picture.
 - [WebGenerateCaption.py](https://github.com/MartinezAgullo/GenAI_1_ImgCaptioner/blob/main/WebGenerateCaption.py): Web-based application to provide captions using `BlipProcessor` and `BlipForConditionalGeneration`.
 - [TorchCaptioner.py](https://github.com/MartinezAgullo/GenAI_1_ImgCaptioner/blob/main/TorchCaptioner.py):  Web-based application to provide captions using torchvision. Returns probabilities. See Figure 2.

To run them 
>     pip install gymnasium transformers Pillow torch torchvision torchaudio
>     pip install gradio
>     python3.9 AutomatedPhotoCaptioning.py
>     python3.9 VisualQuestionAnswering.py
>     python3.9 TorchCaptioner.py
The web interfaces are obtained using Gradio. After executing the python script, the AI tool is available in the local server http://localhost:7860
  

We use 'BlipProcessor' and 'BlipForConditionalGeneration' from the 'transformers' library to set up an image captioning model.  The 'flagged' folder contains the saved outputs from the web applications.
<!-- For [TorchCaptioner.py](https://github.com/MartinezAgullo/GenAI_1_ImgCaptioner/blob/main/TorchCaptioner.py), the torchvision model is used. -->



<!-- ![Image of me riding a tractor](https://github.com/MartinezAgullo/GenAI_1_ImgCaptioner/blob/main/test_data/Results/ScreenshotResult_1.png) -->

![Image of me holding an old coffee mill](https://github.com/MartinezAgullo/GenAI_1_ImgCaptioner/blob/main/test_data/Results/ScreenshotResult_2.png)
Figure 1: Visual interface of [WebGenerateCaption.py](https://github.com/MartinezAgullo/GenAI_1_ImgCaptioner/blob/main/WebGenerateCaption.py). The images can be upload with the webcam. The AI confuses the caffe mill with a camera.


![Lion MisID](https://github.com/MartinezAgullo/GenAI_1_ImgCaptioner/blob/main/test_data/Results/ScreenshotResult_3.png)
Figure 2: Visual interface of [TorchCaptioner.py](https://github.com/MartinezAgullo/GenAI_1_ImgCaptioner/blob/main/TorchCaptioner.py).



          )  (
         (   ) )
          ) ( (
        _______)_
     .-'---------|  
    ( C|/\/\/\/\/|
     '-./\/\/\/\/|
       '_________'
        '-------'

### Deploy your app with Code Engine

    mkdir myapp
    cd myapp
    touch demo.py Dockerfile requirements.txt

Create `requirements.txt` with `gradio==4.17.0` in it,

    pip3 install -r requirements.txt

The  `Dockerfile`  is the blueprint for assembling a container image.

Open the  `Dockerfile`  in  `/myapp`  and paste the following commands into the file:

    FROM python:3.9
    
    WORKDIR /app
    COPY requirements.txt requirements.txt
    RUN pip3 install --no-cache-dir -r requirements.txt
    
    COPY . .
    
    CMD ["python", "demo.py"]




### Credits

This repository contains solutions and work done for the first module of the course[Building Generative AI-Powered Applications with Python](https://www.coursera.org/learn/building-gen-ai-powered-applications). All rights and credits go to the course creators and instructors. This work is shared for personal use and academic purposes only.