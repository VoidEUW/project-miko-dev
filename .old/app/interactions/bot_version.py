# # # # # # # # #
# project-miko
# Created by Void EUW
# # # # # # # # #

# importing files
from app.utils.messages import send_message

async def bot_version(app, msg):

    #
    # TODO embed
    #

    version = app.cacher.cache["config"]["config"]["version"]
    version_date = app.cacher.cache["config"]["changelog"]["versions"][version]["version-date"]
    raw_changes = app.cacher.cache["config"]["changelog"]["versions"][version][app.cacher.cache["config"]["config"]["lang"]]["changes"]
    version_changes = ""
    for change in raw_changes:
        version_changes += "\n- "
        version_changes += change
    await send_message(msg, f"### Yae Miko\n**Version: {version}**\n**Date: {version_date}**```{version_changes}```", 0.3)