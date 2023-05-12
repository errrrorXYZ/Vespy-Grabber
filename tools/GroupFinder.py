import random
import requests
from threading import Thread
from discord_webhook import DiscordWebhook, DiscordEmbed

class Groupfind:

    def __init__(self,webhook,threads:int,proxy:bool):
        self.myproxy = None
        self.webhook = webhook
        self.threads = threads
        self.proxy = proxy
        if self.proxy:
            self.myproxy = open("proxy.txt").read().strip()
            self.myproxy = {"http":f"http://{self.myproxy}", "https":f"http://{self.myproxy}"}
        for _ in range(100):
            Thread(target=self.GEN).start()

    def GEN(self):
        TTT = int(self.threads / 100)
        for _ in range(TTT):
            try:
                ID = random.randint(1000000, 18000000)
                if self.proxy:
                    r = requests.get(f"https://www.roblox.com/groups/group.aspx?gid={ID}",proxies=self.myproxy)
                else:
                    r = requests.get(f"https://www.roblox.com/groups/group.aspx?gid={ID}")
                if 'owned' not in r.text:
                    if self.proxy:
                        r2 = requests.get(f"https://groups.roblox.com/v1/groups/{ID}",proxies=self.myproxy)
                    else:
                        r2 = requests.get(f"https://groups.roblox.com/v1/groups/{ID}")
                    if 'isLocked' not in r2.text and 'owner' in r2.text:
                        if r2.json()['publicEntryAllowed'] == True and r2.json()['owner'] == None:
                            webhook = DiscordWebhook(url=self.webhook, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png")
                            embed = DiscordEmbed(title=f"Group Unowned Found", description=f"https://www.roblox.com/groups/group.aspx?gid={ID}", color='4300d1')
                            embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png')
                            embed.set_footer(text='Vespy 2.0 | by : vesper')
                            embed.set_timestamp()
                            webhook.add_embed(embed)
                            webhook.execute()
            except:
                pass