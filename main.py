import discord
import os
from discord.ext import commands
import random
from dotenv import load_dotenv

load_dotenv() 

#bot = commands.Bot(command_prefix='$')

client = discord.Client()

imagesDict = {
  "Haze":"https://gamepress.gg/arknights/sites/arknights/files/2019-11/char_141_nights_2.png",
  "Gitano":'https://gamepress.gg/arknights/sites/arknights/files/2019-11/char_109_fmout_2.png',
  "Jessica":'https://gamepress.gg/arknights/sites/arknights/files/2019-11/char_235_jesica_2.png'
}

def validate_image(imageName):
  for the_key, the_value in imagesDict.items():
    if imageName.lower() == the_key:
      return True
      break

# def random_crop(image):
#  cropped_image = tf.image.random_crop(
#      image, size=[100, 100, 3])

#  return cropped_image

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

  
#@bot.command()
#async def test(ctx, arg):
#  await ctx.send(arg)

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith("$random"):
    embed = discord.Embed(title="Guess which character this is:")

    
    embed.set_image(url=random.choice(list(imagesDict.items()))[1])
    await message.channel.send(embed=embed)



client.run(os.getenv('TOKEN'))