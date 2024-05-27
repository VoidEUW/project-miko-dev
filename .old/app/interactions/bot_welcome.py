# # # # # # # # #
# project-miko
# Created by Void EUW
# # # # # # # # #

from app.utils.messages import random_message

async def bot_welcome(app, member):
    messages: str = app.cacher.cache["interactions"]["bot_interactions"]["bot_welcome"][app.cacher.cache["config"]["config"]["lang"]]["dm"]

    welcome_message = random_message(app.cacher.cache["interactions"]["bot_interactions"]["bot_welcome"][app.cacher.cache["config"]["config"]["lang"]]["guild"])
    # TODO better Channel ID
    welcome_channel = app.client.get_channel(1241836347174551594)
    await welcome_channel.send(f"{member.name} {welcome_message}")

    # TODO remove the delete_after when its finished
    await member.send(messages[0]) # delete_after=15
    await member.send(messages[1]) # delete_after=15