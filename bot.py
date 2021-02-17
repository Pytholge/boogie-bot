import discord
from discord.ext import commands

import random

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '.', intents = intents)



@client.event
async def on_ready():
    print('Kiss my entire giant fatass!')

@client.event
async def on_member_join(member):
    print(f'Hi {member}, kiss my giant fatass!')

@client.event
async def on_member_remove(member):
    print(f'Bye, {member}, you con artist!')

@client.command()
async def boog(ctx):
    response = ['Kiss my entire giant fatass!',
                "No, you're the fatass!",
                'No!',
                'Fix this shit, you con artists!',
                "You're the fatass!",
                "No, don't take my fuckin' iPad!",
                "Hey guys, it's me, Francis!",
                "Did you drink my Mountain Dew?",
                "Lemme smell your breath!",
                "Ohhh, you Mountain Dew drinkin' bitch!",
                "There might only be one fucking diaper in a fucking landfill, that may be fucking rare, but it’s still a piece of fucking shit!"]

    random_message = random.choice(response)

    await ctx.send(random.choice(response))
    

@client.command()
async def me(ctx):
    images = ["boogie/boog1.jpg",
              "boogie/boog2.jpg",
              "boogie/boog3.jpg",
              "boogie/boog4.jpg",
              "boogie/boog5.jpg",
              "boogie/boog6.png",
              "boogie/boog7.jpg",
              "boogie/boog8.jpg",
              "boogie/boog9.jpg",
              "boogie/boog10.jpg",
              "boogie/boog11.jpg",
              "boogie/boog12.jpg",
              "boogie/boog13.jpg",
              "boogie/boog14.jpg"]

    random_image = random.choice(images)

    await ctx.send(file=discord.File(random_image))
    
    

    
    
client.run('Njk2MjE4MDgxMDU5NTM2OTM2.XolhnQ.AsPuVspLTbqPx2asmtyy9szAm-Q')
