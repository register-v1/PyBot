from core.bot_class import Bot

commands = {
    "help": {"func": "bot_help"},
    "authors": ["Credits for GPL development of this bot goes to r0073d, Woz & v1"],
    "version": ["The current version is 1.3 Use &help to get some more information."],
    "whypy3": ["0. There are many improvements made in python3 you will not find in python2.",
               "1. Socket handling, threading, better standard lib, the list goes on.",
               "2. Realize that if you learn 2.7.5, you will be almost 10 revisions behind!",
               "Docs you should have a look at: http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html",
               "and https://docs.python.org/3/whatsnew/3.6.html"],
    "pep8": ["Here is the URL for PEP8: https://www.python.org/dev/peps/pep-0008/"],
    "science": ["Science Bitches!!  https://www.youtube.com/watch?v=9Cd36WJ79z4"],
    "pip": ["pip is a python package manager similar to apt-get. It installs modules and packages,",
            "that you would not have by default in the standard library.",
            "Official Documentation here: https://pip.pypa.io//, when in doubt, uninstall pip and re-install.",
            "Don't forget to use pip for your python version!"]
}


class Plugins:
    def __init__(self, config):
        self.config = config
        self.bot = Bot(config)

    def add_command(self, entry, desc):
        if isinstance(desc, list):
            commands[entry] = desc
        else:
            commands[entry] = [desc]

    def exec_command(self, entry, nick=None):
        info = commands[entry]
        if isinstance(info, list):
            for i in info:
                self.bot.send_message(i, nick if nick else self.config["channel"])
        else:
            globals()[info["func"]](nick)

    def bot_help(self, nick):
        info = ", ".join(c for c in commands)
        # Change this so that it works calling an async function
        self.bot.send_message(info, nick if nick else self.config["channel"])
