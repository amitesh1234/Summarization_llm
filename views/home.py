import gradio as gr
from helpers.extractor import Website
from validator.validator import validate_url
from helpers.openai import OpenApi

def generateWebsiteSummary(url):
    if not validate_url(url):
        return "Please Enter the Correct URL"
    website_details = Website(url)
    openAI = OpenApi()
    details = openAI.summarize(website_details)
    # print(details)
    return details

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
            with gr.Column():
                markdown_output = gr.Markdown(label="Summary Output", value="Summarized will show here!")
        
        # Submit button to trigger function
        submit_btn = gr.Button("Generate Summary")
        
        # Link the input and output to the function
        submit_btn.click(fn=generateWebsiteSummary, inputs=text_input, outputs=markdown_output, show_progress='full')

    return demo


    