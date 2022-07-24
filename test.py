import discord
from discord import app_commands

from const import get_secret


class Client(discord.Client):
    def __init__(self, intents: discord.Intents, **options):
        super().__init__(intents=intents, **options)
        self.synced = False  # we use this so the bot does not sync commands more than once

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild=discord.Object(id=561880172542820353))
            self.synced = True
        print(f'We have logged in as {self.user}.')


client = Client(intents=discord.Intents.all())
tree = app_commands.CommandTree(client)


@tree.command(guild=discord.Object(id=561880172542820353), name='testa', description='wowey, suvie!')
async def testa(interaction: discord.Interaction):
    await interaction.response.send_message(f'I am working! I was made with Discord.py', ephemeral=True)


client.run(get_secret('bot_token'))
