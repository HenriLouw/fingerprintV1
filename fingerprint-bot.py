import discord 
import requests
import json
import pyrebase
from discord import Color
from discord.ext import commands, tasks
from itertools import cycle
import time
import youtube_dl
import os


#Set Prefix
bot = commands.Bot(command_prefix = '.') 
status = cycle(['https://fingerprintza.com/', 'Visit our Twitter @fingerprintza', 'Register Today, fingerprintza.com/register-section','.commands'])
emojiF = ('<:Fingerprint:813383545065439253>')

#Set Message when Bot is online
@bot.event 
async def on_ready():
  change_status.start()
  print('Main Fingerprint ZA Bot is Online !')
 

#On error Command
@bot.event
async def on_command_error(ctx,error):
  if isinstance(error,commands.MissingPermissions):
    await ctx.send('You don\'t have the Permision to use this command 😕', delete_after = 5)
    await ctx.message.delete()
  elif isinstance(error,commands.MissingRequiredArgument):
    await ctx.send('Please enter all the required arguements ⌨️', delete_after = 5)
    await ctx.message.delete()
  elif isinstance(error,commands.CommandInvokeError):
    await ctx.send('Player Does not exist 😕', delete_after = 5)
    await ctx.message.delete()
  else:
    raise error

#Gets Information from Firebase
config = {
    "apiKey": "AIzaSyDZpGc9E2BhD_XMJcYlir2c_bRVoL--hJw",
    "authDomain": "fingerprint-za.firebaseapp.com",
    "databaseURL": "https://fingerprint-za-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "fingerprint-za",
    "storageBucket": "fingerprint-za.appspot.com",
    "messagingSenderId": "1099288539318",
    "appId": "1:1099288539318:web:5944ddd1eb25e0b58c7617",
    "measurementId": "G-5L8EW2MW4R"
}


#Embedded Player info
@bot.command() 
async def cs(ctx,player='ultrafy'):
  firebase = pyrebase.initialize_app(config)
  database = firebase.database()
  rootRef = database.child('counterstrike/pro').get()
  data = rootRef.val()

  playerU = player.upper()

  #try:
  myplayer = data[playerU]
    #await ctx.send('Showing Results for ' + myplayer)
  keyboard = myplayer['keyboard']
  mouse = myplayer['mouse']
  age = myplayer['age']
  fullname = myplayer['fullname']
  headset = myplayer['headset']
  resolution = myplayer['resolution']
  monitor = myplayer['monitor']
  monitor_hz = myplayer['monitor_hz']
  raw_input = myplayer['raw_input']
  sens = myplayer['sensitivity']
  team = myplayer['team']
  aspect_ratio = myplayer['aspect_ratio']
  dpi = myplayer['dpi']
  scaling_mode = myplayer['scaling_mode']
  zoom_sens = myplayer['zoom_sens']
  gamertag = myplayer['gamertag']
  crosshair_code = myplayer['crosshair_code']
  # faceit = myplayer['faceit']
  # esea = myplayer['esea']
  #except KeyError:
  # await ctx.send('User ' + myplayer + ' does not exist, contact support !')

  await ctx.send('Busy fetching data!', delete_after=3.0)  
  embed = discord.Embed(
    title = 'Player Information', 
    description = 'All Available data about the player is stated below.',
    colour = discord.Colour.teal()
  )

  embed.set_footer(text='Website: https://fingerprintza.com/ | Twitter: @fingerprintza ')
  embed.set_thumbnail(url='https://imgur.com/P1msmYz.png')
  embed.add_field(name= '**__Player:__**' , value= gamertag, inline=False)
  embed.add_field(name= '**__Player Information__**' , value= '**FullName:** ' + fullname + '\n**Player Team:** ' + team + '\n**Age:** ' + age, inline=False)
  embed.add_field(name= '**__Mouse Settings__**' , value= '**DPI:** ' + dpi + '\n**Sensitivity:** ' + sens + '\n**Raw Input:** ' + raw_input + '\n**Zoom Sensitivity:** ' + zoom_sens, inline=False)
  embed.add_field(name= '**__Monitor Settings__**' , value= '**Resolution:** ' + resolution + '\n**Aspect Ratio:** ' + aspect_ratio + '\n**Scaling Mode:** ' + scaling_mode + '\n**Hz:** ' +monitor_hz, inline=False)
  embed.add_field(name= '**__Crosshair__**' , value= '**Crosshair Code:** ' + crosshair_code , inline=False)
  embed.add_field(name= '**__Gear__**' , value= '**Monitor:** ' + monitor + '\n**Mouse:** ' + mouse + '\n**Keyboard:** ' + keyboard + '\n**Headset:** ' + headset, inline=False)
  embed.add_field(name= '**__Sponsors: __** ' , value= '- Tint Formulae | #FindYourHiddenEnergy | Use code fingerprint for 5' + '%' + ' off \n - FrostByte Network | @FrostByteZA', inline=False)

  await ctx.send(embed=embed)

