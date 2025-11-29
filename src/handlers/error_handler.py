from src.utils.logger import get_logger

logger = get_logger(__name__)

class PhotoGuideError(Exception):
    """Base exception for Photo Guide Agent"""
    pass

class ErrorHandler:
    @staticmethod
    def handle_error(error: Exception):
        logger.error(f"An error occurred: {str(error)}")
        # In a real app, you might send this to Sentry or similar
        return {"error": str(error), "status": "failed"}
