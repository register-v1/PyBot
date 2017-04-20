# -*- coding: utf-8 -*-
from PyBot.core.bot_class import *

# Should be moved to main.py soon....
#channel can also be a list if you want to join more then one channel
test = bot("irc.armillaria.net/6697", "#python")
# connect
test.connect()
# recive data and log it
data = test.recv_data()
log.log_write(data)
# send nick and user name
test.send_nick()
test.send_user()
my_bool = True
# First loop to get the server's login message
while my_bool:
    data = test.recv_data()
    data = str(data)
    # generally the last message that is send after you login on a server
    if data.find(':is now your hidden') != -1:
        # join a channel
        test.join()
        # quit the other loop
        my_bool = False
        # start an other loop to get info and check if it contains a command
        while True:
            data = test.recv_data()
            data = str(data)

            test.command(data)
