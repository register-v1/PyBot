# -*- coding: utf-8 -*-
import re
import subprocess
import os

#This is a prototype/test Dont mind this code 
def make_template(cmd):
    template = """
import subprocess

cmd_line = "help(%s)"
_file = open("gen_output.py", "a")
_file.write(str(cmd_line))
_file.close()
cmd_line = "python gen_output.py"
p = subprocess.Popen(cmd_line, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
out = p.communicate()[0]
_file = open("output.txt", "a")
out = str(out)
_file.write(out)
_file.close()
    """ % str(cmd)
    return template

def python_search(data):
    need_help = re.findall(r"&pyhelp\s+([a-zA-Z|\'|\"]+)", data)
    msg = make_template(need_help[0])
    _file = open("command.py", "a")
    _file.write(msg)
    _file.close()
    cmd_line = "python command.py"
    p = subprocess.Popen(cmd_line, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return "!file output.txt"
