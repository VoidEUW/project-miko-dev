"""
- project-miko
- created by Void EUW
- date: 2024-05-22
"""

# importing libraries
import discord
# importing files
from app.cacher import Cacher
from app.controller import Controller
from app.interactor import Interactor
from app.logger import Logger

class Application:
    """
    ## Class Application
    used for managing the whole bot
    ### Methods:
        - `__init__`
        - `load_application`
    """

    def __init__(self, token_keyword: str) -> None:
        """
        ## __init__
            - `Cacher`
            - `Logger`
            - `Controller`
            - `Interactor`
        ### Params:
            - `token_keyword` is the used token to start the bot
        """

        self.cacher: Cacher = Cacher(token_keyword)
        self.client = self.load_application()
        self.logger: Logger = Logger(self)
        self.controller: Controller = Controller(self)
        self.interactor: Interactor = Interactor(self)
        self.client.run(self.cacher.token)
    
    def load_application(self):
        """
        ## load_application
        creating the client
        ### Returns:
            - `client` (class Client)
        """

        intents = discord.Intents.all()
        intents.message_content = True
        client = discord.Client(intents=intents)
        return client