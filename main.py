import discord
from discord.ext import commands
import interactions
from dotenv import load_dotenv
import os
import random

load_dotenv()

client = discord.Client(intents=discord.Intents.all())
interactions = interactions.Client(token=os.getenv('TOKEN'))

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    channel = client.get_channel(int(os.getenv('CHANNEL_ID')))  # Convert the channel ID to int
    if channel is not None:
        await channel.send(f'All hail the one and only {client.user.name}')
        with open('Pics/CocoGun.jpg', 'rb') as f:
            picture = discord.File(f)
            await channel.send('!!! HELLO MOTHERFUCKER !!!', file = picture)
    else:
        print("Channel not found or accessible.")

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
    
#     if message.content.startswith('/h') or message.content.startswith('/help'):
#         commands = [
#             '/damn: Sends a message "Damn You Mofo"',
#             '/randmanga: Recommends a random manga from the list',
#             '/savemanga [manga_name]: Saves a manga to the list',
#             '/remove [manga_name]: Removes a manga from the list'
#         ]
#         await message.channel.send('\n'.join(commands))
    
#     if message.content.startswith('/damn'):
#         await message.channel.send('Damn You Mofo')
    
#     if message.content.startswith('/randmanga'):
#         with open('mangalist.txt', 'r') as file:
#             random_messages = file.readlines()
        
#         selected_message = random.choice(random_messages).strip()
#         await message.channel.send(f'A worth-reading manga for you: "{selected_message}"')
    
#     if message.content.startswith('/savemanga'):
#         manga = message.content.split('/savemanga ', 1)[1]
        
#         with open('mangalist.txt', 'a') as file:
#             file.write(manga + '\n')
        
#         await message.channel.send(f'"{manga}" has been saved!')
    
#     if message.content.startswith('/remove'):
#         manga_to_remove = message.content.split('/remove ', 1)[1].strip()
        
#         with open('mangalist.txt', 'r') as file:
#             lines = file.readlines()
        
#         with open('mangalist.txt', 'w') as file:
#             for line in lines:
#                 if line.strip() != manga_to_remove:
#                     file.write(line)
        
#         await message.channel.send(f'"{manga_to_remove}" has been removed!')
    
#     if message.content.startswith('/shutdown'):
#         print(f'{client.user.name} is shutting down!')
#         channel = client.get_channel(int(os.getenv('CHANNEL_ID')))
#         with open('Pics\Bruhuh.jpg', 'rb') as f:
#             picture = discord.File(f)
#             await channel.send('さよなら, bruh', file = picture)

#         os._exit()

@interactions.command(name="damn",
                     description="Sends a message 'Damn You Mofo'")
async def damn(ctx):
    await ctx.send("Damn You Mofo")

@interactions.command(name="randmanga",
                     description="Recommends a random manga from the list")
async def randmanga(ctx):
    with open('mangalist.txt', 'r') as file:
        random_messages = file.readlines()
    
    selected_message = random.choice(random_messages).strip()
    await ctx.send(f'A worth-reading manga for you: "{selected_message}"')

@interactions.command(name="savemanga",
                     description="Saves a manga to the list",
                     options=[
                         {
                             "name": "manga_name",
                             "description": "The name of the manga",
                             "type": 3,
                             "required": True
                         }
                     ])
async def savemanga(ctx, manga_name: str):
    with open('mangalist.txt', 'a') as file:
        file.write(manga_name + '\n')
    
    await ctx.send(f'"{manga_name}" has been saved!')

@interactions.command(name="remove",
                     description="Removes a manga from the list",
                     options=[
                         {
                             "name": "manga_name",
                             "description": "The name of the manga",
                             "type": 3,
                             "required": True
                         }
                     ])
async def remove(ctx, manga_name: str):
    with open('mangalist.txt', 'r') as file:
        lines = file.readlines()
    
    with open('mangalist.txt', 'w') as file:
        for line in lines:
            if line.strip() != manga_name:
                file.write(line)
    
    await ctx.send(f'"{manga_name}" has been removed!')

@interactions.command(name="shutdown",
                     description="Shuts down the bot")
async def shutdown(ctx):
    print(f'{client.user.name} is shutting down!')
    channel = client.get_channel(int(os.getenv('CHANNEL_ID')))
    with open('Pics/Bruhuh.jpg', 'rb') as f:
        picture = discord.File(f)
        await channel.send('さよなら, bruh', file=picture)
    await ctx.send("Bot is shutting down.")
    os._exit(0)


client.run(os.getenv('TOKEN'))
