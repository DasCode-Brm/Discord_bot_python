import random

from discord.ext import commands
from prefix import bot


@bot.command()
async def com(ctx, num1="", m="", num2=""):
    usuario = ctx.message.author
    if m != ";":
        await ctx.send(f"Estimado {usuario}, use el separador de argumentos ';',    ejemplo: x ; x :relaxed:")

    elif (num1 == "") or (num2 == ""):
        await ctx.send(f"Estimado {usuario}, necesita al menos dos argumentos ")

    else:
        if len(num1) == len(num2):
            await ctx.send("las dos cadenas tienen la misma cantidad son del mismo tamaño")
        else:
            await ctx.send("las dos cadenas tienen diferente tamaño")


c, i = 0, 0


@bot.command()
async def ppt(ctx, game=""):
    global c, i
    d = ctx.message.id
    if game == "":
        await ctx.send("Escribe por lo menos un argumento")
        return

    a = ["piedra", "papel", "tijera"]
    b = random.choices(a)
    for c in b:
        print(c)
    game = game.lower()
    if game == c:
        await ctx.send("Empate")

    elif (game == "tijera") and (c == "papel"):
        await ctx.send(f"pusiste: {game}, y yo: {c}, por lo tanto ganaste")
        i += 1

    elif (game == "piedra") and (c == "tijera"):
        await ctx.send(f"pusiste: {game}, y yo: {c}, por lo tanto ganaste")
        i += 1
    elif (game == "papel") and (c == "tijera"):
        await ctx.send("perdiste")

    elif (game == "tijera") and (c == "piedra"):
        await ctx.send("perdiste")

    elif (game == "piedra") and (c == "papel"):
        await ctx.send(f"pusiste: {game}, y yo: {c}, por lo tanto ganaste")
        i += 1
    elif (game == "papel") and (c == "piedra"):
        await ctx.send(f"pusiste: {game}, y yo: {c}, por lo tanto ganaste")
        i += 1


@bot.command()
async def score(ctx):
    global i
    c = ctx.message.author
    cc = bot.user.name
    await ctx.send(f"{i}: {c} y {cc}")
