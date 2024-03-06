import os
import gradio as gr
from langchain_openai import ChatOpenAI


# Mengatur environment variable "OPENAI_API_KEY" dengan OpenAI API key milikmu. ini diperlukan untuk proses autentikasi ke OpenAI API.
os.environ["OPENAI_API_KEY"] = "API_Opeanai_Kamu"

# Mendefinisikan jenis model 
gpt3 = ChatOpenAI(model_name="gpt-3.5-turbo" )

text = "Berikan fakta menarik tentang kentang!"
print(gpt3.invoke(text).content)

def chatbot(prompt):
    return gpt3.invoke(prompt).content

demo = gr.Interface(fn=chatbot, inputs="text", outputs="text")   

demo.launch(server_name="0.0.0.0", server_port= 7860, share=True)
