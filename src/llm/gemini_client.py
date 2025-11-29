from .base import BaseLLMClient
import os
try:
    import google.generativeai as genai
except ImportError:
    genai = None

class GeminiClient(BaseLLMClient):
    def __init__(self, model_name="gemini-1.5-flash", api_key=None):
        self.model_name = model_name
        self.api_key = api_key or os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        
        if not self.api_key:
            raise ValueError("Google API key is required. Set GEMINI_API_KEY or GOOGLE_API_KEY env var.")
        
        if genai:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel(self.model_name)

    def generate(self, prompt: str, image_data: bytes = None, **kwargs) -> str:
        if not genai:
            raise ImportError("google-generativeai package is not installed.")

        try:
            inputs = [prompt]
            if image_data:
                from PIL import Image
                import io
                image = Image.open(io.BytesIO(image_data))
                inputs.append(image)

            response = self.model.generate_content(inputs, **kwargs)
            return response.text
        except Exception as e:
            return f"Error calling Gemini: {str(e)}"
