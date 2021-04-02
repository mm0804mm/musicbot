import youtube_dl
import discord

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('login')
    print(client.user.id)
    print('------------------------')


@client.event
async def on_message(message):
    if message.content.startswith("/들어와 현성"):
        await message.author.voice.channel.connect()
        await message.channel.send("두둥등장")

    if message.content.startswith("/돌아가 현성"):
        for vc in client.voice_clients:
            if vc.guild == message.guild:
                voice = vc
        await voice.disconnect()
        await message.channel.sned("도주~")

        url = message.content.split(" ")[1]
        option = {
            'outtmpl':"file/"+url.split('=')[1]+".mp3"
            
        }

        with youtube_dl.YoutubeDL(option) as ydl:
            ydl.download(url)
            info = ydl.extract_info(url, download=False)
            title = info["title"]

        voice.play(discord.FFmpegPCMAudio("file/" + url.split('=')[1] + ".mp3"))
        await message.channel.send(title + "을 듣는다고? 뭔 또 버러지같은 노래야?")