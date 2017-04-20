#!usr/bin/env python3.6
# -*- coding: utf-8 -*-
from PyBot.core import log as log
from PyBot.core import commands as comd
import socket
import ssl
import re


#This is the main class. Everything passes through this!
class bot:
    def __init__(self, server, chan, ssl=True):

        self.server = server
        self.chan = chan
        self.port = 6697
        #name
        self.name = "PyBot"
        #nick
        self.nick = "PyBot"
        #host : put name before the '@'
        self.host = "python_b0t@127.0.0.1"
        #Dont touch this
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 0)
        self.sock.setblocking(True)
        if ssl:
            return self.sock = ssl.wrap_socket(self.sock)
        else:
            pass
    #connect to the server...
    def connect(self):
        try:
            log.log_file()
            print("Trying to connect to the server...")
            self.sock.connect((self.server, self.port))
            print("We did it!")
        except Exception as e:
            print("There was an exception....")
            print("Please look into the log file...")
            print("Exception: ", e)
            log.report_error(e)
    # Kill the bot
    def kill_self(self):
        return self.sock.close()
        
    #send data to the server (in a special format -> not privmsg)
    def send_data(self, data):
        try:
            self.sock.send((data).encode('UTF-8'))
        except Exception as e:
            print("There was an error sending the data...")
            log.report_error(e)
    #send a privmsg to a room
    def send_message(self, msg):
        try:
            msg = str(msg)
            self.sock.send(("PRIVMSG {} :{}\r\n".format(self.chan, msg)).encode('UTF-8'))
        except Exception as e:
            print("There was an error sending the message...")
            log.report_error(e)
    #join a specefic channel. By default will use the one created in the class. You can join an additional one
    #bycalling the function with an argument
    def join(self):
        try:
            if isinstance(self.chan, list) :
                for x in self.chan:
                    join = "JOIN :{0}\r\n".format(x)
                    print(join)
                    self.send_data(join)
            else:
                join = "JOIN :{0}\r\n".format(self.chan)
                print(join)
                self.send_data(join)

        except Exception as e:
            print("There was an exception..")
            log.report_error(e)

    def recv_data(self):
        try:
            data = self.sock.recv(3000)
            data = data.decode('UTF-8')
            print("Data recived:\t", data)
            if data.find('PING') != -1:
                data = data.split()
                self.sock.send(("PONG {} \r\n".format(data[1])).encode('UTF-8'))
            else:
                data = str(data)
                return data
       except(Exception) as e:
           raise Exception("The following Exception occured.\n{0}".format(e))
           
    def send_user(self):
        try:
            print("Sending the user....")
            usr = "USER {0} {1} {2} : I'm a bot!\r\n".format(self.name, self.host, self.nick)
            self.send_data(usr)
        except Exception as e:
            print("There was an error sending the user...")
            log.report_error(e)

    def send_nick(self):
        try:
            print("Sending the nick...")
            nick = "NICK {}\r\n".format(self.nick)
            self.send_data(nick)
            print(nick)
        except Exception as e:
            print("There was an error sending the nick...")
            log.report_error(e)
'''
    def command(self, data_sent):
        answer = comd.find_command(data_sent, self.chan, self.nick)
        if answer is None:
            pass
        elif "op" == answer[0]:
            self.send_data("MODE {} +o {}\r\n".format(self.chan, answer[1]))
        elif "unop" == answer[0]:
            self.send_data("MODE {} -o {}\r\n".format(self.chan, answer[1]))
        elif "ban" in answer[0]:
            self.send_data("KICK {} {} {}\r\n".format(self.chan, answer[1], "You're fucking gay."))
            self.send_data("MODE {} +b {}!*@*\r\n".format(self.chan, answer[1]))
        elif "!file" in answer:
            file_name = re.findall(r"!file\s+([a-zA-Z0-9|x]*)", answer)
            _file = open(file_name[0] + ".txt", "r")
            for x in _file:
                self.send_message(x)
        else:
            payload = str(answer)
            self.send_message(payload)
'''