@bot.command() 
async def fortnite(ctx,player='ultrafy'):
  firebase = pyrebase.initialize_app(config)
  database = firebase.database()
  rootRef = database.child('fortnite/pro').get()
  data = rootRef.val()

  playerU = player.upper()

  #try:
  myplayer = data[playerU]
    #await ctx.send('Showing Results for ' + myplayer)
  keyboard = myplayer['keyboard']
  mouse = myplayer['mouse']
  age = myplayer['age']
  fullname = myplayer['fullname']
  headset = myplayer['headset']
  resolution = myplayer['resolution']
  monitor = myplayer['monitor']
  monitor_hz = myplayer['monitor_hz']
  color_blind_mode = myplayer['color_blind_mode']
  sens = myplayer['sensitivity']
  team = myplayer['team']
  vsyncc = myplayer['vsyncc']
  dpi = myplayer['dpi']
  brightness = myplayer['brightness']
  scope_sens = myplayer['scope_sens']
  gamertag = myplayer['gamertag']
  fortnite_tracker = myplayer['fortnite_tracker']
  #binds
  ramp_bind = myplayer['ramp_bind']
  wall_bind = myplayer['wall_bind']
  cone_bind = myplayer['cone_bind']
  edit_bind = myplayer['edit_bind']
  floor_bind = myplayer['floor_bind']
  edit_release = myplayer['edit_release']
  # faceit = myplayer['faceit']
  # esea = myplayer['esea']
  #except KeyError:
  # await ctx.send('User ' + myplayer + ' does not exist, contact support !')

  await ctx.send('Busy fetching data!', delete_after=3.0)  
  embed = discord.Embed(
    title = 'Player Information', 
    description = 'All Available data about the player is stated below.',
    colour = discord.Colour.teal()
  )

  embed.set_footer(text='Website: https://fingerprintza.com/ | Twitter: @fingerprintza ')
  embed.set_thumbnail(url='https://imgur.com/P1msmYz.png')
  embed.add_field(name= '**__Player:__**' , value= gamertag, inline=False)
  embed.add_field(name= '**__Player Information__**' , value= '**FullName:** ' + fullname + '\n**Player Team:** ' + team + '\n**Age:** ' + age, inline=False)
  embed.add_field(name= '**__Mouse Settings__**' , value= '**DPI:** ' + dpi + '\n**Sensitivity:** ' + sens + '\n**Scope Sensitivity:** ' + scope_sens, inline=False)
  embed.add_field(name= '**__Monitor Settings__**' , value= '**Resolution:** ' + resolution + '\n**Color Blind Mode:** ' + color_blind_mode + '\n**Brightness:** ' + brightness + '\n**Hz:** ' +monitor_hz, inline=False)
  embed.add_field(name= '**__Fortnite Binds__**' , value= '**Ramp Bind:** ' + ramp_bind + '\n**Cone Bind:** ' + cone_bind + '\n**Floor Bind:** ' + floor_bind + '\n**Wall Bind:** ' + wall_bind , inline=False)
  embed.add_field(name= '**__Gear__**' , value= '**Monitor:** ' + monitor + '\n**Mouse:** ' + mouse + '\n**Keyboard:** ' + keyboard + '\n**Headset:** ' + headset, inline=False)
  embed.add_field(name= '**__Sponsors: __** ' , value= '- Tint Formulae | #FindYourHiddenEnergy | Use code fingerprint for 5' + '%' + ' off \n - FrostByte Network | @FrostByteZA', inline=False)

  await ctx.send(embed=embed)


@bot.command() 
async def counterstrikers(ctx):
  firebase = pyrebase.initialize_app(config)
  database = firebase.database()
  rootRef = database.child('counterstrike/pro').get()
  data = rootRef.val()
  await ctx.send('Getting Players!', delete_after=3.0)
  await ctx.send('***Players :***')
  for i in data:
    await ctx.send('`'+i+'`')
    time.sleep(2)
  
@bot.command() 
async def fortniters(ctx):
  firebase = pyrebase.initialize_app(config)
  database = firebase.database()
  rootRef = database.child('fortnite/pro').get()
  data = rootRef.val()
  await ctx.send('Getting Players!', delete_after=3.0)
  await ctx.send('***Players :***')
  for i in data:
    await ctx.send('`'+i+'`')
    time.sleep(2)


