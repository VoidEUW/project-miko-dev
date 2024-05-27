"""
- project-miko
- created by Void EUW
- date: 2024-05-22
"""

# events
from app.interactions.bot_welcome import bot_welcome
# from app.interactions.bot_goodbye import bot_goodbye
# interactions
from app.interactions.bot_ping import bot_ping, bot_beep
from app.interactions.bot_help import bot_help
from app.interactions.bot_hello import bot_hello
from app.interactions.bot_mentioned import bot_mentioned
from app.interactions.bot_memes import bot_send_meme
from app.interactions.bot_version import bot_version
from app.interactions.bot_person.bot_person_void import bot_person_void
from app.interactions.bot_person.bot_person_yuxuan import bot_person_yuxuan

class Interactor:
    """
        ## Class Controller
        used for managing the events and moderation
        ### Methods:
            - `__init__` -> None
            - `bot_beep` -> None
            - `bot_ping` -> None
            - `bot_hello` -> None
            - `bot_memes` -> None
            - `bot_person_void` -> None
            - `bot_person_mrgeneral` -> None
            - `bot_version` -> None
            - `bot_mentioned` -> None
            - `bot_welcome` -> None
            - `bot_goodbye` -> None
    """
    
    def __init__(self, app) -> None:
        """
        ## __init__
            - `self.app`
        ### Params:
            - `app` (class Application)
        """

        self.app = app
    
    async def bot_ping(self, client, msg) -> None:
        """
        ## bot_ping
        pinging the bot and returns a latency in ms to the channel
        """
        await self.app.logger.log_on_event("bot_ping", msg)
        await bot_ping(self.app, client, msg)

    async def bot_beep(self, msg) -> None:
        """
        ## bot_beep
        beeping the bot and returns a beep to the channel
        """
        await self.app.logger.log_on_event("bot_beep", msg)
        await bot_beep(self.app, msg)

    async def bot_help(self, msg) -> None:
        """
        ## bot_help
        returning a help message to the channel
        """
        await self.app.logger.log_on_event("bot_help", msg)
        await bot_help(self.app, msg)

    async def bot_hello(self, msg) -> None:
        """
        ## bot_hello
        returning a hello message to the channel
        """
        await bot_hello(self.app, msg)

    async def bot_memes(self, msg) -> None:
        """
        ## bot_help
        will return a random meme which was requested in the meme API
        """
        await self.app.logger.log_on_event("bot_memes", msg)
        await bot_send_meme(self.app, msg)

    async def bot_person_void(self, msg) -> None:
        """
        ## bot_help
        returning a message that talks about Void
        """
        await self.app.logger.log_on_event("bot_person_void", msg)
        await bot_person_void(self.app, msg)

    async def bot_version(self, msg) -> None:
        """
        ## bot_help
        returning a message that lists all version info to the channel
        """
        await self.app.logger.log_on_event("bot_version", msg)
        await bot_version(self.app, msg)

    async def bot_mentioned(self, msg) -> None:
        """
        ## bot_help
        returning a message to indicate that the bot has seen the mention
        """
        await self.app.logger.log_on_event("bot_mentioned", msg)
        await bot_mentioned(self.app, msg)

    async def bot_welcome(self, member) -> None:
        """
        ## bot_help
        returning a welcome message to the user and to the channel
        """
        await self.app.logger.log_on_member_join(member)
        await bot_welcome(self.app, member)
    
    async def bot_goodbye(self, member) -> None:
        """
        ## bot_help
        returning a goodbye message to the channeö
        """
        await self.app.logger.log_on_member_remove(member)
        #await bot_goodbye(self.app, member)