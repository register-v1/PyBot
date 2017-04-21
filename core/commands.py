# -*- coding: utf-8 -*-
import re
import API.python as python
#import PyBot.plugin.bad_word as bw
#import PyBot.plugin.admin as check


# finds a command and calls the right function
def find_command(data, channel, bot_name):
    data = str(data)
    # this is to find a who sends a msg. The name is used in some functions
    privmsg = re.findall(":(.*)!(.*)\s+PRIVMSG {0} :(.*)".format(channel), data)
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
        elif "JOIN" in data and [] == privmsg:
                name = re.findall(r":([a-zA-Z0-9|\-|\.|\_]+)!", data)
                for x in channel:
                    if "JOIN {}".format(x) in data:
                        if bot_name in data:
                            #Bot says hi when he joins a room
                            msg = "Greeting! My name is {0}. r0073d is the best btw ;)".format(str(bot_name))
                            return msg
                        else:
                            # Greet the new commers
                            msg = "Welcome {0}!".format(name[0])
                            print(msg)
                            return msg



