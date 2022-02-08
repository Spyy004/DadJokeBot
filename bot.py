import os
from dotenv import load_dotenv
import nextcord
import requests
from nextcord.ext import commands
load_dotenv()

bot = commands.Bot(command_prefix=" ")

GUILD_IDS = os.getenv("GUILD_IDS")
gID = [int(GUILD_IDS)]
            
@bot.slash_command(description="Get a DAD Joke", guild_ids=gID)
async def joke(interaction):
    
    await interaction.send(await on_message("joke"))


async def on_message(message:str):
    url = "https://dad-jokes.p.rapidapi.com/random/joke"
    APIKEY = os.getenv("APIKEY")
    headers = {
    'x-rapidapi-host': "dad-jokes.p.rapidapi.com",
    'x-rapidapi-key': APIKEY
    }

    response = requests.request("GET", url, headers=headers)

    jokeData = response.json()

    joke1 = jokeData['body'][0]['setup']
    joke2 = jokeData['body'][0]['punchline']
    joke = joke1 + '\n' + joke2
    return joke
bot.run(os.getenv("TOKEN"))





