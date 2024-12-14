import discord
from discord.ext import commands

class Slots(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @discord.app_commands.command(name="testtest123")
    async def testing123(self, interaction:discord.Interaction):
        await interaction.response.send_message("Hello world!")


async def setup(bot):
    await bot.add_cog(Slots(bot))