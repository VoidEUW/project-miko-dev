# # # # # # # # #
# project-miko
# Created by Void EUW
# # # # # # # # #

import json
import requests

# importing files
from app.utils.messages import send_message, random_message

async def bot_send_meme(app, msg):
    selected_message = random_message(app.cacher.cache["interactions"]["bot_interactions"]["bot_memes"][app.cacher.cache["config"]["config"]["lang"]])
    meme_api_response = requests.get("https://meme-api.com/gimme")
    if meme_api_response == None:
        return
    json_data = json.loads(meme_api_response.text)
    await send_message(msg, selected_message, 0.2)
    await send_message(msg, json_data["url"], 0.3)