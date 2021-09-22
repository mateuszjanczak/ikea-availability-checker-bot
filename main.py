import os
import discord
from time import time, sleep
from webbot import Browser
from keep_alive import keep_alive

userId = int(os.environ['userId'])
channelId = int(os.environ['channelId'])
token = os.environ['token']
ikeaProductUrl = os.environ['ikeaProductUrl']
intervalInSeconds = int(os.environ['intervalInSeconds'])

client = discord.Client()
web = Browser(showWindow = False)

def checkProductStatus():
  web.go_to(ikeaProductUrl)
  status = web.exists(text = 'Produkt dostępny')
  if status == True:
    return 'Jest %s <@!%s>' % (ikeaProductUrl, userId)
  else:
    return 'Nie ma'

@client.event
async def on_ready():
  channel = client.get_channel(channelId)
  await channel.send("obudzony, ale jakim kosztem... :joy_cat:")
  await channel.send("monitoruję produkt = %s" % ikeaProductUrl)
  while True:
    sleep(intervalInSeconds - time() % intervalInSeconds)
    await channel.send(checkProductStatus())

keep_alive()
client.run(token)