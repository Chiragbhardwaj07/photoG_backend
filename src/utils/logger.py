import logging
import logging.config
import os

try:
    import yaml
except ImportError:
    yaml = None

def setup_logging(config_path="config/logging_config.yaml"):
    """Setup logging configuration"""
    if yaml and os.path.exists(config_path):
        with open(config_path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=logging.INFO)

def get_logger(name):
    return logging.getLogger(name)
