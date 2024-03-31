import os

from dotenv import load_dotenv

load_dotenv(".env")

DEVS = [
    995099715,
]

API_ID = int(os.getenv("API_ID", "995099715"))

API_HASH = os.getenv("API_HASH", "050e7be583eeb13d8f52c8e7cf8740e9")

BOT_TOKEN = os.getenv("BOT_TOKEN", "6338027024:AAEmOv3PDOyrC_pIH7B_ToZd1i6KqGWRre0")

OWNER_ID = int(os.getenv("OWNER_ID", "995099715"))

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002009863217"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002084592162").split()))

MAX_BOT = int(os.getenv("MAX_BOT", "20"))

RMBG_API = os.getenv("RMBG_API", "9MHfCmCPbe9nkd69piCG12HS")

COMMAND = os.getenv("COMMAND", ".")
PREFIX = COMMAND.split()

OPENAI_KEY = os.getenv(
    "OPENAI_KEY",
    "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",
).split()

MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb+srv://manage:909090@cluster0.hselvy4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
)


