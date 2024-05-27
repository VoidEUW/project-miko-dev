# # # # # # # # #
# project-miko
# Created by Void EUW
# # # # # # # # #

# importing files
from app.utils.messages import send_message, random_message

async def bot_mentioned(app, msg):
    selected_message: str = random_message(app.cacher.cache["interactions"]["bot_interactions"]["bot_mentioned"][app.cacher.cache["config"]["config"]["lang"]])
    await send_message(msg, selected_message, 0.3)