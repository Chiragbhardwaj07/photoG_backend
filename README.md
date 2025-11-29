# Photo Guide Agent

A GenAI-based agent that helps users take better photos by providing real-time advice on composition, lighting, and more.

## Structure

The project follows a modular structure:
- `config/`: Configuration files.
- `src/`: Source code.
- `data/`: Data storage.
- `examples/`: Usage examples.

## Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure API Key**:
   - Create a `.env` file in the project root (copy from `.env.example`).
   - Add your Google Gemini API key:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```

## Usage

Run the demo script:
```bash
python examples/photo_guide_demo.py
```
