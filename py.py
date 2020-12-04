import discord
from discord.ext import commands
import sys
import os
import requests
import json
import json
import math
import cv2
import numpy as np
import urllib
import cv2
from urllib.request import urlopen
import os
from io import StringIO  # Python3
from urllib import request, parse
import random
from discord import Webhook, AsyncWebhookAdapter
import aiohttp

ez = ["Wait... This isn't what I typed!",
"Anyone else really like Rick Astley?",
"Hey helper, how play game?",
"Sometimes I sing soppy, love songs in the car.",
"I like long walks on the beach and playing Hypixel",
"Please go easy on me, this is my first game!",
"You're a great person! Do you want to play some Hypixel games with me?",
"In my free time I like to watch cat videos on Youtube",
"When I saw the witch with the potion, I knew there was trouble brewing.",
"If the Minecraft world is infinite, how is the sun spinning around it?",
"Hello everyone! I am an innocent player who loves everything Hypixel.",
"Plz give me doggo memes!",
"I heard you like Minecraft, so I built a computer in Minecraft in your Minecraft so you can Minecraft while you Minecraft",
"Why can't the Ender Dragon read a book? Because he always starts at the End.",
"Maybe we can have a rematch?",
"I sometimes try to say bad things then this happens :(",
"Behold, the great and powerful, my magnificent and almighty nemisis!",
"Doin a bamboozle fren.",
"Your clicks per second are godly. :eek:",
"What happens if I add chocolate milk to macaroni and cheese?",
"Can you paint with all the colors of the wind",
"Blue is greener than purple for sure",
"I had something to say, then I forgot it.",
"When nothing is right, go left.",
"I need help, teach me how to play!",
"Your personality shines brighter than the sun.",
"You are very good at the game friend.",
"I like pineapple on my pizza",
"I like pasta, do you prefer nachos?",
"I like Minecraft pvp but you are truly better than me!",
"I have really enjoyed playing with you! <3",
"ILY <3",
"Pineapple doesn't go on pizza!",
"Lets be friends instead of fighting okay?"
]


bot = commands.Bot(command_prefix='.')
bot.remove_command("help")

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')



@bot.command()
async def analyze(ctx):
	extract = ctx.message.attachments
	extract = str(extract)
	x = extract
	x = x.replace("<", "")
	x = x.replace(">", "")
	x = x.replace("\'", "")
	x = x.replace("<", "")
	x = x.replace("id", "\"id\"")
	x = x.replace("filename", "\"filename\"")
	x = x.replace("url", "\"url\"")
	x = x.replace("Attachment ", "")
	x = x.replace(" ", ", ")
	x = x.replace("\,", "\"\, ")
	x = x.replace("=", ":")
	x = x.replace(":", ":\"")
	x = x.replace(",", "\",")
	x = x.replace("g]", "g\"]")
	x = x.replace("[", "{")  
	x = x.replace("]", "}")
	x = x.replace("https:\"//", "")
	x = json.loads(x)
	if str(x) != "{}":
		z=(x['url'])
		z = "https://"+str(z)
	print(z)

	files = {
	        'api_key': (None, 'bXOWX8Xc9csAF0AJp6UB3bo2K0tJDKwH'),
	        'api_secret': (None, 'vQwCJGK5ue2bBqRTsa_P80yCY7411Vw1'),
	        'image_url': (None, z),
	        'return_attributes': (None, 'gender,age,ethnicity,emotion,age,glass'),
	    }

	response = requests.post('https://api-us.faceplusplus.com/facepp/v3/detect', files=files)
	response = response.content
	response = json.loads(response)
	print(response)
	car = response['faces'][0]['attributes']
	gender = car['gender']['value']
	emotion = car['emotion']
	age = car['age']['value']
	print(emotion)
	top = 0
	best = ""
	for i in emotion:
		print(emotion[i])
		if emotion[i]>top:
			top=emotion[i]
			best = i
	print(best)
	print(top)
	top = str(top)

	embedVar = discord.Embed(title="Recognition", description="Features", color=0x9900FF)
	embedVar.add_field(name="gender", value=gender, inline=False)
	embedVar.add_field(name="Emotion", value=best+":  "+top+"%", inline=False)
	embedVar.add_field(name="Age(estimated)", value=age, inline=False)
	embedVar.set_thumbnail(url=z)
	await ctx.send(embed=embedVar)


@bot.event
async def on_message(message):
	if message.author.id == 566904870951714826:
		print("talk")
		await message.add_reaction("🤡")

@bot.command()
async def detect(ctx):

	extract = ctx.message.attachments
	extract = str(extract)
	x = extract
	x = x.replace("<", "")
	x = x.replace(">", "")
	x = x.replace("\'", "")
	x = x.replace("<", "")
	x = x.replace("id", "\"id\"")
	x = x.replace("filename", "\"filename\"")
	x = x.replace("url", "\"url\"")
	x = x.replace("Attachment ", "")
	x = x.replace(" ", ", ")
	x = x.replace("\,", "\"\, ")
	x = x.replace("=", ":")
	x = x.replace(":", ":\"")
	x = x.replace(",", "\",")
	x = x.replace("g]", "g\"]")
	x = x.replace("[", "{")  
	x = x.replace("]", "}")
	x = x.replace("https:\"//", "")
	x = json.loads(x)
	if str(x) != "{}":
		z=(x['url'])
		p = "https://"+str(z)

	try:
		os.delete("testrip.png")
	except:
	      pass
	#perform request
	# perform request
	response =  requests.get(p).content
	# convert to array of ints
	nparr = np.frombuffer(response, np.uint8)
	# convert to image array
	img = cv2.imdecode(nparr,cv2.IMREAD_UNCHANGED)
	cv2.imwrite("testrip.png", img)
	# Load the cascade
	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
	# Read the input image
	img = cv2.imread("testrip.png")
	# Convert into grayscale
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	# Detect faces
	faces = face_cascade.detectMultiScale(gray, 1.1, 4)
	# Draw rectangle around the faces
	for (x, y, w, h) in faces:
	    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
	# Display the output
	cv2.imwrite("testrip.png", img)
	
	await ctx.send(file=discord.File('testrip.png'))


bot.run('NzI5MDIyOTc0MTk5MzMyOTc1.XwC5jQ.4nHZqWhEJzLFFr5pheRH_XrPGMU')
