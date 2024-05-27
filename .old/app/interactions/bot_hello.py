# # # # # # # # #
# project-miko
# Created by Void EUW
# # # # # # # # #

# importing files
from app.utils.messages import send_message, random_message

# will answer if the user needs help
async def bot_hello(app, msg):
    """
        ## bot_hello
        returning a hello message to the channel
        ### Params:
            - `app` (class Application)
            - `msg` (any)
    """

    # check if the last message is from the same day
    # if not write hello depending on day time
    # TODO create JSON file for hello answers in every form
    selected_message: str = random_message(app.cacher.cache["interactions"]["bot_interactions"]["bot_hello"][app.cacher.cache["config"]["config"]["lang"]])
    await send_message(msg, selected_message, 0.3)