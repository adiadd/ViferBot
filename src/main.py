from array import array
from ast import Bytes
import discord
import os
from discord.ext import commands
import random
from dotenv import load_dotenv
import dataa
from arrayData import arrayImages
#import tensorflow as tf
from PIL import Image
from random import randrange
import requests
import io
import torch
import torchvision.transforms as T
import base64

load_dotenv() 

API_KEY=os.getenv('API_KEY')
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

#TODO: randomly crop a part of the image
def random_crop(image):
  
  left = 0
  top = 50
  right = 510
  bottom = 292

  img_res = image.crop((left, top, right, bottom)) 
  #cropped_image = tf.image.random_crop(image, size=[100, 100, 3])
  return img_res

#TODO: Check if the value entered is the same as the name of the image given
#def crossCheck(val):
  #if val == 

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
       
    #embed.set_image(url=random.choice(list(dataa.dictImages.items())))
    #embed.set_image(url=random.choice(arrayImages[1]))

    # byteImgIO = io.BytesIO()
    # byteImg = Image.open("some/location/to/a/file/in/my/directories.png")
    # byteImg.save(byteImgIO, "PNG")
    # byteImgIO.seek(0)
    # byteImg = byteImgIO.read()

    embed = discord.Embed(title="Guess which character this is:")

    def pillow_image_to_base64_string(img):
      buffered = io.BytesIO()
      img.save(buffered, format="JPEG")
      return base64.b64encode(buffered.getvalue()).decode("utf-8")


    def base64_string_to_pillow_image(base64_str):
        return Image.open(io.BytesIO(base64.decodebytes(bytes(base64_str, "utf-8"))))


    # Example for Converting pillow image to base64 data URL to view in browser
    
    # You can put this data URL in the address bar of your browser to view the image

    url=random.choice(arrayImages)
    print("url: ", url)
    response = requests.get(url)
    img = Image.open(io.BytesIO(response.content)).convert('RGB')
    print("image format: ",img.format)

    transform = T.RandomCrop((300,300))
    img = transform(img)
    print("show image")
    print("image cropped format", img.format)
    img.show()
    print(img)
    print("Image mode: ", img.mode)

    # Send image to embed and send embed to response
    embed.set_image(url=img)
    await message.channel.send(embed=embed)



client.run(os.getenv('TOKEN'))