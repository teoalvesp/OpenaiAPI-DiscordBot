import openai
import discord
from config.config import API_KEY, TOKKEN_DISCORD

openai.api_key = API_KEY

intents = discord.Intents(messages=True)
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} bot conectado no discord')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    print()
    response = await prompt(message.content)
    response_text = response.choices[0].text
    
    for chunk in split_response(response_text):
        await message.channel.send(chunk)

def split_response(text, chunk_size=2000):
    """Divide uma resposta em pedaços menores para enviar no Discord"""
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

async def prompt(message):
    prompt = message
    print(message)

    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1000,
    n=1,
    stop=None,
    temperature=0.5,
)
    return response

client.run(TOKKEN_DISCORD)

