import discord
from discord.ext import commands
from discord import app_commands
from config import TEST_GUILDS_ID, GUILDS_ID



class Math(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    
    commands_list = [
        r"`\info` - Information about the bot",
        r"`\roll` - Roll dices", 
        r"`\create` - Create a custom command"
    ]
    
    @app_commands.command(name="calc", description="Do the calculation")
    @app_commands.guilds(*TEST_GUILDS_ID)
    async def calc(self, interaction: discord.Interaction, eq: str):
    
        await interaction.response.send_message(eq)    
    
    
async def setup(client):
    await client.add_cog(Math(client))