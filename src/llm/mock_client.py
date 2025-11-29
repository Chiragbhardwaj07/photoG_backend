from .base import BaseLLMClient
import time
import random

class MockLLMClient(BaseLLMClient):
    def generate(self, prompt: str, **kwargs) -> str:
        """Simulate LLM response"""
        time.sleep(0.5) # Simulate latency
        
        # Simple keyword matching for demo purposes
        if "dark" in prompt.lower():
            return "The image seems a bit dark. Try increasing the exposure or adding a light source."
        elif "blur" in prompt.lower():
            return "The subject is blurry. Please hold the camera steady or use a faster shutter speed."
        elif "center" in prompt.lower():
            return "Try to place the subject in the center of the frame for a balanced composition."
        else:
            return "Great shot! Maybe try the rule of thirds for a more dynamic composition."
