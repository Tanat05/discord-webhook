import asyncio
import os
import disnake
from disnake.ext import commands
from disnake import Webhook
import aiohttp



intents = disnake.Intents().all()
bot = commands.Bot(command_prefix="!", intents=intents,owner_id = 836773084056649818)
bot.remove_command("help")

@bot.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.CommandNotFound):
        return

@bot.event
async def on_ready():
    print(f"[!] 다음으로 로그인에 성공했습니다.")
    print(f"[!] 다음 : {bot.user.name}")
    print(f"[!] 다음 : {bot.user.id}")


async def send(content,name):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url('웹훅 URL', session=session)
        await webhook.send(content, username=name)

@bot.slash_command(name="send",description = "send a message")
async def send(inter, name:str, content:str):
    if "@here" in content:
        return
    if "@everyone" in content:
        return
    await send(content,name)
    await inter.response.send_message("전송이 완료되었습니다",ephemeral=True)



keep_alive.keep_alive()
bot.run(os.getenv("TOKEN"))
