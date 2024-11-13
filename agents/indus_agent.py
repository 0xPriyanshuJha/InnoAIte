import ollama

class IndusResearch:
    def __init__(self, company_name, industry):
        self.company_name = company_name
        self.industry = industry

    def gather_indus_info(self):
        prompt = f"What are the current AI trends and challenges in the {self.industry} industry?"
        return self._get_response(prompt)

    def gather_info(self):
        prompt = f"What strategic focus should a company like {self.company_name} in {self.industry} have?"
        return self._get_response(prompt)

    def _get_response(self, prompt):
        try:
            response = ollama.generate(model="llama2", prompt=prompt)
            if response and isinstance(response, list):
                return response[0].get('text', 'No text found in response')
            return "No response generated"
        except Exception as e:
            return f"Error generating response: {str(e)}"
