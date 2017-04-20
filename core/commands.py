# -*- coding: utf-8 -*-
import re
import PyBot.API.python as python
import PyBot.API.python_help as pyh
#import PyBot.plugin.bad_word as bw
#import PyBot.plugin.admin as check


# finds a command and calls the right function
def find_command(data, channel, bot_name):
    data = str(data)
    join = ("JOIN {0}".format(channel))
    # this is to find a who sends a msg. The name is used in some functions
    privmsg = re.findall("(:(.*)!)(.*)\s+PRIVMSG {0} :(.*)".format(channel), data)
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
        elif join in data:
            name = re.findall(r":([a-zA-Z0-9|\_|\-|\.]+)!", data)
            if str(privmsg) in data:
                msg = "Nice try {0} ;)".format(name[0])
                return msg
            # if the bot joins a room or if someone else joins a room
            elif bot_name in data:
                msg = "{0} has been updated b0ss.".format(str(bot_name))
                return msg
            else:
                # Greet the new commer
                msg = "Welcome {0}!".format(name[0])
                print(msg)
                return msg
        # wip, suppose to do the help() function
        elif cmd in "&pyhelp":
            return pyh.python_search(data)
        elif privmsg != []:
            # checks for badwords!
            status = bw.check_badword(privmsg, bot_name)
            if status != None:
                return status
            else:
                pass
        #elif 
