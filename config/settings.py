import os
import torch
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Settings:
    # Model Settings
    MODEL_NAME = os.getenv("MODEL_NAME", "mistral-7B-v0.1")
    MODEL_PATH = os.getenv("MODEL_PATH", "./models")
    MODEL_CACHE_DIR = os.getenv("MODEL_CACHE_DIR", "./models")
    
    # Adapter Settings
    ADAPTER_PATH = os.getenv("ADAPTER_PATH", "./adapters")
    ADAPTER_CACHE_DIR = os.getenv("ADAPTER_CACHE_DIR", "./adapters")
    
    # Hardware Settings
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
    CUDA_VISIBLE_DEVICES = os.getenv("CUDA_VISIBLE_DEVICES", "0")
    QUANTIZE = os.getenv("QUANTIZE", "True").lower() == "true"
    
    # Server Settings
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", "8000"))
    
    # Monitoring Settings
    ENABLE_METRICS = os.getenv("ENABLE_METRICS", "True").lower() == "true"
    METRICS_PORT = int(os.getenv("METRICS_PORT", "8001"))
    
    # Logging Settings
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE = os.getenv("LOG_FILE", "./logs/hlo.log")
    
    # Security Settings
    MAX_TOKENS = int(os.getenv("MAX_TOKENS", "512"))
    REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "30"))