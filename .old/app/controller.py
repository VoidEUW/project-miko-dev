"""
- project-miko
- created by Void EUW
- date: 2024-05-22
"""

# importing files
from app.controllers.event_listener import EventListener
from app.controllers.event_handler import EventHandler
from app.controllers.moderator import Moderator

class Controller:
    """
        ## Class Controller
        used for managing the events and moderation
        ### Methods:
            - `__init__`
    """
    
    def __init__(self, app) -> None:
        """
        ## __init__
            - `EventListener`
            - `EventHandler`
            - `Moderator`
        ### Params:
            - `app` (class Application)
        """

        self.event_listener: EventListener = EventListener(app, self)
        self.event_handler: EventHandler = EventHandler(app)
        self.moderator: Moderator = Moderator(app)