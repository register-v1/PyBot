# -*- coding: utf-8 -*-
import re
import API.python as python
import API.wisdom as wisdom
from core.bot_class import *
import time
import random
import asyncio

# import PyBot.plugin.bad_word as bw
# import PyBot.plugin.admin as check


# finds a command and calls the right function
def find_command(data, channels, bot_name):
    # this is to find a who sends a msg. The name is used in some functions
    privmsg = re.findall(r":(.*)!(.*)\s+PRIVMSG {0} :(.*)".format(channels[1]), data)    # find a command
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
            
                
            
            '''
        elif (cmd == '&exec'):
            banned_code = ['import']
            
            if data in banned_code:
                return "That code is banned"
            else:
                return exec(data)    
                     '''   
        elif (cmd == "&charge"):
            num = re.findall(r"&charge ([a-zZA-Z0-9|\-|\_]+)", data)
            if num:          
                return "PyBot charges {} for being a nigger. http://imgur.com/gallery/1M1WhGN".format(num[0])       
            else:
                return "PyBot charges {} for being a nigger. http://imgur.com/gallery/1M1WhGN".format(privmsg[0][0])                        

        elif (cmd == "&weed"):
            num = re.findall(r"&weed ([a-zZA-Z0-9|\-|\_]+)", data)
            if num:
                
                return "PyBot rolls a joint for {} and passes it.".format(num[0])       
            else:
                return "PyBot rolls a joint for {} and passes it.".format(privmsg[0][0]) 
                
        elif (cmd == "&popcorn"):
            num = re.findall(r"&popcorn ([a-zZA-Z0-9|\-|\_]+)", data)
            if num:
                
                return "PyBot gives {} a bag of pocorn and sits back to watch this shit go down.".format(num[0])       
            else:
                return "PyBot gives {} a bag of pocorn and sits back to watch this shit go down.".format(privmsg[0][0]) 
                                
        elif (cmd == "&beer"):
            num = re.findall(r"&beer ([a-zZA-Z0-9|\-|\_]+)", data)
            if num:
                
                return "PyBot pours up a mugg for {} and slides it down the bar.".format(num[0])       
            else:
                return "PyBot pours up a mugg for {} and slides it down the bar.".format(privmsg[0][0])                 
                  
                
        elif (cmd == "&leet"):
            user_to_tell = re.findall(r"&leet ([a-zZA-Z0-9|\-|\_]+)", data)
            if user_to_tell:
                
                return "HA HA HA HA! You think you're 1337 {}? BITCH PLZ xD".format(user_to_tell[0])       
            else:
                return "HA HA HA HA! You think you're 1337 {}? BITCH PLZ xD".format(privmsg[0][0])        
                              

        elif (cmd == '&pastejacking'):
            def func00(): return 'Pastejacking is an exploit that uses the JavaScript programming language. '
            def func01(): return "It is possible to sanitize data to protect yourself, Please see:  "
            def func10(): return "https://nakedsecurity.sophos.com/2016/05/26/why-you-cant-trust-things-you-cut-and-paste-from-web-pages/"
        
            return f'{func00()!s} {func01()!s} {func10()!s}'
            
        elif (cmd == "&wisdom"):
            return_value =  wisdom.wisdom()
            return return_value
            
        elif (cmd == "&troll"):
            return_value =  wisdom.troll()
            return return_value
            
        elif (cmd == "&whypy3"):
            def func00(): return "There are many improvements made in python3 you will not find in python2. "
            def func01(): return "Socket handling, threading, better standard lib, the list goes on. "
            def func10(): return "Please see http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html"
            def func11(): return "and https://docs.python.org/3/whatsnew/3.6.html"
            def func100(): return "Realize that if you learn 2.7.5, you will be almost 10 revisions behind!"
            
            
            return f'''{func00()!s} {func01()!s} {func10()!s} {func11()!s} {func100()!s}'''
            
        
        elif (cmd =='&bo'):
            def func00(): return "Buffer Overflows are explots to buffers in memory. An example can be found here : "
            def func01(): return "http://www.thegeekstuff.com/2013/06/buffer-overflow/?utm_source=feedly"
            
            return f'{func00()!s} {func01()!s}'
            
        elif (cmd == "&pep8"):
            return "Here is the URL for PEP8: https://www.python.org/dev/peps/pep-0008/"
            
        elif (cmd == "&creds"):
            return "Credits for GPL development of this bot goes to r0073d, Woz, v1 & others. Credit for Ghostbin go to revaa, v1 and others."
            
        elif (cmd == "&sciencepls"): 
            science_video = wisdom.science()
            return f"SCIENCE Bitches!!  {science_video!s}"
            
        elif (cmd == "&science"):
            science_song = re.findall(r"&science ([a-zZA-Z0-9|\-|\_]+)", data)
            if science_song:
                
                return "SCIENCE! {0}".format(wisdom.science_song(int(science_song[0])))        
            else:
                return "SCIENCE! {0}".format(wisdom.science_song(int(privmsg[0][0])))             
            
        elif (cmd == "&song"):
            number = re.findall(r"&song ([a-zZA-Z0-9|\-|\_]+)", data)
            if number:
                
                return "This is the song: {0}".format(wisdom.song(int(number[0])))        
            else:
                return "This is the song: {0}".format(wisdom.song(int(privmsg[0][0]))) 
            
        elif (cmd == "&help" or cmd == '&rules'):
            def func00(): return "Please see this url: https://bpaste.net/show/2d3e0924c403"
            def func01(): return "This url contains our rules and culture"
            
            return f'{func00()!s} {func01()!s}'
            
        elif (cmd == "&pyai"):
            def func00(): return "Here is the URL for Artificial Intelligent Packages:  https://wiki.python.org/moin/PythonForArtificialIntelligence"
            def func01(): return "https://www.youtube.com/watch?v=OGxgnH8y2NM&list=PLQVvvaa0QuDfKTOs3Keq_kaG2P55YRn5v"
            def func10(): return "This is not a complete list, but it helps you to get started.."
            
            return f'''{func00()!s}  {func01()!s} {func10()!s}'''
            
            
        elif (cmd == "&sql"):
            def func00(): return "SQL is a programming language for managing databases.  "
            def func01(): return "Please watch this for SQL Injection concepts : https://www.youtube.com/watch?v=ciNHn38EyRc "               
            
        elif (cmd == "&cookie" or cmd == "&cookies"):
            return "Please watch this for cookie concepts : https://www.youtube.com/watch?v=T1QEs3mdJoc"
            
        elif (cmd == '&bash'):
            def func00(): return "Bash, although used by GNU/Linux terminals, can be used in Python! Here is one way how: "
            def func01(): return 'http://stackoverflow.com/questions/13745648/running-bash-script-from-within-python  '   
            def func10(): return 'To learn more about bash, see http://www.learnshell.org/' 
            
            return f'{func00()!s} {func01()!s} {func10()!s}'
            
            
        elif (cmd == '&idor'):
            return "https://blog.detectify.com/2016/05/25/owasp-top-10-insecure-direct-object-reference-4/"
            
        elif (cmd == '&apple'):
            return  "There is a surge of the newest thing on the streets! It's called the iDiot!"
            
        elif (cmd == '&fact'):
            return "There is NO system but GNU and Linux is one of it's Kernels."   
            
                
        elif (cmd =='&cfunctions'):
            def func00(): return "C builtin functions are included in standard header files. "
            def func01(): return "Different header files will have different functions. Some are not ISO. "
            def func10(): return "https://www.techonthenet.com/c_language/standard_library_functions/"
            
            return f'{func00()!s} {func01()!s} {func10()!s}'        
                
        elif (cmd == "&pyfunctions"):
            return "Here is the URL to builtin Python functions:  https://docs.python.org/3/library/functions.html"
            
        elif (cmd =='&perlfunctions'):
            return "Here is the URL for Perl functions: http://perldoc.perl.org/index-functions.html"  
            
        elif (cmd == '&rubyfunctions'):
            def func00(): return "The main power of Ruby is it's builtin methods, which can be found with:"
            def func01(): return "object.methods.sort; and example would be 's'.methods.sort"
            def func10(): return "But you can find functions and classes here: https://ruby-doc.org/docs/ruby-doc-bundle/Manual/man-1.4/function.html"
            
            return f'{func00()!s} {func01()!s} {func10()!s}'      
            
        elif (cmd == "&functions"):
            def func00(): return 'use &pyfunctions for Python, &perlfunctions for Perl, &cfunctions for C and &rubyfunctions for Ruby.'
            def func01(): return 'More coming later.' 
            
            return f'{func00()!s} {func01()!s}'
            
        elif (cmd == "&python"):
            def func00(): return "Python is a Free Software Programming language!"
            def func01(): return "Python, although high level, has low level powers. From Buffer Overflows,ot HDL"
            def func10(): return "The offical docs are here: python.org"
            
            return f'{func00()!s} {func01()!s} {func10()!s}'    
            
        elif (cmd =='&password'):
            return "It isn't hard to make a secure password: https://xkcd.com/936/"   
            
        elif (cmd == "&linux"):
            return "Linux? Never heard of it. OH! You must mean GNU/Linux! Good shit."  
            
        elif (cmd == "&ctypes"):
            
            def func00(): return "Here is an example for use of ctypes:  http://www.ostricher.com/2015/03/hello-python-ctypes-world/ "        
            def func01(): return "Don't forget to check out ctypes in standard lib!"
            def func10(): return "&search 3.6 ctypes"
            
            return f'''{func00()!s}  {func01()!s}   {func10()!s}'''
            
        elif (cmd == '&backdoors' or cmd == '&backdoor'):
            def func00(): return "Backdoors are banned from all GNU Software."
            def func01(): return "To see the threat of proprietary backdoors, please see the following: "
            def func10(): return "https://www.gnu.org/proprietary/proprietary-back-doors.en.html"
            
            return f'{func00()!s} {func01()!s} {func10()!s}'    
            
        elif (cmd =='&c'):
            def func00(): return "Please understand that the Python, Ruby, and Perl programming languages were made in ISO C"
            def func01(): return "The C code that made Python3, is better than the C code that Python2.7. The same is true for other languages."
            def func10(): return "C Standards: http://port70.net/~nsz/c/ | Current ISO is C11. "  
            def func11(): return "C is a compiled low leveled language, and the GNU compiler for it is GCC."  
                
            return f'{func00()!s} {func01()!s} {func10()!s} {func11()!s}'
            
        elif (cmd == '&cms'):
            def func00(): return "CMS is a 'Content Managment System'. You can find info here:  "
            def func01(): return "https://www.incapsula.com/blog/cms-security-tips.html"    
            
            return f'{func00()!s}  {func01()!s}'
            
        elif (cmd == '&roulette'):
            def func00(): return "import random; print('DEAD!') if random.randrange(0,10) > 5 else print('Safe')"  
            def func01(): 
                
                if random.randrange(0,11) > 5:
                    return 'DEAD!'
                else:
                    return 'Safe'
                    
            return f"{func00()!s}  You're {func01()!s}"        
                 
    
                
        elif (cmd == "&quote"):
            number = re.findall(r"&quote ([a-zZA-Z0-9|\-|\_]+)", data)
            if number:
                
                return "{0}".format(wisdom.quote(int(number[0])))        
            else:
                return "{0}".format(wisdom.quote(int(privmsg[0][0])))                             


        elif (cmd == "&beer"):
            name = re.findall(r"&beer ([a-zZA-Z0-9|\-|\_]+)", data)
            if name:
                return "{} pours a mug of beer for {} and slides it down.".format(bot_name, name[0])
            else:
                return "{} pours a mug of beer for {} and slides it down.".format(bot_name, privmsg[0][0])

        elif (cmd == "&crypto"):
            def func000(): 
                return "info and tools about cryptography: https://pastebin.com/36DwYdgY"          
            return f'''{func000()!s}'''

        elif (cmd == "&pip"):
            def func00(): return "pip is a python package manager similar to apt-get. It installs modules and packages,"
            def func01(): return " that you would not have by default in the standard library."
            def func10(): return "Offical Documentation here:  https://pip.pypa.io//   , when in doubt, uninstall pip and re-install. "
            def func11(): return "Don't forget to use pip for your python version! For example, pip for python2.7 and pip3 for python3.4"
            
            return f'''{func00()!s} {func01()!s} {func10()!s} {func11()!s}'''
            
        elif (cmd == "&hack"):
            def func00(): return "Learning to 'hack' is like learning to invent. It doesn't work that way."
            def func01(): return "Hacking is a mindset, a form of discovery, not DOSing a random server."
            def func10(): return "You are not a hacker just because you can use nmap, hping3, etc."
            def func11(): return "If you are sincere about 'hacking', then learn2codepls"
            
            
            return f'''{func00()!s} {func01()!s} {func10()!s} {func11()!s}'''
            
        elif (cmd == '&bs4'):
            return "https://www.crummy.com/software/BeautifulSoup/bs4/doc/"    
            
        elif (cmd == "&pypi"):
            return "You can find the Python Package Index here:  https://pypi.python.org/pypi   "
            
        elif (cmd == "&urlpls"):
            return_value = wisdom.urlpls()
            return return_value
            
        elif (cmd in "&url"):
            num = re.findall(r"&url ([a-zZA-Z0-9|\-|\_]+)", data)
            if num:
                
                return "This is the URL: {0}".format(wisdom.url(int(num[0])))        
            else:
                return "This is the URL: {0}".format(wisdom.url(int(privmsg[0][0])))
            
        elif (cmd == "&setmode"):
            return exe( test.mode_set() )
            
        elif (cmd == "&identify"):
            return exe( test.identify() )
            

            
        elif (cmd == "&rekt"):
            name = re.findall(r"&rekt ([a-zZA-Z0-9|\-|\_]+)", data)
            if name:
                return "Damn, {} knows that {} just got &rekt()".format(bot_name, name[0])
            else:
                return "Damn, {} knows that {} just got &rekt()".format(bot_name, privmsg[0][0])
            
        elif (cmd == "&keylogger"):
            def func00(): return "Keyloggers log all the key strokes made, and are malicious malware "
            def func01(): return "Here is a basic keylogger in python:  https://www.youtube.com/watch?v=8BiOPBsXh0g"
            
            return f'{func00()!s}  {func01()!s}'
             
            
        elif (cmd == "&gnu"):
            def func00(): return "'open source' software and 'free' software are NOT the same thing!"
            def func01(): return "Free software is 'free' as in 'freedom', it gives you rights! Open source doesn't."
            def func10(): return "The U.S. Bill of Rights gives you 10 freedoms. The GPL gives you 4 "
            def func11(): return "To learn more, please watch this:  https://www.youtube.com/watch?v=Ag1AKIl_2GM "
            
            return f'''{func00()!s} {func01()!s} {func10()!s} {func11()!s} '''
            
        elif (cmd == "&ipython"):
            def func00(): return "Ipython is a python interpreter written in Python. "
            def func01(): return "It is free software (BSD License) and is extremely helpful in coding "
            def func10(): return "Ipython offers indentation, coloring of keywords, and showing of source code "
            def func11(): return "To learn more, see:  https://ipython.org/install.html "
            
            return f'''{func00()!s}  {func01()!s}  {func10()!s}  {func11()!s} '''
            
        elif (cmd == "&turing"): 
            def func00(): return "Python is a turing complete language just like C, Ruby, Java, or GNU Assembly." 
            def func01(): return "Turing complete languages can complete any turing instruction "
            def func10(): return "Please see : https://en.wikipedia.org/wiki/Turing_completeness "  
            def func11(): return "While no language is better than python, python isn't 'better' than other languages. "
            def func100(): return "There are pros/cons to any language you could/would use."
            
            return f'''{func00()!s} {func01()!s} {func10()!s} {func11()!s} {func100()!s}'''
            
        elif (cmd == "&gil"):
            def func00(): return "GIL is GLobal Interpreter Lock. It is when a program is bound to 1 core of a CPU, even when the CPU has multiple cores."
            def func01(): return "This is a PROBLEM that exists in a few interpretted languages and has been with us for years."
            def func10(): return "Python, Ruby, and other languages are affected by the GIL, while languages like Perl and Java are not. To learn more, see :"
            def func11(): return "https://www.quora.com/Why-does-the-JVM-not-have-a-GIL-while-the-Ruby-and-Python-interpreters-do "  
            def func100(): return "https://www.youtube.com/watch?v=l_HBRhcgeuQ      <- Explains more"
            
            return f'''{func00()!s} {func01()!s}  {func10()!s} {func11()!s} {func100()!s}'''
            
        elif (cmd == "&beginner"):
            def func00(): return "Starting off with codecademy is an option if you're a 100% beginner! Be sure to check our library in the topic!"
            def func01(): return "If you are past the level of codecademy, then you are probably a novice."
            def func10(): return "Check our topic. "
            def func11(): return "You may also want to see https://mediafire.com/file/ucduxouvzr48jq0/Complete_Python_Bootcamp.rar and "
            def func100(): return "http://www.pythonchallenge.com/  #programmers and #learninghub can help with basic topics."
            
            def big00(): return f'''{func00()!s} {func01()!s} {func10()!s} '''
            def big01(): return f'''{func11()!s} {func100()!s}'''
            
            return f'{big00()!s} {big01()!s}'
            
            
            
            
        elif (cmd == "&novice"):
            def func00(): return "Novice level coding is the 'long haul', because a lot of what you will be learning is how to use code"
            def func01(): return "that is already in existence, such as argparse, sys, and asyncoro."
            def func10(): return "Advice is to explore both the standard library, and Python Package Index."
            def func11(): return "If you haven't already started a project, then it would be wise to do so."
            
            return f'{func00()!s} {func01()!s} {func10()!s} {func11()!s}'
            
        elif (cmd == "&songpls"):
            result  = wisdom.songpls()
            return "Random Musix: {0}".format(result)        
            
        elif (cmd == "&ai"):
            return "https://www.youtube.com/watch?v=OGxgnH8y2NM&list=PLQVvvaa0QuDfKTOs3Keq_kaG2P55YRn5v"
            
        elif (cmd == "&pycrypto"):
            def func00(): return "Cryptographay is a huge field in it's own right. If you want the basics, then please see:"
            def func01(): return "https://cryptography.io/en/latest/   pyaes and pycrypto have also been found useful"
            
            return f'''{func00()!s}  {func01()!s} '''
        
        elif (cmd == "&concurrent"):
             return "https://docs.python.org/3.6/library/concurrent.futures.html#module-concurrent.futures " 
        
            
        elif (cmd == "&version"):
            return "This is beta version. Tell Woz I added some of his logic, and he is gay for not idling."    
             
            
        elif (cmd == "&obfuscated"):
            return "http://preshing.com/20131219/bitcoin-address-generator-in-obfuscated-python/"    
            
        elif (cmd == "&ivr"):
            return "https://www.twilio.com/blog/2014/07/build-an-ivr-system-with-twilio-and-django.html"     
            
        elif (cmd in "&randomtopic"):
            result = wisdom.randomtopic()    
            return "Here is the topic: {0}".format(result)
            
        elif (cmd in "&randomcourse"):
            result = wisdom.randomcourse()    
            return "Here is the course: {0}".format(result)  
            
        elif (cmd == "&noob"):
            result = wisdom.noob()
            return result     
            
        elif (cmd == "&noobquote"):
        
            result = wisdom.noob_quote(index)    
             
        elif (cmd == '&gnumarsch'):
             return "EIN GNU!! EIN PROGRAM!! EIN PROGRAMMER!! HEIL GNU!! DAS GNU MARSCH!! \o\o\o\o\o"
             
        elif (cmd == '&whygnu'):
            def func00(): return "#1 Don't say you can't make money off free software. The US Airforce paid for a GNU Ada compiler."
            def func01(): return "#2 Free Software helps protect our other freedoms, such as free speech and free press."
            def func10(): return "If you don't care about your free software rights, you don't need your other rights."
            
            return f"{func00()!s} {func01()!s} {func10()!s}"
     #### OpTraining commands below  ####        
        elif (cmd in "&tor"):
            return "To download tor: https://www.torproject.org/download/download.html.en, For more info about tor: https://pastebin.com/kyJD9B7U"

        elif (cmd in "&virtualbox"):
            return "To download virtualbox: https://www.virtualbox.org/ For more info about virtualbox: https://pastebin.com/EiYuT6E6"

        elif (cmd in "&pentesting"):
            return "list of pentesting tools: https://pastebin.com/Wwnb4bRP Extra info about pentesting: https://pastebin.com/di1YtYU6"

        elif (cmd in "&verification"):
            return "To verify your completed challenges please pm dsr with the following info: <ChallangeID> <challangetopic> <nickname> <answer>"

        elif (cmd in "&forum"):
            return "Channel forum is found here: https://pastebin.com/EiYuT6E6"

        elif (cmd in "&highscores"):
            return "Please visit the following url to see the highscore: https://pastebin.com/nVYVJdsr"

        elif(cmd in "&challengeme"):
            return "Please visit this page to know more about challenges: https://pastebin.com/vjK6kC55"

        elif (cmd in "&challenges"):
            return "You can now start the challneges - https://pastebin.com/vjk6kC55"

        elif (cmd in "&challengeshelp"):
            return "If you want to join a challenge or need help with one please ask help to: dsr or someone25572"

        elif (cmd in "&vpn"):
            def func00(): return "Info about Virtual Private Networks (aka vpn): https://pastebin.com/FpqC4bkX"
            def func01(): return "Consider Mullvad, which has an open source Linux client in python. mullvad.net"
            def func10(): return "READ THE PRIVACY POLICY AND TERMS OF SERVICE. DATA LOGS ARE NO JOKE"
            
            return f"{fucn00()!s} {func01()!s} {func10()!s}"

        elif (cmd in "&stenography"):
            return "stenography tools and information: https://pastebin.com/Rub0brF5"


        elif (cmd in "&coding"):
            def func00(): return "If you have any questions about coding you can go to one of the following channels:"
            def func01(): return "#opspeakcode , #swift , #python, #ruby, #javascript, #css, #php, #SQL and #perl "
            def func10(): return "You can also ask questions to: v1 and void(might be using a different nick)"

            return f"""{func00()!s} {func01()!s} {func10()!s}"""

        elif (cmd in "&helpme"):

            return "This is the help for #Optraining: https://bpaste.net/show/9abc8b2aa037"


        elif (cmd in "&botversion"):
            return "PyBot_version: dsr_edition_xdd"        
            



        else:
            return None


