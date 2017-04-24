# -*- coding: utf-8 -*-
import optparse
import asyncio
import time
from core import log
from core.bot_class import Bot

loop = asyncio.get_event_loop()
def exe(coro): return loop.run_until_complete(coro)

config = {"server": "irc.anonops.com", "port": 6697, "chans": ["#bots"]}

#Main loop
def authenticate():
    global test
    test = Bot(config["server"], config["port"], config["chans"])
    exe( test.connect() )
    data = str( exe( test.recv_data() ))
    log.log_write(data)
    exe( test.send_nick() )
    exe( test.send_user() )
    #test.register_nickserv()
    data = str( exe( test.recv_data() ))
    exe( test.identify() )
    exe( test.mode_set() )
    receive_data(test) 

    #exe( test.send_message("Hello!", config["chans"]) )


#test
def receive_data(bot, check=True):
    while check:
        data = str(exe(bot.recv_data()))
        """
        Armillaria: (:is now your hidden)
        Anonops: (:Global!services@anonops)
        """
        if config['server'] == 'irc.anonops.com':
        
            if data.find(':Global!services@anonops') != -1:
                exe(bot.join())
                check = False
                receive_command(bot)
    
                #exe( bot.register() )
                exe( bot.recv_data() )
                exe(bot.identify() )
                exe(bot.recv_data() )
                exe(bot.mode_set() )
                exe(bot.recv_data() )
                exe(bot.join() )
                check = False
                receive_command(bot) 
                              
        elif config['server'] == 'irc.armillaria.net':
        
            if data.find(':is now your hidden') != -1:
                exe(bot.join())
                check = False
                receive_command(bot) 


def receive_command(bot):
    while True:
        data = str( exe(bot.recv_data()) )
        exe(bot.command(data))


def check_input():
    parser = optparse.OptionParser("%prog -n <bot_file>")
    parser.add_option("-s", dest="server", help="irc server")
    parser.add_option("-p", dest="port", help="irc port [6697]")
    parser.add_option("-c", dest="channels", help="channels the bot should connect to")
    (options, args) = parser.parse_args()

    if not (options.server or config["server"]):
        parser.print_help()
        exit(0)

    config["server"] = options.server if options.server else config["server"]
    config["port"] = int(options.port) if options.port else 6697
    config["chans"] = options.channels.split(',') if options.channels else config["chans"]


def main():
    check_input()
    authenticate()
    authenticate() #i tried again to see if it would work the 2nd time


if __name__ == "__main__":
    main()
