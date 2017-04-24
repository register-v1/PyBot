# -*- coding: utf-8 -*-
import re
import API.python as python
import API.wisdom as wisdom
from core.bot_class import *

#import PyBot.plugin.bad_word as bw
#import PyBot.plugin.admin as check

global test

# finds a command and calls the right function
def find_command(data, channels, bot_name):
    data = str(data)
    # this is to find a who sends a msg. The name is used in some functions
    privmsg = re.findall(":(.*)!(.*)\s+PRIVMSG {0} :(.*)".format(channels), data)
    # find a command
    cmd = re.findall(r':(&[a-z]+)', data)
    # if a command was found
    if (data != []):
        if cmd != []:
            cmd = str(cmd[0])
            cmd = cmd.lower()
            print("Command found: ", cmd)
        else:
            cmd = "empty"
        # if the command is search, call the search function
        if (cmd in "&search"):
            return python.search_python(data)
        elif (cmd in "&weed"):
            name = re.findall(r"&weed ([a-zZA-Z0-9|\-|\_]+)", data)
            if name:
                return "{} rolls a blunt for {} and passes it.".format(bot_name, name[0])
            else:
                return "{} rolls a blunt for {} and passes it.".format(bot_name, privmsg[0][0])
                
        elif (cmd in "&wisdom"):
            return_value =  wisdom.wisdom()
            return return_value
            
        elif (cmd in "&troll"):
            return_value =  wisdom.troll()
            return return_value
            
        elif (cmd in "&whypy3"):
            def func0(): return "There are many improvements made in python3 you will not find in python2. "
            def func1(): return "Socket handling, threading, better standard lib, the list goes on. "
            def func2(): return "Please see http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html"
            def func3(): return "and https://docs.python.org/3/whatsnew/3.6.html"
            def func4(): return "Realize that if you learn 2.7.5, you will be almost 10 revisions behind!"
            
            
            return func0(), func1(), func2(), func3(), func4()
            
            
        elif (cmd in "&pep8"):
            return "Here is the URL for PEP8: https://www.python.org/dev/peps/pep-0008/"
            
        elif (cmd in "&creds"):
            return "Credits for GPL development of this bot goes to r0073d, Woz & v1"
            
        elif (cmd in "&science"): 
            return "Science Bitches!!  https://www.youtube.com/watch?v=9Cd36WJ79z4"
            
        elif (cmd in "&help"):
            return "Commands for users include &pep8, &pip, &sockets, &keylogger, &whypy3, &wisdom, &troll, &search and &creds"
            
        elif (cmd in "&pip"):
            def func00(): return "pip is a python package manager similar to apt-get. It installs modules and packages,"
            def func01(): return " that you would not have by default in the standard library."
            def func0(): return "Offical Documentation here: https://pip.pypa.io//, when in doubt, uninstall pip and re-install. "
            def fun1(): return "Don't forget to use pip for your python version! For example, pip for python2.7 and pip3 for python3.4"
            
            return func0()
        elif (cmd in "&hack"):
            def func0(): return "Learning to 'hack' is like learning to invent. It doesn't work that way."
            def func1(): return "Hacking is a mindset, a form of discovery, not DOSing a random server."
            def func2(): return "You are not a hacker just because you can use nmap, hping3, etc."
            def func3(): return "If you are sincere about 'hacking', then learn2codepls"
            
            
            return func0(), func1(), func2(), func3()
            
        elif (cmd in "&pypi"):
            return "You can find the Python Package Index here:  https://pypi.python.org/pypi"
            
        elif (cmd in "&urlpls"):
            return_value = wisdom.urlpls()
            return return_value
            
        elif (cmd in "&setmode"):
            return exe( test.mode_set() )
            
        elif (cmd in "&identify"):
            return exe( test.identify() )
            
        elif (cmd in "&rekt"):
            name = re.findall(r"&weed ([a-zZA-Z0-9|\-|\_]+)", data)
            if name:
                return "Damn, {} knows that {} just got &rekt()".format(bot_name, name[0])
            else:
                return "Damn, {} knows that {} just got &rekt()".format(bot_name, privmsg[0][0])
            
        elif (cmd in "&keylogger"):
            return "Here is a basic keylogger:  https://www.youtube.com/watch?v=8BiOPBsXh0g"
            
        elif (cmd in "&socket"):
            return "Here is the doc for sockets: https://docs.python.org/3/library/socket.html"

        elif (cmd in "&sockets"):
            return "Here is the doc for sockets: https://docs.python.org/3/library/socket.html"   
            
        elif (cmd in "&freedom"):
            return "It is important that you watch this:  https://www.youtube.com/watch?v=Ag1AKIl_2GM"
            
        elif "JOIN" in data and [] == privmsg:
                name = re.findall(r":([a-zA-Z0-9|\-|\.|\_]+)!", data)
                for x in channels:
                    if "JOIN {}".format(x) in data:
                        if bot_name in data:
                            #Bot says hi when he joins a room
                            msg = "Greetings! My name is {0}. There is no system but GNU and Linux is one of it's Kernels".format(str(bot_name))
                            return msg
                        else:
                            # Greet the new commers
                            msg = "Welcome {0}!".format(name[0])
                            print(msg)
                            return msg

        else:
            return None

