import discord 
from discord.ext import commands
import openai

intents = discord.Intents.default()
intents.message_content = True  

bot = commands.Bot(command_prefix="!",intents=intents)

# Open-ai API Key temp key because it is free 😅
openai.api_key = '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' 

def chat_with_gpt(message):
    conversation = [
        {'role': 'user', 'content': message}
    ]

    # Set up the conversation history 
    user_message = conversation[-1]['content']

    # Generate a response from ChatGPT
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=user_message,
        max_tokens=200
    )

    # Extract and return the generated response
    reply = response.choices[0].text.strip()
    return reply

@bot.event
async def on_ready():
    # bot.guilds are the servers in which bot is connected 
    print(f"Bot is online. Connected to {len(bot.guilds)} server(s).")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.startswith("!hello") or message.content.startswith("! hello") or message.content.startswith("! Hello") or message.content.startswith("!Hello") :
        await message.channel.send("Hello, I'm your Discord bot!")

    elif message.content.startswith("!your owner") or message.content.startswith("!owner") :
        await message.channel.send("Nobody is my owner but my creator is shaan thakkar")
    
    elif message.content.startswith("!"):
        # Chat with GPT when a message is received 
        reply = chat_with_gpt(message.content)

        # Send the generated response as a message to the Discord channel
        await message.channel.send(reply)

@bot.event
async def on_member_join(member):
    welcome_channel = bot.get_channel(1117104429645176964)  # channel id is given to the bot
    await welcome_channel.send(f"Welcome, {member.mention}!")

@bot.event
async def on_reaction_add(reaction, user):
    if reaction.emoji == "👍":
        await reaction.message.channel.send(f"{user.name} reacted with a thumbs up!")

# bot id and run function starts the bot through it's id 
bot.run('MTExNjk5MDQzODk0NDAxODUxMg.GOLOxu.6cBUjdFA27wZdZV9-OL9yTOtgwSG3ozI8CsJKU') 

