import asyncio

import discord
# from discord import activity
from discord.ext import commands, tasks
from prefix import bot
from datetime import datetime, timedelta, date

d = []


@bot.command(name="carr")
async def carr(ctx):
    user = ctx.message.author.id
    usuario = ctx.message.author
    await ctx.send("hola {0.mention}, {1}".format(usuario, user))
    await bot.delete_message(ctx)


@bot.command()
async def nuke(ctx, ready=""):
    if ready == "stop":
        await ctx.send("comando nuclear detenido")
        return
    await ctx.send("comando nuclear iniciado")


@bot.command()
async def tim(ctx):
    group_message = []
    minimum_date = datetime.utcnow().date().strftime("%d/%m/%Y")
    minimum_date = datetime.strptime(minimum_date, '%d/%m/%Y')
    messages = await ctx.channel.history(limit=None, after=minimum_date).flatten()
    for message in messages:
        message_date = message.created_at
        message_date = message_date - timedelta(hours=5)
        if minimum_date <= message_date <= datetime.utcnow():
            group_message.append(message)
    await ctx.send(f"Cantidad de mensajes: {len(group_message)}")
    """for d in group_message:
        print(f"mensaje content: {d.content}")"""


@bot.command(aliases=["cls"])
@commands.has_permissions(manage_messages=True)
@commands.bot_has_permissions(manage_messages=True)
async def clear(ctx, m=""):
    global d, embed
    if m == "":
        embes = discord.Embed(description="<a:no:846822577666392094> Requiere un argumento <a:no:846822577666392094> ",
                              color=discord.Color.red())
        await ctx.send(embed=embes)
        return
    elif m.isnumeric():
        m = int(m)
        d = []
        if m == 0:
            embed = discord.Embed(title="Aviso", description="{0} mensajes borrados".format(len(d)),
                                  color=discord.Color.red())
            await ctx.send(embed=embed, delete_after=4)
            return
    else:
        await ctx.send("solo argumentos numericos positivos")
        return
    await ctx.message.delete()
    f = datetime.utcnow() - timedelta(days=14)
    async for message in ctx.channel.history(limit=m):
        time = message.created_at
        if f <= time <= datetime.utcnow() and m >= 1:
            d = await ctx.channel.purge(limit=m, after=datetime.utcnow() - timedelta(days=14))
            if len(d) > 1:
                embed = discord.Embed(title="Aviso", description="{0} mensajes borrados".format(len(d)),
                                      color=discord.Color.red())
            elif len(d) in range(0, 2):
                embed = discord.Embed(title="Aviso", description="{0} mensaje borrado".format(len(d)),
                                      color=discord.Color.red())
            m = 0
        elif not f <= time <= datetime.utcnow():
            if len(d) >= 1:
                await ctx.send(
                    "Mensajes borrados {0}, sin embargo, discord no permite borrar mensajes de mas de 2 semanas".format(
                        len(d)))
                return
            elif len(d) == 0:
                day = datetime.utcnow().date() - time.date()
                day = day.days
                await ctx.send("Debido a una limitacion de discord, no puedo eliminar mensajes de mas de dos semanas "
                               "de antiguedad, el ultimo mensajes enviado tiene: {0} dias, si quiere eliminar el "
                               " contenido, clona el canal".format(day))
                return
    await ctx.send(embed=embed, delete_after=4)


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title="Error", description=":no_entry_sign: No tienes permisos :no_entry_sign:",
                              color=discord.Color.purple())
        await ctx.send(embed=embed)

    if isinstance(error, commands.errors.BotMissingPermissions):
        embe = discord.Embed(title="Error",
                             description=":no_entry_sign: No tengo permisos, damelos <a:birb:846825232907239477> "":no_entry_sign:",
                             color=discord.Color.purple())
        await ctx.send(embed=embe)
