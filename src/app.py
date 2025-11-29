import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import FastAPI, UploadFile, File, HTTPException

from pydantic import BaseModel
from src.llm.gemini_client import GeminiClient
from src.prompt_engineering.templates import TemplateManager
from src.utils.logger import setup_logging, get_logger
from dotenv import load_dotenv
import os
import yaml

# Initialize app
load_dotenv()
setup_logging()
logger = get_logger(__name__)
app = FastAPI(title="Photo Guide Agent API")

# Load config
model_name = "gemini-2.0-flash"
if os.path.exists("config/model_config.yaml"):
    with open("config/model_config.yaml", "rt") as f:
        config = yaml.safe_load(f)
        model_name = config.get("model", {}).get("name", model_name)

# Initialize components
try:
    client = GeminiClient(model_name=model_name)
    template_manager = TemplateManager()
except Exception as e:
    logger.error(f"Failed to initialize components: {e}")
    raise RuntimeError("Failed to initialize backend components")

class AnalysisRequest(BaseModel):
    prompt: str

@app.get("/")
async def root():
    return {"message": "Photo Guide Agent API is running"}

@app.post("/analyze")
async def analyze_photo(
    prompt: str = "Analyze this photo and give me advice.", 
    image: UploadFile = File(...)
):
    try:
        logger.info(f"Received analysis request with prompt: {prompt}")
        
        # Read image bytes
        image_bytes = await image.read()
        
        # Format prompt using template
        # Note: For image analysis, we might want a simpler prompt or a specific template
        # For now, we'll append the user's prompt to a system instruction if needed
        # or just pass it directly.
        
        # Get advice
        advice = client.generate(prompt, image_data=image_bytes)
        
        return {"advice": advice}
    except Exception as e:
        logger.error(f"Error processing request: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
