# # # # # # # # #
# project-miko
# Created by Void EUW
# # # # # # # # #

async def bot_goodbye(app, member):
    messages: str = app.cacher.cache["interactions"]["bot_interactions"]["bot_goodbye"][app.cacher.cache["config"]["config"]["lang"]]

    app.client.get_channel(1231722238298816594)
    # TODO remove the delete_after when its finished
    await member.send(messages[0], delete_after=15)
    await member.send(messages[1], delete_after=15)