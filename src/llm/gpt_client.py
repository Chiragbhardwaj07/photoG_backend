from .base import BaseLLMClient
import os
try:
    import openai
except ImportError:
    openai = None

class GPTClient(BaseLLMClient):
    def __init__(self, model_name="gpt-3.5-turbo", api_key=None):
        self.model_name = model_name
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key is required. Set OPENAI_API_KEY env var or pass it to constructor.")
        
        if openai:
            openai.api_key = self.api_key

    def generate(self, prompt: str, **kwargs) -> str:
        if not openai:
            raise ImportError("openai package is not installed.")

        try:
            response = openai.ChatCompletion.create(
                model=self.model_name,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                **kwargs
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Error calling OpenAI: {str(e)}"
