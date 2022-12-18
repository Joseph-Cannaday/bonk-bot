import os

import discord
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
MEMBER = os.getenv('DISCORD_MEMBER')
GUILD_ID = os.getenv('GUILD_ID')

intent = discord.Intents.all()
intent.members = True

client = discord.Client(intents=intent)

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False
        
    async def on_ready(self):
        if not self.synced:
            await tree.sync()#cut out guild param to do a global sync but takes longer
            self.synced = True
        for guild in client.guilds:
            print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})\n'
            )
        
client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(name='bonk', description='bonk someone') 
async def self(interaction: discord.Interaction, name: discord.Member):
    await interaction.response.send_message(f'Bonked {name.name}')
    await name.move_to(None)
  
@tree.command(name='jail')
async def self(interaction: discord.Interaction, name: discord.Member):
    guild = interaction.guild
    channel = discord.utils.get(guild.voice_channels, name = 'bonk')
    await name.move_to(channel)
    await interaction.response.send_message(f'Jailed {name.name}')

@tree.command(name='change-jail', default_member_permissions='administrator')
async def self(interaction: discord.Interaction, channel: discord.VoiceChannel):
    guild = interaction.guild
    channel = discord.utils.get(guild.voice_channels, name = 'bonk')

# TODO: Add server dict for jail vc name

client.run(TOKEN)
