import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.llm.gemini_client import GeminiClient
from src.prompt_engineering.templates import TemplateManager
from src.utils.logger import setup_logging, get_logger
from dotenv import load_dotenv
import os
try:
    import yaml
except ImportError:
    yaml = None

def main():
    load_dotenv()
    setup_logging()
    logger = get_logger(__name__)
    
    logger.info("Starting Photo Guide Agent Demo (Gemini)...")
    
    # Load model config
    model_name = "gemini-2.0-flash" # Default
    if yaml and os.path.exists("config/model_config.yaml"):
        with open("config/model_config.yaml", "rt") as f:
            config = yaml.safe_load(f)
            model_name = config.get("model", {}).get("name", model_name)
    
    logger.info(f"Using model: {model_name}")

    # Initialize components
    # Ensure GEMINI_API_KEY is set in environment
    try:
        client = GeminiClient(model_name=model_name)
    except ValueError as e:
        logger.error(f"Initialization failed: {e}")
        return
    template_manager = TemplateManager()
    
    # Simulate user input
    scene_description = "I am taking a photo of my dog in the park, but the sun is behind him and his face is dark."
    logger.info(f"User Input: {scene_description}")
    
    # Prepare prompt
    prompt = template_manager.format_prompt("photo_advice", scene_description=scene_description)
    logger.info(f"Generated Prompt: {prompt}")
    
    # Get advice
    advice = client.generate(prompt)
    logger.info(f"Agent Advice: {advice}")

if __name__ == "__main__":
    main()
