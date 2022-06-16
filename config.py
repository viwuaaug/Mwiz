## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQCWSnjTtmVrUe0nqh4SF1nexA2KPq3Eylji0ZS-LNQw7e9hdm3BZFNWtEpgboanoVMuUDDfV7bVgerHyqDVtY0QtTgHblv2jIO3QnWNLb5psKm-9mUXoFrhZtepVJ9RZnbb_Chj6I4TI72zSobpzJyEeXy3ec0Ei0JFr2kO2jQmgqBbZfI6uO-aqwaFsH88iBwU0zhS6BFjhXCSgzcV4KLrWSzmF_aIE4VJua94pu-QGf_Spt9T4elhclTLi0j6M5FE3O3XAWq-YIBAIvBRG3m-nj1qiWhGUrw0J6SZ2hr9SBMSlp10ZCkn_t6lEeYxQ-k3Js97AzuNT-em3xYHkGNhAAAAATWvjxgA")
BOT_TOKEN = getenv("BOT_TOKEN", "5431876752:AAHzNyYQaXOYQnDwu9RVOmLGVIsWLjSRb8I")
BOT_NAME = getenv("BOT_NAME", "𝐵𝑂𝑇 𝑀𝑈𝑆𝐼𝐶 𝑇𝑋𝑁 ")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "تگسن")
OWNER_USERNAME = getenv("OWNER_USERNAME", "T_T_X_N")
ALIVE_NAME = getenv("ALIVE_NAME", "تگسن")
BOT_USERNAME = getenv("BOT_USERNAME", "MusicTXNbot")
OWNER_ID = getenv("OWNER_ID", "5244755240")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "T_T_X_N")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "N1111V")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "N1111V")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5244755240").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/7713b9828bced85d9b46e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
