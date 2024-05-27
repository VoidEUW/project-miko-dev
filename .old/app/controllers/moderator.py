"""
- project-miko
- created by Void EUW
- date: 2024-05-22
"""

# import other files
from app.utils.messages import send_message, random_message

class Moderator:
    """
        ## Class Moderator
        used for checking messages, uids and channels
        ### Methods:
            - __init__ -> None
            - check_message_content -> int
            - check_channel_id -> None
            - check_creator_id -> None
    """

    def __init__(self, app) -> None:
        """
        ## __init__
            - self.app
        ### Params:
            - app (class Application)
        """
        
        self.app = app
    
    async def check_message_content(self, msg) -> int:
        """
        ## check_message_content
            - no description yet
        ### Params:
            - msg (any) is the message
        ### Returns:
            - returns 0 when there is an error
            - else returns 1
        """

        msg_content = msg.content.lower().split(" ")
        curse_words = self.app.cacher.cache.get("moderation", {}).get("blacklist", {}).get("blacklisted-words", [])
        if curse_words != None:
            if any(word in msg_content for word in curse_words):
                await self.app.logger.log_automod_delete(msg)
                await msg.delete()
                selected_message: str = random_message(self.app.cacher.cache["interactions"]["bot_interactions"]["bot_censor"][self.app.cacher.cache["config"]["config"]["lang"]])
                await send_message(msg, selected_message, 0.5, 10)
                await send_message(msg, self.app.cacher.cache["interactions"]["bot_interactions"]["bot_gifs"]["angry"][0] , 0.2, 10)
                return 0
            return 1
        else:
            self.app.logger.log_automod_delete(msg)
            return 1
    
    async def check_channel_id(self, msg):
        # [ ] check_channel_id
        return True
    
    # [ ] check_creator_uid