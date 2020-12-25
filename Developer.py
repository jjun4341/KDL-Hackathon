import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import bot
import os

class Developer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = '제작자', aliases=['크레딧', '개발자', 'roqkfwk', 'wpwkrwk'])
    async def 개발자(self, ctx):
        embed = discord.Embed(title = '티켓 봇 개발자', description = '티켓 봇의 개발자 목록입니다.', colour = 0xFF00, inline=True)
        embed.add_field(name = '`총관리자`', value = '땅콩#7610')
        await ctx.send(embed=embed)
    
def setup(bot):
    bot.add_cog(Developer(bot))