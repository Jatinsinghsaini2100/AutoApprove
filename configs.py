from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", ""))
    API_HASH = getenv("API_HASH", "")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    FSUB = getenv("FSUB", "Sastatony")
    CHID = int(getenv("CHID", ""))
    SUDO = list(map(int, getenv("SUDO", "6996289801").split()))
    MONGO_URI = getenv("MONGO_URI", "")
    
cfg = Config()
