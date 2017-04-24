# -*- coding: utf-8 -*-
import datetime
#PyBot


#THIS IS TO LOG ERRORS
def log_file():
    try:
        #this is ran when the bot launches.
        print("Opening file....")
        f = open("../logs.txt", "a")
        f.write("Rib is being launched....\nTimestamp: "+str(datetime.datetime.now())+"\n")
    except:
        print("There was an error opening the file.")
        print("Creating a new one....")
        f = open("../logs.txt", "a")
        f.write("Log file created....\n")
        f.write("Rib is being launched.....\nTimestamp: "+str(datetime.datetime.now())+"\n")
        f.close()
#open file to write errors
def log_write(msg):
    f = open("../logs.txt", "a")
    f.write(msg)
    f.close

def report_error(error):
    error = "There was an error:\t{} :{}\n".format(str(error.__class__), str(error))
    log_write(error)
