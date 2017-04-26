# -*- coding: utf-8 -*-
import re
import API.python as python
import API.wisdom as wisdom
from core.bot_class import *
import time

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
                
        elif (cmd in "&beer"):
            name = re.findall(r"&beer ([a-zZA-Z0-9|\-|\_]+)", data)
            if name:
                return "{} pours a mug of beer for {} and slides it down.".format(bot_name, name[0])
            else:
                return "{} pours a mug of beer for {} and slides it down.".format(bot_name, privmsg[0][0])
                
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
            return "Credits for GPL development of this bot goes to r0073d, Woz & others. Credit for Ghostbin go to revaa and others."
            
        elif (cmd in "&science"): 
            return "Science Bitches!!  https://www.youtube.com/watch?v=9Cd36WJ79z4"
            
        elif (cmd in "&help"):
            def func0(): return "Commands for non-op users include:"
            def func1(): return "&pep8 - Gives you pep8 documentation : &pip - Pip documentation"
            def func111(): return "&pypi -  Gives you quick access to Python package index"
            def func10(): return "&sockets - Gives you documentation for sockets. Needed for networking"
            def func100(): return "&keylogger, - Gives you a url to a simple keylogger"
            def func101(): return "&whypy3 - Tells you why you should move to python3 and not python2"
            def func102(): return "&wisdom - Givs you a random quote for wisdom"
            def func103(): return "&troll - Randomly trolls. If you over use this, you will be kicked."
            def func104(): return "&search - Searches python documentation : syntax &search [version] [item]"
            def func105(): return "&beer and &weed give you some of the good stuff."
            def func106(): return "&turing - will tell you what a turing complete language is. &gil explains GIL"
            def func2(): return "&urlpls - This will give you a random tutorial url, &hack, &gnu, &ipython and &science"
            
            def stack1(): return func0(), func1(), func10(), func100(), time.sleep(2), func101(), func102()
            def stack2(): return func103(), func104(), func105(), func111(), func106(), func2()
            
            return stack1(), stack2()
            
        elif (cmd in "&pip"):
            def func00(): return "pip is a python package manager similar to apt-get. It installs modules and packages,"
            def func01(): return " that you would not have by default in the standard library."
            def func0(): return "Offical Documentation here:  https://pip.pypa.io//   , when in doubt, uninstall pip and re-install. "
            def func1(): return "Don't forget to use pip for your python version! For example, pip for python2.7 and pip3 for python3.4"
            
            return func00(), func01(), func0(), func1()
            
        elif (cmd in "&hack"):
            def func0(): return "Learning to 'hack' is like learning to invent. It doesn't work that way."
            def func1(): return "Hacking is a mindset, a form of discovery, not DOSing a random server."
            def func2(): return "You are not a hacker just because you can use nmap, hping3, etc."
            def func3(): return "If you are sincere about 'hacking', then learn2codepls"
            
            
            return func0(), func1(), func2(), func3()
            
        elif (cmd in "&pypi"):
            return "You can find the Python Package Index here:  https://pypi.python.org/pypi   "
            
        elif (cmd in "&urlpls"):
            return_value = wisdom.urlpls()
            return return_value
            
        elif (cmd in "&setmode"):
            return exe( test.mode_set() )
            
        elif (cmd in "&identify"):
            return exe( test.identify() )
            
        elif (cmd in "&joinp"):
            return exe( test.join_python())
            
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
            
        elif (cmd in "&gnu"):
            def func00(): return "'open source' software and 'free' software are NOT the same thing!"
            def func01(): return "Free software is 'free' as in 'freedom', it gives you rights! Open source doesn't."
            def func0(): return "The U.S. Bill of Rights gives you 10 freedoms. The GPL gives you 4 "
            def func1(): return "To learn more, please watch this:  https://www.youtube.com/watch?v=Ag1AKIl_2GM "
            
            return func00(), func01(), func0(), func1()
            
        elif (cmd in "&ipython"):
            def func00(): return "Ipython is a python interpreter written in Python. "
            def func01(): return "It is free software (BSD License) and is extremely helpful in coding "
            def func10(): return "Ipython offers indentation, coloring of keywords, and showing of source code "
            def func11(): return "To learn more, see:  https://ipython.org/install.html     "
            
            return func00(), func01(), func10(), func11()
            
        elif (cmd in "&turing"): 
            def func0(): return "Python is a turing complete language just like C, Ruby, Java, or GNU Assembly. " 
            def func00(): return "Turing complete languages can complete any turing instruction"
            def func1(): return "Please see : https://en.wikipedia.org/wiki/Turing_completeness "  
            def func2(): return "While no language is better than python, python isn't 'better' than other languages. "
            def func3(): return "There are pros/cons to any language you could/would use"
            
            return func0(), func1(), func2(), func3() 
            
        elif (cmd in "&gil"):
            def func00(): return "GIL is GLobal Interpreter Lock. It is when a program is bound to 1 core of a CPU. "
            def func01(): return "This problem applies to computers with a CPU having 4 cores. The program is still trapped."
            def func10(): return "Python, Ruby, and other languages are affected by the GIL. To learn more, see :  "
            def func11(): return "https://www.quora.com/Why-does-the-JVM-not-have-a-GIL-while-the-Ruby-and-Python-interpreters-do "  
            
            return func00(), func01(), func10(), func11()
            
            
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

