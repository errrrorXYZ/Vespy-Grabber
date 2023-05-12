import requests
from discord_webhook import DiscordWebhook, DiscordEmbed
def stealclothes(webhooky,id):
        r=requests.get(f"https://assetdelivery.roblox.com/v1/assetId/{id}")
        if 'errors' in r.json():
            pass
        else:
            webhook = DiscordWebhook(url=webhooky, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png")
            XML = r.json()['location']
            r2=requests.get(XML)
            JUIC = str(r2.content)
            IDD = str(JUIC.split("<url>http://www.roblox.com/asset/?id=")[1].split("</url>")[0])
            SOP = str(JUIC.split('<string name="Name">')[1].split("</string>")[0])
            if SOP == "Shirt":aaa = "s"
            else:aaa="p"
            r3=requests.get(f"https://www.roblox.com/library/{IDD}").text
            URLL = r3.split("""<span class="thumbnail-span" ><img  class='' src='""")[1].split("'")[0]
            TITLE = str(r3.split("<title>")[1].split("</title>")[0]);TITLE = TITLE.replace(" ","_")
            if aaa == "s":
                embed = DiscordEmbed(title=f"SHIRT Stolen", description=f"``{TITLE}``", color='4300d1')
                embed.set_image(url=URLL)
            else:
                embed = DiscordEmbed(title=f"PANTS Stolen", description=f"``{TITLE}``", color='4300d1')
                embed.set_image(url=URLL)
            embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png')
            embed.set_footer(text='Vespy 2.0 | by : vesper')
            embed.set_timestamp()
            webhook.add_embed(embed)
            webhook.execute()