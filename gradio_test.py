######################################################
#  gradio_test.py :: Dummy program to test gradio    #
######################################################

# The Interface class creates demos for ML models. It has three arguments
#   fn: Function to wrap a user interface  around. You can pass any Python function you want to wrap with a UI
#   inputs: The Gradio component(s) to use for the input. Must much the inputs of fn function.
#   outputs: The Gradio component(s) to use for the output. Must much the outputs of fn function.

import gradio as gr
def greet(name, intensity):
  return "Hello, " + name + "!" * int(intensity)
demo = gr.Interface(
  fn=greet,
  inputs=["text", "slider"],
  outputs=["text"],
)
demo.launch()