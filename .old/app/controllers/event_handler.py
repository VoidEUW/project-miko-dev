"""
- project-miko
- created by Void EUW
- date: 2024-05-22
"""

class EventHandler:
    """
        ## Class EventHandler
        used for handling the msg commands sent by the user
        ### Methods:
            - __init__ -> None
            - event_handler -> None
    """

    def __init__(self, app) -> None:
        """
        ## __init__
            - self.app
        ### Params:
            - app (class Application)
        """

        self.app = app
    
    async def event_handler(self, client, msg):
        """
        ## event_handler
            - recognizing the commands
            - calling the Interactor methods
        ### Params:
            - client (Client) is the discord client
            - msg (any) is the message
        """

        logger = self.app.logger

        if(msg.content.startswith(f"{client.user.mention}")):
            # TODO: regex commands
            match msg.content.lower():
                case "<@1220434598434050139> hello":
                    await self.app.interactor.bot_hello(msg)
                case "<@1220434598434050139> meme":
                    await self.app.interactor.bot_memes(msg)
                case "<@1220434598434050139> ping":
                    await self.app.interactor.bot_ping(client, msg)
                case "<@1220434598434050139> beep":
                    await self.app.interactor.bot_beep(msg)
                case "<@1220434598434050139> help":
                    await self.app.interactor.bot_help(msg)
                case "<@1220434598434050139> void":
                    await self.app.interactor.bot_person_void(msg)
                case "<@1220434598434050139> version":
                    await self.app.interactor.bot_version(msg)
                case "<@1220434598434050139> update cache":
                    self.app.cacher.load_cache()
                case _:
                    await logger.log_on_event("bot_mentioned", msg)
                    await self.app.interactor.bot_mentioned(msg)