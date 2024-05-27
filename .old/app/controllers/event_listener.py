"""
- project-miko
- created by Void EUW
- date: 2024-05-22
"""

class EventListener:
    """
        ## Class EventListener
        checking for the events that happen within the client
        ### Methods:
            - __init__ -> None
            - run -> None
    """

    def __init__(self, app, controller) -> None:
        """
        ## __init__
            - self.app
            - self.controller
            - calling the run method for checking
        ### Params:
            - app (class Application)
            - controller (class Controller)
        """
        
        self.app = app
        self.controller = controller
        self.run()
    
    def run(self) -> None:
        """
        ## run
        checking for the events that happen within the client
        """

        client = self.app.client
        logger = self.app.logger
        controller = self.controller
        
        @client.event
        async def on_ready():
            await logger.log_on_ready(client)
            
        @client.event
        async def on_message(msg):
            if msg.author == client.user:
                return
            await logger.log_on_message(msg)
            if(await controller.moderator.check_message_content(msg) == 1):
                if(await controller.moderator.check_channel_id(msg) == True): # [ ] check_message_id
                    await controller.event_handler.event_handler(client, msg)
                    
        @client.event
        async def on_reaction_add(reaction, user):
            pass
        
        @client.event
        async def on_reaction_remove(reaction, user):
            pass

        @client.event
        async def on_typing(channel, user, _):
            await logger.log_on_typing(channel, user)
            
        @client.event
        async def on_message_edit(before, after):
            await logger.log_on_message_edit(before, after)
            
        @client.event
        async def on_message_delete(msg):
            await logger.log_on_message_delete(msg)
            
            
    # # # # # # # #
    # member events
    # # # # # # # #

        @client.event
        async def on_member_join(member):
            await self.app.interactor.bot_welcome(member)
        
        @client.event
        async def on_member_remove(member):
            await self.app.interactor.bot_goodbye(member)
        
        @client.event
        async def on_member_update(before, after):
            await logger.log_on_member_update(before, after)
        
        @client.event
        async def on_user_update(before, after):
            await logger.log_on_user_update(before, after)
        
        @client.event
        async def on_member_ban(guild, user):
            await logger.log_on_member_ban(guild, user)
        
        @client.event
        async def on_member_unban(guild, user):
            await logger.log_on_member_unban(guild, user)
        
        @client.event
        async def on_voice_state_update(member, before, after):
            await logger.log_on_voice_state_update(member, before, after)
        
    # # # # # # #
    # role events
    # # # # # # #

        @client.event
        async def on_guild_role_create(role):
            pass
        
        @client.event
        async def on_guild_role_update(before, after):
            pass
        
        @client.event
        async def on_guild_role_delete(role):
            pass


    # # # # # # # # #
    # scheduled events
    # # # # # # # # #

        @client.event
        async def on_scheduled_event_create(event):
            pass
        
        @client.event
        async def on_scheduled_event_update(before, after):
            pass
        
        @client.event
        async def on_scheduled_event_delete(event):
            pass
        
        @client.event
        async def on_scheduled_event_user_add(event, user):
            pass
        
        @client.event
        async def on_scheduled_event_user_remove(event, user):
            pass