@bot.command(aliases =['commands'])
async def fingerprintcommands(ctx):
  await ctx.send('Getting Commands!', delete_after=3.0)  
  embed = discord.Embed(
    title = 'Commands', 
    description = 'All Available Commands.',
    colour = discord.Colour.teal()
  )

  embed.set_footer(text='Website: https://fingerprintza.com/ | Twitter: @fingerprintza ')
  embed.set_thumbnail(url='https://imgur.com/P1msmYz.png')
  embed.add_field(name= '**__.counterstrikers:__**' , value= 'Shows All CS Players In Database', inline=False)
  embed.add_field(name= '**__.fortniters:__**' , value= 'Shows All Fortnite Players In Database', inline=False)
  embed.add_field(name= '**__.fortnite + "player name"__**' , value= 'Shows Fortnite Player Specified After .fortnite Info', inline=False)
  embed.add_field(name= '**__.cs + "player name"__**' , value= 'Shows CS Player Specified After .cs Info', inline=False)
  embed.add_field(name= '**__.clear__** + **__amount__**' , value= 'Clears Specific amount of lines', inline=False)
  embed.add_field(name= '**__Sponsors: __** ' , value= '- Tint Formulae | #FindYourHiddenEnergy | Use code fingerprint for 5' + '%' + ' off \n - FrostByte Network | @FrostByteZA', inline=False)


  await ctx.send(embed=embed)





#Auto Role Command
@bot.event
async def on_raw_reaction_add(payload):
  message_id = payload.message_id
  if message_id == 805537263617703996:
    guild_id = payload.guild_id
    guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)

    if payload.emoji.name == 'Agree':
      role = discord.utils.get(guild.roles, name='Members')

    if role is not None:
      member = payload.member
      if member is not None:
        await member.add_roles(role)
        print('Done')
      else:
        print('Member not found.')


#Purge command
@bot.command(aliases =['p','purge','delete'])
async def clear(ctx, amount=3):
    await ctx.channel.purge(limit=amount)
    embed = discord.Embed(
     title = 'FingerPrintZa', 
     description =  'FingerPrintZa Bot Cleared: ' + '`' + str(amount) + '`' + ' messages' + emojiF,
     colour = discord.Colour.teal()
  )
    await ctx.send(embed=embed, delete_after=3.0)



#Testing Command
@bot.command()
async def Testing(ctx):
 msg = await ctx.send(':Statusgreen:')
 await msg.add_reaction('<:Statusgreen:805475295573442560>')

#Testing2
@bot.command() 
async def Testing2(ctx):
  await ctx.send('Busy fetching data!', delete_after=3.0)
  
  embed = discord.Embed(
    title = 'Your Title', 
    description =  'Your Description [Twitter](https://twitter.com/MrT1TAN)',
    colour = discord.Colour.blue()
  )
  await ctx.send(embed=embed)

#StatusgreenCommand
@bot.command() 
@commands.has_permissions(manage_messages = True)
async def Statusgreen(ctx):
  channel = bot.get_channel(805159215370076191)
  embed = discord.Embed(
    title = 'ZA FingerPrint Status', 
    description =  '',
    colour = discord.Colour.green()
  )
  embed.set_thumbnail(url='https://imgur.com/P1msmYz.png')
  embed.add_field(name='**Status:**', value='\n **All ZA FingerPrint Services are currently running** 🟢 ', inline=True)
  await channel.send(embed=embed)

@bot.command()
async def invite(ctx):
  embed = discord.Embed(
    title = 'ZA FingerPrint Status', 
    description =  'Invite link to invite the bot to your server',
    colour = discord.Colour.teal()
  )
  embed.set_footer(text='Website: https://fingerprintza.com/ | Twitter: @fingerprintza | Sponsored by: TINTFORMULAE')
  embed.set_thumbnail(url='https://imgur.com/P1msmYz.png')
  embed.add_field(name='**Invite Link:**', value='\n **https://discord.com/api/oauth2/authorize?client_id=805461368055529502&permissions=0&scope=bot** ', inline=True)
  await ctx.send(embed=embed)


