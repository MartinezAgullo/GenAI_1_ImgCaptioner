# GenerativeAI-based image captioner


## Simple models


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
  

We use 'BlipProcessor' and 'BlipForConditionalGeneration' from the 'transformers' library to set up an image captioning model.  The 'flagged' folder containes the saved outputs from the web applications.
<!-- For [TorchCaptioner.py](https://github.com/MartinezAgullo/GenAI_1_ImgCaptioner/blob/main/TorchCaptioner.py), the torchvision model is used. -->



<!-- ![Image of me riding a tractor](https://github.com/MartinezAgullo/GenAI_1_ImgCaptioner/blob/main/test_data/Results/ScreenshotResult_1.png) -->

![Image of me holding an old coffee mill](https://github.com/MartinezAgullo/GenAI_1_ImgCaptioner/blob/main/test_data/Results/ScreenshotResult_2.png)


![Lion MisID](https://github.com/MartinezAgullo/GenAI_1_ImgCaptioner/blob/main/test_data/Results/ScreenshotResult_3.png)
Figure 2: Visual interface of [TorchCaptioner.py](https://github.com/MartinezAgullo/GenAI_1_ImgCaptioner/blob/main/TorchCaptioner.py).