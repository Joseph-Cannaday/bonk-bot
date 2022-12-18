import os
import os.path
import json
import discord
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

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
    #check if the
    if os.path.isfile('jailserver.json'):
            with open('jailserver.json') as f:
                data = f.read()
            if data: 
                jail_dict = json.loads(data)
                channel_name = jail_dict.get(str(guild.id), 'bonk')
                channel = discord.utils.get(guild.voice_channels, name = channel_name)

    await name.move_to(channel)
    await interaction.response.send_message(f'Jailed {name.name}')

@tree.command(name='change-jail')
async def self(interaction: discord.Interaction, channel: discord.VoiceChannel):
    guild = interaction.guild
    if os.path.isfile('jailserver.json'):
        with open('jailserver.json') as f:
            data = f.read()
        if data: 
            jail_dict = json.loads(data)
            jail_dict.update({str(guild.id) : channel.name})
        else:
            jail_dict = {str(guild.id) : channel.name}
    else:
        jail_dict = {str(guild.id) : channel.name}
    with open('jailserver.json', 'w') as convert_file:
        convert_file.write(json.dumps(jail_dict))

    await interaction.response.send_message('Jail channel moved to: '+ channel.name, ephemeral=True)

client.run(TOKEN)
