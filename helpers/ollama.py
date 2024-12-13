import requests

class Ollama:
    OLLAMA_API = "http://localhost:11434/api/chat"
    HEADERS = {"Content-Type": "application/json"}
    MODEL = "llama3.2"
    
    def generate_prompt(self, website):
        system_prompt = "You are an assistant that analyzes the contents of a website and provides a short summary, ignoring text that might be navigation related. Respond in markdown. "
        user_prompt = f"\nYou are looking at a website titled {website.title}"
        user_prompt += "\nThe contents of this website is as follows; please provide a short summary of this website in markdown. If it includes news or announcements, then summarize these too.\n\n"
        user_prompt += website.text
        prompt = system_prompt + user_prompt
        return [
            {"role": "user", "content": prompt}
        ]
    
    def generate_payload(self, website):
        return {
            "model": self.MODEL,
            "messages": self.generate_prompt(website),
            "stream": False
        }
    
    def summarize(self, website):
        payload = self.generate_payload(website)
        response = requests.post(self.OLLAMA_API, json=payload, headers=self.HEADERS)
        return response.json()['message']['content']