import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
BOT_TOKEN = os.environ.get("TOKEN") # iz peremennoi okrujeniya poluchili TOKEN