#StatusredCommand
@bot.command() 
@commands.has_permissions(manage_messages = True)
async def Statusred(ctx):
  channel = bot.get_channel(805159215370076191)
  embed = discord.Embed(
    title = 'ZA FingerPrint Status', 
    description =  '',
    colour = discord.Colour.red()
  )
  embed.set_thumbnail(url='https://imgur.com/P1msmYz.png')
  embed.add_field(name='**Status:**', value='\n **Some ZA FingerPrint Services are currently not Running. Don\'t worry. The team is busy working on a fix** 🔴 ', inline=True)
  await channel.send(embed=embed)

#Set Bot status
@tasks.loop(seconds=15)
async def change_status():
  await bot.change_presence(activity=discord.Game(next(status)))

#Discord Rules Embed
@bot.command() 
@commands.has_permissions(administrator = True)
async def Rules(ctx):
  embed = discord.Embed(
    title = 'ZaFingerPrint Server Rules', 
    description =  'Please Respect and Obey the Server',
    colour = discord.Colour.teal()
  )

  embed.set_footer(text='Made by MrT1TAN#3244')
  embed.set_thumbnail(url='https://imgur.com/P1msmYz.png')
  embed.set_author(name='MrT1TAN#3244', 
  icon_url='https://imgur.com/YoOQFrW.png')
  embed.add_field(name='Rule #1: **__NSFW Content__**', value='Any form of NSFW content is strictly forbidden, if you are found posting content of this nature, you will be banned on the spot.', inline=False)
  embed.add_field(name='Rule #2: **__Advertising__**', value='No advertising of any kind (Discord, YouTube, Twitter, Etc). If you are found advertising, this is also grounds for an immediate ban.', inline=False)
  embed.add_field(name='Rule #3: **__Defamation Behavior__**', value='Absolutely no Racist, Sexist, or otherwise degrading behavior will be tolerated. Anyone displaying this behavior will be banned.', inline=False)
  embed.add_field(name='Rule #4: **__Mentions__**', value='Repeated pings will result in a mute, kick, or even ban.', inline=False)
  embed.add_field(name='Rule #5: **__Discord Terms of Service__**', value='You must be at least 13 years old to use Discord, and raiding, illegal activities, attempting to obtain personal information, and all other prohibited acts will result in punishment.', inline=False)
  embed.add_field(name='Rule #6: **__Do not spam!__**', value='Avoid excessive and/or unnecessary messages, caps, emojis, text walls, spoiler messages, chains, images and @mentions. This includes unwarranted tags and derailing conversations.', inline=False)
  embed.add_field(name='Rule #7: **__Be respectful and accepting towards other members.__**', value='No instances of personal attacks, disrespect, exclusion, harassment, slurs, doxxing, or arguments should occur here. Treat everyone as if they\'re your equal. Don\'t try to act like a staff member or as if you have staffing ability if you don\'t have the role.', inline=False)
  embed.add_field(name= '**__Sponsors: __** ' , value= '- Tint Formulae | #FindYourHiddenEnergy | Use code fingerprint for 5' + '%' + ' off \n - FrostByte Network | @FrostByteZA', inline=False)

  msg = await ctx.send(embed=embed)
  await msg.add_reaction('<:agree:805537012161314816>')
 #########################################################################################
 #########################################################################################
 #########################################################################################
#########################################################################################
 #Music

@bot.command()
async def play(ctx, url : str, channel='General'):
  song_there = os.path.isfile('song.mp3')
  try:
    if song_there:
      os.remove('song.mp3')
  except PermissionError:
    await ctx.send('Wait for current song to end. YOu can use !stop')
    return
  #channel = guild.get_channel(‘your-channel-Id’)
  voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=channel)
  await voiceChannel.connect()
  voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
  

  ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
      'key': 'FFmpegExtractAudio',
      'preferredcodec': 'mp3',
      'preferredquality': '192'
    }],
  }
  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
  for file in os.listdir('./'):
    if file.endswith('.mp3'):
      os.rename(file, 'song.mp3')
  
  voice.play(discord.FFmpegPCMAudio('song.mp3'))

@bot.command()
async def leave(ctx):
  voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
  if voice.is_connected():
    await voice.disconnect()
  else:
    await ctx.send('The bot is not currently connected to a VC.')

@bot.command()
async def pause(ctx):
  voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
  if voice.is_playing():
    voice.pause()
  else:
    await ctx.send('No audio is currently playing')

@bot.command()
async def resume(ctx):
  voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
  if voice.is_paused():
    voice.resume()
  else:
    await ctx.send('No audio is already playing')

@bot.command()
async def stop(ctx):
  voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
  voice.stop()


bot.run('ODA1NDYxMzY4MDU1NTI5NTAy.YBbOWg.ga2Xakk4ddaD3m0x7sBN_UIn2GQ')