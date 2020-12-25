import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import bot


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = '도움말', aliases=['도움', 'help', 'ehdna', 'ehdnaakf'])
    async def 도움말(self, ctx):
        embed = discord.Embed(title = '티켓 봇 도움말', description = '티켓 봇 명령어 목록입니다.', colour = 0xFF00, inline=True)
        embed.add_field(name = '`-티켓생성`', value = '티켓을 생성합니다.')
        embed.add_field(name = '`-제작자`', value = '티켓 봇 제작자 목록입니다.')
        await ctx.send(embed=embed)
    
def setup(bot):
    bot.add_cog(Help(bot))
