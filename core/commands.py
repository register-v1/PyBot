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
                return "{} rolls a joint for {} and passes it.".format(bot_name, name[0])
            else:
                return "{} rolls a joint for {} and passes it.".format(bot_name, privmsg[0][0])
                

                
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
            return "Credits for GPL development of this bot goes to r0073d, Woz, v1 & others. Credit for Ghostbin go to revaa, v1 and others."
            
        elif (cmd in "&science"): 
            return "Science Bitches!!  https://www.youtube.com/watch?v=9Cd36WJ79z4"
            
        elif (cmd in "&help"):
            return "Please see this url: https://bpaste.net/show/2a53b4f4511e"
            
        elif (cmd in "&pyai"):
            def func00(): return "Here is the URL for Artificial Intelligent Packages:  https://wiki.python.org/moin/PythonForArtificialIntelligence"
            def func01(): return "https://www.youtube.com/watch?v=OGxgnH8y2NM&list=PLQVvvaa0QuDfKTOs3Keq_kaG2P55YRn5v"
            
            return str(func00()) + ' ' + str(func01())
            
        elif (cmd in "&sql"):
            return "Please watch this for SQL : https://www.youtube.com/watch?v=ciNHn38EyRc"    
            
        elif (cmd in "&cookie"):
            return "Please watch this for cookies : https://www.youtube.com/watch?v=T1QEs3mdJoc"
            
        elif (cmd in '&bash'):
            return 'http://stackoverflow.com/questions/13745648/running-bash-script-from-within-python'    
            
        elif (cmd in "&url"):
            num = re.findall(r"&url ([a-zZA-Z0-9|\-|\_]+)", data)
            if num:
                
                return "This is the URL: {0}".format(wisdom.url(int(num[0])))        
            else:
                return "This is the URL: {0}".format(wisdom.url(int(privmsg[0][0])))
                
                
        elif (cmd in "&song"):
            number = re.findall(r"&song ([a-zZA-Z0-9|\-|\_]+)", data)
            if number:
                
                return "This is the song: {0}".format(wisdom.song(int(number[0])))        
            else:
                return "This is the song: {0}".format(wisdom.song(int(privmsg[0][0])))     
                
        elif (cmd in "&quote"):
            number = re.findall(r"&quote ([a-zZA-Z0-9|\-|\_]+)", data)
            if number:
                
                return "{0}".format(wisdom.quote(int(number[0])))        
            else:
                return "{0}".format(wisdom.quote(int(privmsg[0][0])))                             


        elif (cmd in "&beer"):
            name = re.findall(r"&beer ([a-zZA-Z0-9|\-|\_]+)", data)
            if name:
                return "{} pours a mug of beer for {} and slides it down.".format(bot_name, name[0])
            else:
                return "{} pours a mug of beer for {} and slides it down.".format(bot_name, privmsg[0][0])
          
            
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
            name = re.findall(r"&rekt ([a-zZA-Z0-9|\-|\_]+)", data)
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
            def func01(): return "This problem applies to programs that run on a CPU with multiple cores, and has been an issue for years."
            def func10(): return "Python, Ruby, and other languages are affected by the GIL. To learn more, see :  "
            def func11(): return "https://www.quora.com/Why-does-the-JVM-not-have-a-GIL-while-the-Ruby-and-Python-interpreters-do "  
            def func100(): return "https://www.youtube.com/watch?v=l_HBRhcgeuQ      <- Explains more"
            
            return func00(), func01(), func10(), func11(), func100()
            
        elif (cmd in "&beginner"):
            def func00(): return "Starting off with codecademy is a good start if you're a 100% beginner! Be sure to check our library in the topic!"
            def func01(): return "If you are past the level of codecademy, it is recommended to start a github and work on a project"
            
            return func00(), func01()
            
        elif (cmd in "&songpls"):
            result  = wisdom.songpls()
            return "Random Musix: {0}".format(result)        
            
        elif (cmd in "&ai"):
            return "https://www.youtube.com/watch?v=OGxgnH8y2NM&list=PLQVvvaa0QuDfKTOs3Keq_kaG2P55YRn5v"
            
        elif (cmd in "&crypto"):
            def func00(): return "Cryptographay is a huge field in it's own right. If you want the basics, then please see:"
            def func01(): return "https://cryptography.io/en/latest/   pyaes and pycrypto have also been found useful"
            
            return func00(), func01()
            
        elif (cmd in "&version"):
            return "This is beta version. Tell Woz I added some of his logic."    
            
        elif (cmd in '&charge'):
            return "http://imgur.com/gallery/1M1WhGN"   
            
        elif (cmd in "&obfuscated"):
            return "http://preshing.com/20131219/bitcoin-address-generator-in-obfuscated-python/"    
            
        elif (cmd in "&ivr"):
            return "https://www.twilio.com/blog/2014/07/build-an-ivr-system-with-twilio-and-django.html"     
            
        elif (cmd in "&randomtopic"):
            result = wisdom.randomtopic()    
            return "Here is the topic: {0}".format(result)
            
        elif (cmd in "&randomcourse"):
            result = wisdom.randomcourse()    
            return "Here is the course: {0}".format(result)            
            
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

