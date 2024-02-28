import discord
import datetime
import asyncio

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

async def alarm_task(time_str, channel):
    while True:
        now = datetime.datetime.now()
        current_time_str = now.strftime('%H:%M')
        if current_time_str == time_str:
            await channel.send("時間だよ！！！")
            break  # 一度アラームを送信したらループを終了します。
        await asyncio.sleep(1)  # 1秒ごとに時間をチェック

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!alarm'):
        time_str = message.content.split('!alarm')[1].strip()  # 時間:分 の形式で取得
        asyncio.create_task(alarm_task(time_str, message.channel))


client.run('TOKEN')
