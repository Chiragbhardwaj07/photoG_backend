import os
try:
    import yaml
except ImportError:
    yaml = None

class TemplateManager:
    def __init__(self, templates_path="config/prompt_templates.yaml"):
        self.templates = self._load_templates(templates_path)

    def _load_templates(self, path):
        if yaml and os.path.exists(path):
            with open(path, 'rt') as f:
                return yaml.safe_load(f)
        # Fallback if yaml is missing or file not found
        return {
            "photo_advice": {
                "system": "You are a professional photographer guide.",
                "user": "Analyze the following scene description and provide 3 specific tips to improve the photo: {scene_description}"
            }
        }

    def get_template(self, name):
        return self.templates.get(name, {})

    def format_prompt(self, template_name, **kwargs):
        template = self.get_template(template_name)
        if not template:
            return ""
        
        user_prompt = template.get("user", "")
        return user_prompt.format(**kwargs)
