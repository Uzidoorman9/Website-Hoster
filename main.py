import os
import threading
from flask import Flask
import discord
from discord.ext import commands

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from the Flask server!"

# Setup discord bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

def run_flask():
    # Run Flask app on port 5000, accessible from outside (host=0.0.0.0)
    app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    # Start Flask in a new thread
    threading.Thread(target=run_flask).start()
    # Run Discord bot (blocks main thread)
    bot.run(os.getenv("DISCORD_BOT_TOKEN"))

