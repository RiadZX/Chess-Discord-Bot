import discord
from discord import app_commands 
import data
import scraper
import chess
import os
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

DataHandler = data.Data()
ChessHandler = chess.Chess()


# CREATE CLIENT
class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.default())
        self.synced = False #we use this so the bot doesn't sync commands more than once

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: #check if slash commands have been synced 
            await tree.sync() #guild specific: leave blank if global (global registration can take 1-24 hours)
            self.synced = True
        print(f"We have logged in as {self.user}.")

client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(name="statistics",description="Get statistics about a user")
async def get_stats(interaction: discord.Interaction, user: str):
    await interaction.response.defer(ephemeral = False)

    exists = DataHandler.check_user_existence(interaction.user.id)
    if not exists:
        await interaction.followup.send("You must register your account first!")
        return
    
    profile = DataHandler.load_user_profile(interaction.user.id)
    stats = ChessHandler.get_stats(profile)

    embed = discord.Embed(title = "Statistics", description = "Statistics for " + profile, color = 0x00ff00)
    try:
        #seperator
        embed.add_field(name = "\u200b", value = "\u200b", inline = False)
        embed.add_field(name = "Bullet Rating", value = stats["bulletRating"], inline = True)
        embed.add_field(name = "Bullet Games", value = stats["bulletGames"], inline = True) 
    except:
        pass
    try:
        embed.add_field(name = "\u200b", value = "\u200b", inline = False)
        embed.add_field(name = "Blitz Rating", value = stats["blitzRating"], inline = True) 
        embed.add_field(name = "Blitz Games", value = stats["blitzGames"], inline = True)   
    except:
        pass

    try:
        embed.add_field(name = "\u200b", value = "\u200b", inline = False)
        embed.add_field(name = "Rapid Rating", value = stats["rapidRating"], inline = True) 
        embed.add_field(name = "Rapid Games", value = stats["rapidGames"], inline = True)   
    except:
        pass





    await interaction.followup.send(embed=embed)

@tree.command(name="register",description="Register your account")
async def register(interaction: discord.Interaction, profile: str):
    await interaction.response.defer(ephemeral = False)
    DataHandler.save_user_profile(interaction.user.id, profile)

    await interaction.followup.send("Registered: " + profile)
    


client.run(DISCORD_TOKEN)