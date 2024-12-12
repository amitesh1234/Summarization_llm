import os
from dotenv import load_dotenv
from IPython.display import Markdown, display
from openai import OpenAI

class OpenApi:
    system_prompt = "You are an assistant that analyzes the contents of a website and provides a short summary, ignoring text that might be navigation related. Respond in markdown."
    
    def __init__(self):
        load_dotenv()
        api_key = os.getenv('OPENAI_API_KEY')
        
        if not api_key:
            print("No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!")
            return "Cannot use openApi"
        elif not api_key.startswith("sk-proj-"):
            print("An API key was found, but it doesn't start sk-proj-; please check you're using the right key - see troubleshooting notebook")
            return "Cannot use openApi"
        elif api_key.strip() != api_key:
            print("An API key was found, but it looks like it might have space or tab characters at the start or end - please remove them - see troubleshooting notebook")
            return "Cannot use openApi"
        self.openai = OpenAI()
        
        
    def user_prompt_for(self, website):
        print("[user_prompt_for]")
        # print(website.title)
        user_prompt = f"You are looking at a website titled {website.title}"
        user_prompt += "\nThe contents of this website is as follows; please provide a short summary of this website in markdown. If it includes news or announcements, then summarize these too.\n\n"
        user_prompt += website.text
        return user_prompt
    
    def messages_for(self, website):
        print("[messages_for]")
        return [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": self.user_prompt_for(website)}
        ]
        
    def summarize(self, website):
        response = self.openai.chat.completions.create(
            model = "gpt-4o-mini",
            messages = self.messages_for(website)
        )
        return response.choices[0].message.content