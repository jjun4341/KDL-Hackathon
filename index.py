import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import bot
import koreanbots
import os

bot = commands.Bot(command_prefix='+', help_command=None)

startup_extensions = ['cogs.Ticket_tool.py', 'cogs.Developer']

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('불러오기에 실패 하였습니다. 에러 파일 : {}\n에러 내용 : {}'.format(extension,exc))

@bot.event
async def on_ready():
    print('Client is ready')

bot.run('TOKEN')
