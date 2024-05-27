# # # # # # # # #
# project-miko
# Created by Void EUW
# # # # # # # # #

# importing files
from app.utils.messages import send_message

async def bot_person_void(app, msg):
    message: list[str] = app.cacher.cache["interactions"]["bot_person"]["bot_void"][app.cacher.cache["config"]["config"]["lang"]]
    await send_message(msg, message[0] + "\n" + message[1] , 1.3)
    await send_message(msg, message[2] , 0.3)