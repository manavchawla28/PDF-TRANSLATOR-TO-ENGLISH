import gradio as gr
from PyPDF2 import PdfReader
from googletrans import Translator

def extract_text_from_pdf(file_path):
    pdf = PdfReader(file_path)
    text = ''
    for page in pdf.pages:
        text += page.extract_text()
    return text

def translate_text(text, dest_lang='en'):
    translator = Translator()
    translation = translator.translate(text, dest=dest_lang)
    return translation.text

def translate_pdf(file):
    text = extract_text_from_pdf(file.name)
    translation = translate_text(text)
    return translation

iface = gr.Interface(fn=translate_pdf, 
                     inputs=gr.inputs.File(label="Upload PDF file to translate"), 
                     outputs='text', 
                     title="PDF Translation App",
                     description="Use this application to translate PDF documet from foreign language to English. Push 'Submit' button when ready to translate.")
iface.launch()
