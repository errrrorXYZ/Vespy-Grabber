class ErrorMsg:

    def __init__(self):
        error = ""
        ctypes.windll.user32.MessageBoxW(None, error, 'Fatal Error', 2)
