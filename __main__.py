from discord import Intents
from discord.ext import commands

from const import get_const, get_secret
from util import set_programwide


class Zastravapera(commands.Bot):
    def __init__(self):
        super().__init__('!', intents=Intents.all(), sync_commands=True)

        self.guild_ids = set_programwide('guild_ids', list())

    async def setup_hook(self) -> None:
        await self.load_extension('cogs.dictionary')
        print('Loaded cog dictionary')
        # for file in listdir('cogs'):
        #     if file.endswith('.py') and not file.startswith('_'):
        #         await bot.load_extension(f'cogs.{file[:-3]}')

        await bot.tree.sync()

    async def on_ready(self):
        self.guild_ids.clear()
        for guild_id in get_const('guild_ids'):
            guild = self.get_guild(guild_id)
            if guild is not None:
                self.guild_ids.append(guild_id)
                print(f'Bot loaded on guild {guild.name}')

        print(f'Bot loaded. Bot is in {len(self.guild_ids)} guilds.')


bot = Zastravapera()
bot.run(get_secret('bot_token'))
