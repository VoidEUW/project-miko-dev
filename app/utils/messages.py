"""
- project-miko
- created by Void EUW
- date: 2024-05-22
"""

# import libraries
import random
import asyncio
    
async def send_message(msg, text: str, duration=1.0, delete_timer=0):
    """
        ## send_messages
        sending the messages in the channel
        ### Params:
            - `msg` (any)
            - `text` (str)
            - `duration` (float) standard: 1.0
    """

    async with msg.channel.typing():
        await asyncio.sleep(duration)
    if delete_timer == 0:
        await msg.channel.send(text)
    else:
        await msg.channel.send(text, delete_after=delete_timer)

def random_message(messages: list[str]):
    """
        ## random_messages
            - self.app
        ### Params:
            - app (class Application)
    """
    random_message: str = messages[random.randint(0, len(messages)-1)]
    return random_message