import os # for env variables
from dotenv import load_dotenv

load_dotenv() 

BOT_TOKEN = os.getenv("BOT_TOKEN")
OMDB_API_KEY = os.getenv("API_KEY")

DB_PATH = "mySlate.db"