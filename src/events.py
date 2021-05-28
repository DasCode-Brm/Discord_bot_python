from datetime import datetime,timedelta
import discord
from discord.ext import commands, tasks
from prefix import bot

status = [discord.Activity(type=discord.ActivityType.watching, name=f"Mi prefix es {bot.command_prefix}"), discord.Game("quererte bebe"),
          discord.Streaming(name="ROLON",
                            url="https://www.youtube.com/watch?v=CLaJp3JnpyQ&list=RDrFk87rdyPro&index=17")]
y, i = 0, 1
a = "$"

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=""))
    status_change.start()
    print(f"Bot encendido: {bot.user.name}")
    print(f"Bot id: {bot.user.id}")
    print(f"Bot servers: {len(bot.guilds)}")
    print('Name_server:', ','.join([str(lst) for lst in bot.guilds]))
    print(datetime.utcnow() == datetime.utcnow())
    if datetime.utcnow():
        print("fecha correcta")
    else:
        print("fecha incorrecta")
    if datetime.utcnow() == datetime.utcnow():
        print(f"Fecha de inicio: {(datetime.now()-timedelta(hours=5)).strftime('%d-%B-%Y %I:%M:%S %p')}")
    else:
        print(f"Fecha de inicio: {(datetime.now()).strftime('%d-%B-%Y %I:%M:%S %p')}")



@tasks.loop(seconds=10)
async def status_change():
    global y, i
    for c in status[y:i]:
        y += 1
        i += 1
    if y == 3 and i == 4:
        y, i = 0, 1
    await bot.change_presence(activity=c)


@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        global a
        a = bot.user.mentioned_in(message)
        print(a)
        await message.channel.send(f"Mi prefix es {bot.command_prefix}")
    await bot.process_commands(message)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("El comando no existe")
