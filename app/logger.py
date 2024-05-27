"""
- project-miko
- created by Void EUW
- date: 2024-05-22
"""

# importing libraries
import discord
from datetime import datetime
# importing other files

class Logger:
    
    def __init__(self, app) -> None:
        """
        ## __init__
            - self.app
        ### Params:
            - app (class Application)
        """

        self.app = app
    
    def log_prefix(self):
        bot_prefix = self.app.cacher.cache["config"]["config"]["bot-tag"]
        prefix = f"{self.time()} {bot_prefix}"
        return prefix
    
    def time(self):
        return datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    
    async def console_log(self, text, guild_id):
        bot_prefix = self.log_prefix()
        await self.write_log(f"{bot_prefix}     {text}", guild_id)

    # logs when bot is ready to operate
    async def log_on_ready(self, client):
        await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.listening, name="Void"))
        bot_prefix = self.log_prefix()
        await self.write_log(f"{bot_prefix}     '{client.user.name}' is online")

    # logs when bot receives a message
    async def log_on_message(self, msg):
        bot_prefix = self.log_prefix()
        await self.write_log(f"{bot_prefix}     '{msg.author}' has sent: '{msg.content}' in '{msg.channel}'", msg.guild.id)

    # logs when someone is typing a message
    async def log_on_typing(self, channel, user):
        bot_prefix = self.log_prefix()
        await self.write_log(f"{bot_prefix}     '{user}' is typing in '{channel.name}'", channel.guild.id)

    # logs when someone has edited a message
    async def log_on_message_edit(self, before, after):
        bot_prefix = self.log_prefix()
        await self.write_log(f"{bot_prefix}     '{before.author}' changed a message in '{before.channel}': '{before.content}' -> '{after.content}'", 1241836346692075690) # FIXME

    # logs when someone has deleted a message
    async def log_on_message_delete(self, msg):
        bot_prefix = self.log_prefix()
        # FIXME dms delete are shown as a problem
        await self.write_log(f"{bot_prefix}     '{msg.author}' has deleted a message: '{msg.content}'", 1241836346692075690) # FIXME
        
    async def log_on_event(self, event_name, msg):
        bot_prefix = self.log_prefix()
        await self.write_log(f"{bot_prefix}     '{event_name}' triggered by {msg.author.name}", msg.guild.id)
        
    async def log_on_member_join(self, member):
        bot_prefix = self.log_prefix()
        await self.write_log(f"{bot_prefix}     '{member.name}' joined {member.guild.name}", member.guild.id)

    async def log_on_member_remove(self, member):
        bot_prefix = self.log_prefix()
        await self.write_log(f"{bot_prefix}     '{member.name}' left {member.guild.name}", member.guild.id)
        pass

    async def log_on_member_update(before, after):
        pass

    async def log_on_user_update(before, after):
        pass

    async def log_on_member_ban(guild, user):
        pass

    async def log_on_member_unban(guild, user):
        pass

    async def log_on_voice_state_update(self, member, before, after):
        bot_prefix = self.log_prefix()
        await self.write_log(f"{bot_prefix}     EVENT '{member.name}' changed voice-activity '{before.channel}' in '{member.guild}'", member.guild.id)
        pass

    async def log_on_guild_role_create(role):
        pass

    async def log_on_guild_role_update(before, after):
        pass

    async def log_on_guild_role_delete(role):
        pass

    async def log_on_scheduled_event_create(event):
        pass

    async def log_on_scheduled_event_update(before, after):
        pass

    async def log_on_scheduled_event_delete(event):
        pass

    async def log_on_scheduled_event_user_add(event, user):
        pass

    async def log_on_scheduled_event_user_remove(event, user):
        pass

    async def log_automod_delete(self, msg):
        bot_prefix = self.log_prefix()
        await self.write_log(f"{bot_prefix}     AUTOMOD deleted message: '{msg.content}'", msg.guild.id)
        
    async def log_automod_error(self, msg):
        bot_prefix = self.log_prefix()
        await self.write_log(f"{bot_prefix}     AUTOMOD error 'backlisted-words' is empty!", msg.guild.id)

    # will write text into the server_ids file
    async def write_log(self, text, guild_id=None):
        if(guild_id != None):
            log_path = self.app.cacher.cache["config"]["config"]["paths"]["log-path"]
            guild_id_str: str = (str)(guild_id)
            # BUG if file doesn't exist
            f = open(f"{log_path}{guild_id_str}.log", "a")
            f.write("\n" + text)
            f.close()
        print(text)
        # TODO dynamic Channel config in a json file
        log_channel = self.app.client.get_channel(1241838859776426206)
        await log_channel.send(text)
        