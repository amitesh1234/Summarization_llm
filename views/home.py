import gradio as gr
from helpers.extractor import Website
from validator.validator import validate_url
from helpers.openai import OpenApi
from helpers.ollama import Ollama

openAI = OpenApi()
llama = Ollama()

def generateWebsiteSummary(url, useOpenAI, useLlama):
    if not validate_url(url):
        return "Please Enter the Correct URL", ""
    if not useOpenAI and not useLlama:
        return "Please Select at least one AI Model to use", ""
    website_details = Website(url)
    openai_details = "<span style='color: orange;'>Hope You liked the response Llama Gave!</span>"
    llama_details = "<span style='color: orange;'>Hope You liked the response OpenAPI Gave!</span>"

    if useOpenAI:
        openai_details = "# <span style='color: orange;'>OpenAI Response:</span> \n\n\n" + openAI.summarize(website_details)
    if useLlama:
        llama_details = "# <span style='color: orange;'>Llama Response:</span> \n\n\n" + llama.summarize(website_details)
    # print(openai_details)
    return openai_details, llama_details

# def build_ui():
#     print("here")
#     demo = gr.Interface(
#         fn=generateWebsiteSummary,
#         inputs=["text"],
#         outputs="markdown",
#         title="Website Summary",
#         description="Website Summarizer!"
#     )
#     return demo

def build_ui():
    print("Initializing the UI...")
    with gr.Blocks() as demo:
        # Add a title and description
        gr.Markdown("# Website Summary\n\n### Summarize your favorite websites in seconds!")
        
        with gr.Row():
            # Input and output side by side
            with gr.Column():
                text_input = gr.Textbox(
                    label="Enter Website Content",
                    placeholder="Paste the content of the website here...",
                    lines=5
                )
                openAI_checkbox = gr.Checkbox(label="Use OpenAI")
                llama_checkbox = gr.Checkbox(label="Use Llama")
            with gr.Column():
                markdown_output_openAI = gr.Markdown(label="Summary Output", value="OpenAI response will show here!")
                markdown_output_llama = gr.Markdown(label="Summary Output", value="Llama response will show here!")
        
        # Submit button to trigger function
        submit_btn = gr.Button("Generate Summary")
        
        # Link the input and output to the function
        submit_btn.click(fn=generateWebsiteSummary, inputs=[text_input, openAI_checkbox, llama_checkbox], outputs=[markdown_output_openAI, markdown_output_llama], show_progress='full')

    return demo


    