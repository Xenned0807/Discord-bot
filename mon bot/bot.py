import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

# Charger les variables du .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise ValueError("❌ Le token Discord est introuvable. Ajoute-le dans le fichier .env ou dans les variables Railway.")

# Activer les intents
intents = discord.Intents.default()
intents.members = True
intents.presences = True

# Créer l'instance du bot
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Connecté en tant que {bot.user} !")

@bot.event
async def on_disconnect():
    print("⚠️ Bot déconnecté, tentative de reconnexion...")

@bot.event
async def on_resumed():
    print("♻️ Session Discord reprise.")

# Exemple de commande
@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong !")

# Lancer le bot
bot.run(TOKEN)
