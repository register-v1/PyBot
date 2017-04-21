
#!usr/bin/env python3.6
# -*- coding: utf-8 -*-
<<<<<<< HEAD


=======
from PyBot.core import log 
from PyBot.core import commands as comd
>>>>>>> origin/master
import socket
import ssl

from core import commands
from core import log


# This is the main class. Everything passes through this!
class Bot:

    def __init__(self, server, port, chan, ssl_on=True):
        self.config = {
            "server": server,
            "chan": chan,
            "port": port,
            "name": "PyBot",    # Name
            "nick": "PyBot",    # Nick
            "host": "python_b0t@127.0.0.1"  # Put a name before the '@'
        }

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 0)
        self.sock.setblocking(True)
<<<<<<< HEAD

        if ssl_on:
            self.sock = ssl.wrap_socket(self.sock)

    # Connect to the server...
=======
        if ssl:
            self.sock = ssl.wrap_socket(self.sock)
        else:
            pass
    #connect to the server...
>>>>>>> origin/master
    def connect(self):
        try:
            log.log_file()
            print("Trying to connect to the server...")
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

    # Send data to the server (in a special format, not a private msg)
    def send_data(self, data):
        try:
            self.sock.send(data.encode('UTF-8'))
        except Exception as e:
            print("There was an error sending the data...\n{0}".format(e))
            log.report_error(e)

    # Send a privmsg to a channel
    def send_message(self, msg):
        try:
            msg = str(msg)
            self.sock.send(("PRIVMSG {} :{}\r\n".format(self.config["chan"], msg)).encode('UTF-8'))
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
            if isinstance(self.config["chan"], list):
                for x in self.config["chan"]:
                    join = "JOIN :{0}\r\n".format(x)
                    print(join)
                    self.send_data(join)
            else:
                join = "JOIN :{0}\r\n".format(self.config["chan"])
                print(join)
                self.send_data(join)

        except Exception as e:
            print("There was an exception..")
            log.report_error(e)

    def recv_data(self):
        try:
            data = self.sock.recv(3000)
            data = data.decode('UTF-8')
            print("Data received:\t", data)
            if data.find('PING') != -1:
                data = data.split()
                self.sock.send(("PONG {} \r\n".format(data[1])).encode('UTF-8'))
            else:
                data = str(data)
                return data
<<<<<<< HEAD
        except Exception as e:
            raise Exception("The following Exception occurred.\n{0}".format(e))

=======
        except(Exception) as e:
            raise Exception("The following Exception occured.\n{0}".format(e))
           
>>>>>>> origin/master
    def send_user(self):
        try:
            print("Sending the user....")
            usr = "USER {0} {1} {2} : I'm a bot!\r\n".format(
                self.config["name"],
                self.config["host"],
                self.config["nick"]
            )
            self.send_data(usr)
        except Exception as e:
            print("There was an error sending the user...")
            log.report_error(e)

    def send_nick(self):
        try:
            print("Sending the nick...")
            nick = "NICK {}\r\n".format(self.config["nick"])
            self.send_data(nick)
            print(nick)
        except Exception as e:
            print("There was an error sending the nick...\n{0}".format(e))
            log.report_error(e)
<<<<<<< HEAD

    def command(self, data_sent):
        try:
            answer = commands.find_command(data_sent, self.config["chan"], self.config["nick"])

            if not answer:
                pass
            else:
                payload = str(answer)
                self.send_message(payload)
        except Exception as e:
            print("There was an error sending the nick...")
            log.report_error(e)
=======
    
>>>>>>> origin/master
