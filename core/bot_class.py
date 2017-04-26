
#!usr/bin/env python3.6
# -*- coding: utf-8 -*-

import asyncio
import socket
import ssl
import re

from core import commands
from core import log

loop = asyncio.get_event_loop()
def exe(coro): return loop.run_until_complete(coro)

# This is the main class. Everything passes through this!
class Bot:

    def __init__(self, server, port, chan, ssl_on=True):
        self.config = {
            "server": server,
            "chans": chan,
            "port": port,
            "name": "PyBot_beta",    # Name
            "nick": "PyBot_beta",    # Nick
            "host": "PyBot_beta@127.0.0.1" , # Put a name before the '@'
            "pass": "PythonIsBadAssAsFuckYouMotherFucker"
        }

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 0)
        self.sock.setblocking(True)

        if ssl_on:
            self.sock = ssl.wrap_socket(self.sock)

    # Connect to the server...
    async def connect(self):
        try:
            log.log_file()
            print("Trying to connect to the server...")
            print("server: ", self.config["server"], " port: ", self.config["port"])
            self.sock.connect((self.config["server"], self.config["port"]))
            print("We did it!")
        except Exception as e:
            print("There was an exception....")
            print("Please look into the log file...")
            print("Exception: ", e)
            log.report_error(e)

    # Kill the bot
    def kill(self):
        return self.sock.close()
    
    async def mode_set(self):  
        try:
            print("Setting user mode...")
            self.sock.send(("MODE {0} +B\r\n".format(self.config['nick'])).encode('UTF-8'))        
        except Exception as e:
            print("There was an error setting mode...")
            log.report_error(e)

    async def identify(self):

        try:  
            print("Identifying with nickserv...")
            password1 = "PythonIsBadAssAsFuckYouMotherFucker"
            self.sock.send(("PRIVMSG NICKSERV IDENTIFY {0}\r\n".format(password1).encode('UTF-8')))
        except Exception as e:
            print("There was an error identifying...")
            log.report_error(e)       
    #def register_nickserv(self):
        #self.sock.send("MSG NICKSERV REGISTER {0} myfakeemail@email.org\r\n".format(self.config['pass']).encode('UTF-8'))

    # Send data to the server (in a special format, not a private msg)
    async def send_data(self, data):
        try:
            self.sock.send(data.encode('UTF-8'))
        except Exception as e:
            print("There was an error sending the data...\n {0}".format(e))
            log.report_error(e)

    # Send a privmsg to a channel
    async def send_message(self, msg, chan):
        try:
            msg = str(msg)
            self.sock.send(("PRIVMSG {} :{}\r\n".format(chan, msg)).encode('UTF-8'))
        except Exception as e:
            print("There was an error sending the message...")
            log.report_error(e)

    """
        if you want to join more then one channel, please make a list when
        creating the bot containing the channels you would like the bot to join.
        don't forget to put them in strings with a '#' at the start.
    """

    def join(self):
        try:
            if isinstance(self.config["chans"], list):
                for x in self.config["chans"]:
                    join = "JOIN :{0}\r\n".format(x)
                    exe(self.send_data(join))
            else:
                join = "JOIN :{0}\r\n".format(self.config["chans"])
                print(join)
                exe(self.send_data(join))

        except Exception as e:
            print("There was an exception..")
            log.report_error(e)
            
    async def join_python(self):
        try:
            exe(self.sock.send("JOIN :#PYTHON\r\n"))
        except(Exception) as e:
            print("This error occured\n{0}".fromat(e))
            
    async def recv_data(self):
        try:
            data = self.sock.recv(4096)
            data = data.decode('UTF-8')
            print("Data received:\t", data)
            if data.find('PING') != -1:
                data = data.split()
                #make sure its like this
                self.sock.send(("PONG {}\r\n".format(data[1])).encode('UTF-8'))
            elif data == None:
                self.kill()
                log.log_write("Connection closed. Recived No data -> stopping to be sure we don't DoS server")
            else:
                data = str(data)
                return data
        except Exception as e:
            log.report_error(e)

    async def send_user(self):
        try:
            print("Sending the user....")
            usr = "USER {0} {1} {2} : I'm a bot!\r\n".format(
                self.config["name"],
                self.config["host"],
                self.config["nick"]
            )
            exe(self.send_data(usr))
        except Exception as e:
            print("There was an error sending the user...")
            log.report_error(e)

    async def send_nick(self):
        try:
            print("Sending the nick...")
            nick = "NICK {}\r\n".format(self.config["nick"])
            exe( self.send_data(nick) )
            print(nick)
        except Exception as e:
            print("There was an error sending the nick...")
            log.report_error(e)

    async def command(self, data_sent):
        try:
            #Find channel when someone joins
            channel_data_was_sent = re.findall(r"JOIN (#[a-zA-Z0-9|\-|\_]+)", data_sent)
            if channel_data_was_sent == []:
                #find channel when someone sends a message
                channel_data_was_sent = re.findall(r"PRIVMSG (#[a-zA-Z0-9|\-|\_]+) :", data_sent)

            answer = commands.find_command(data_sent, channel_data_was_sent[0], self.config["nick"])

            if not answer or "PING :" in data_sent:
                pass
            else:
                payload = str(answer)
                exe( self.send_message(payload, channel_data_was_sent[0]) )
        except Exception as e:
            print("There was an error sending the data")
            log.report_error(e)
