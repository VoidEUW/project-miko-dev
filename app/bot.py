"""
- project-miko
- created by Void EUW
- date: 2024-05-22
"""

# importing libraries
import discord
# importing files

def start_application(token_keyword):
    client = prepare_client()
    # start_bot(client)
    client.run(get_token(token_keyword))

def prepare_client():
    intents = discord.Intents.all()
    intents.message_content = True
    client = discord.Client(intents=intents)
    return client

def get_token(token_keyword):
    return