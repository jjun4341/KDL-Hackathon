import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
from asyncio import TimeoutError
import random

class Ticket(commands.Cog):
    def __init__(self, bot):
      self.bot = bot
    
    @commands.command(name = '티켓생성', aliases=['티켓 생성', '티켓제작', 'xlzpttodtjd', 'xlzpt todtjd'])
    async def 티켓생성(self, ctx):
        guild = self.bot.get_guild(754181625776046140)
        ticket_channel_name = random.randint(0, 1000)
        channel = await ctx.guild.create_text_channel('티켓-%d' % ticket_channel_name)
        #permission setting

        await channel.set_permissions(ctx.message.author, send_messages=True, read_messages=True) # 티켓 생성자 permission 셋팅
        await channel.set_permissions(ctx.guild.default_role, send_messages=False, read_messages=False) # 기본 역할 permission 셋팅

        #embed
        embed = discord.Embed(title="티켓 생성 완료", description="티켓이 생성되었습니다.\n아래의 이모지 클릭시 채널이 잠기며,\n티켓 생성자는 읽기 전용 모드로 변경됩니다.\n\n:link: [티켓 봇 초대하기](<https://discord.com/api/oauth2/authorize?client_id=775328529885036595&permissions=1342508144&scope=bot>)", colour=0x00ff00, inline=False)
        msg = await channel.send(embed=embed)
        await msg.add_reaction('🔒')

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == '🔒'

        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=None, check=check)
            await channel.set_permissions(ctx.message.author, send_messages=False, read_messages=True) # 티켓 생성자 permission 셋팅
        except:
            await asyncio.sleep(10)


def setup(bot):
  bot.add_cog(Ticket(bot))