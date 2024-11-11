import ollama

class UsecaseResearch:
    def __init__(self, industry_info, company_info):
        self.industry_info = industry_info
        self.company_info = company_info
    
    def generate_usecases(self):
        prompt=f"Generate AI and Generative AI use cases for a company in the {self.industry_info} industry."
        response = ollama.Completion.create(model="llama2", prompt=prompt)
        return response["choices"][0]["text"].splitlines()