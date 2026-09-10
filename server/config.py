import os 
from dotenv import load_dotenv

load_dotenv()

OPEN_AI_KEY = os.getenv("OPEN_AI_KEY", "")
IMAGEKIT_PRIVATE_KEY = os.getenv("IMAGEKIT_PRIVATE_KEY", "")
IMAGEKIT_PUBLIC_KEY = os.getenv("IMAGEKIT_PUBLIC_KEY", "")
IMAGEKIT_URL_ENDPOINT = os.getenv("IMAGEKIT_URL_ENDPOINT", "")

DATABASE_URL = "sqllite:///./thumbnailbuilder.db"