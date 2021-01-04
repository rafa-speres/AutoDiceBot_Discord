import discord
import os
import random as r
from keep_me_alive import keep_alive

client = discord.Client()

help_msg = "Os valores de dados disponíveis são 4, 6, 10, 12, 20 e 100 lados.\nPara escolher o dado desejado escreva &d(valor_dos_dados_desejado)"

greeting = "Olá humano eu sou o AutoDiceBot, para informações sobre como jogar comigo digite &ajuda"

def random_values(max_value):
  value = r.randint(0, max_value)
  return value

@client.event
async def on_ready():
  print("Logged as AutoDiceBot")

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith("&dicebot"):
    await message.channel.send(greeting)

  if message.content.startswith("&ajuda"):
    await message.channel.send(help_msg)

  if message.content.startswith("&d4"):
    await message.channel.send("jogando um D4")
    value = random_values(4)
    await message.channel.send(value)
  
  if message.content.startswith("&d6"):
    await message.channel.send("jogando um D6")
    value = random_values(6)
    await message.channel.send(value)

  if message.content.startswith("&d10") and not message.content.startswith("&d100"):
    await message.channel.send("jogando um D10")
    value = random_values(10)
    await message.channel.send(value)

  if message.content.startswith("&d12"):
    await message.channel.send("jogando um D12")
    value = random_values(12)
    await message.channel.send(value)

  if message.content.startswith("&d20"):
    await message.channel.send("jogando um D20")
    value = random_values(20)
    await message.channel.send(value)

  if message.content.startswith("&d100"):
    await message.channel.send("jogando um D100")
    value = random_values(100)
    await message.channel.send(value)
  
keep_alive()
client.run(os.getenv("PASS"))
