class Hide:

    def __init__(self):
        self.file = sys.argv[0]
        self.hide(self.file)

    def hide(self,f):
        try:
            subprocess.check_call(["attrib","+H",f])
        except:
            pass