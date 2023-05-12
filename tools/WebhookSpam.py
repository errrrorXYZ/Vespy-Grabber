import requests
from discord_webhook import DiscordWebhook, DiscordEmbed
from time import sleep

def spamthatwebhook(wbh,content:str,threads:int,embed_content):
    if embed_content[0] == "No":
        webhook = DiscordWebhook(url=wbh,content=content)
        for _ in range(threads):
            r=webhook.execute()
            if r.status_code == 200 or r.status_code == 204:
                pass
            elif r.status_code == 429:
                sleep(r.json()['retry_after'] / 1000)
            elif r.status_code == 404:
                break
    else:
        title = embed_content[1]
        desc = embed_content[2]
        color = embed_content[3]
        color = str(color).replace("#","")
        img = embed_content[4]
        webhook = DiscordWebhook(url=wbh,content=content)
        embed = DiscordEmbed(title=title, description=desc, color=color)
        if len(img) > 2:
            embed.set_image(url=img)
        webhook.add_embed(embed)
        for _ in range(threads):
            r=webhook.execute()
            if r.status_code == 200 or r.status_code == 204:
                pass
            elif r.status_code == 429:
                sleep(r.json()['retry_after'] / 1000)
            elif r.status_code == 404:
                break

def deletewebhook(webhook):
    try:
        requests.delete(webhook)
    except:
        pass


