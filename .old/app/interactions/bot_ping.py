# # # # # # # # #
# project-miko
# Created by Void EUW
# # # # # # # # #

# importing files
from app.utils.messages import send_message

async def bot_ping(app, client, msg):
    latency = (int)(client.latency * 100)
    await send_message(msg, f"Ping is {latency}ms", 0.3)

async def bot_beep(app, msg):
    await send_message(msg, "boop~", 0.4)