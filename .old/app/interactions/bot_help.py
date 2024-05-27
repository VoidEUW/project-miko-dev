# # # # # # # # #
# project-miko
# Created by Void EUW
# # # # # # # # #

# importing files
from app.utils.messages import send_message, random_message

# will answer if the user needs help
async def bot_help(app, msg):
    selected_message: str = random_message(app.cacher.cache["interactions"]["bot_interactions"]["bot_help"][app.cacher.cache["config"]["config"]["lang"]])
    await send_message(msg, selected_message, 0.3)