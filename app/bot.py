"""
- project-miko
- created by Void EUW
- date: 2024-05-22
"""

# importing libraries
import discord
# importing files
from app.controllers.event_listener import event_listener
from app.controllers.cacher import cacher_ as cacher

def start_application(token_keyword):
    client = prepare_client()
    event_listener(client)
    client.run(cacher.get_token(token_keyword))

def prepare_client():
    intents = discord.Intents.all()
    intents.message_content = True
    client = discord.Client(intents=intents)
    return client