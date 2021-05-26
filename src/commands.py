import discord
# from discord import activity
from discord.ext import commands, tasks
from prefix import bot
from datetime import datetime, timedelta, date


@bot.command(name="carr")
async def carr(ctx):
    user = ctx.message.author.id
    usuario = ctx.message.author
    await ctx.send("hola {0.mention}, {1}".format(usuario, user))
    await bot.delete_message(ctx)


@bot.command()
async def message():
    print()


@bot.command(aliases=["cls"])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, m=""):
    if m == "":
        embes = discord.Embed(description="<a:no:846822577666392094> Requiere un argumento <a:no:846822577666392094> ",
                              color=discord.Color.red())
        await ctx.send(embed=embes)
        return
    await ctx.message.delete()
    m = int(m)
    d = await ctx.channel.purge(limit=m)
    embed = discord.Embed(title="Aviso", description="{0} mensajes borrados".format(len(d)), color=discord.Color.red())
    await ctx.send(embed=embed, delete_after=5)


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title="Error", description=":no_entry_sign: No tienes permisos :no_entry_sign:",
                              color=discord.Color.purple())
        await ctx.send(embed=embed)

    if isinstance(error, commands.errors.CommandInvokeError):
        embe = discord.Embed(title="Error",
                             description=":no_entry_sign: No tengo permisos, damelos <a:birb:846825232907239477> "":no_entry_sign:",
                             color=discord.Color.purple())
        await ctx.send(embed=embe)
