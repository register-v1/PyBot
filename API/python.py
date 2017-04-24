# -*- coding: utf-8 -*-
import requests
import re


def search_python(data):
    try:
        #find python version and what to search
        my_args = re.findall(
            r'(&[a-zA-Z]+)\s+(\d|\d\.\d|\d\.\d\.\d)\s+((?:(?:(?:[a-zA-Z]|\-)*|\s+){1,7}))',
            data)
        version = my_args[0][1]
        search = my_args[0][2]
        #if version between 3.7 and 2.0 we good to go bb
        if float(my_args[0][1]) <= 3.7 and float(my_args[0][1]) >= 2.0:
            pass
        else:
            #return error if its not the right version
            error = "Please input valid arguments or put them in the right oder.(ex: &search [version] [key_word_to_search])"
            return error
    except Exception as e:
        print("There was an error. Version number is probably invalid: ", e)
        return "There was an error. Invalid version number."
    link = ("https://duckduckgo.com/html/?q=python{}+{}".format(version, search))
    #basic header
    headers = {'Accept-Encoding': 'identity'}
    #request the duckduckgo url
    response = requests.get(link, headers=headers)
    data = response.text
    #look for python documentation url
    python_links = re.findall((
        r'docs\.python\.org\/(\d|\d\.\d|\d\.\d\.\d)*((?:\/(?:\w|\.|\-|\#)*){1,2})'
    ), data)
    main_version = re.findall(r'(\d+)', version)
    try:
        #fixes the links for the python documentation
        if ("/whatsnew/{}.html".format(version)) in python_links[0][1]:
            return_value = "https://docs.python.org/{}{}".format(
                version, python_links[1][1])
            print("return value:\t", return_value)
            return return_value
        elif ("/tutorial/" in python_links[0][1]):
            if (version == '2.7' or version == '3.3' or version == '3.4' or
                    version == '3.5' or version == '3.6' or version == '3.7'):
                return_value = "https://docs.python.org/{}{}".format(
                    version, python_links[0][1])
            else:
                return_value = "https://docs.python.org/{}{}".format(
                    main_version[0], python_links[0][1])

            print("return value:\t", return_value)
            return return_value
        else:
            print("Python links:", python_links)
            return_value = "https://docs.python.org/{}{}".format(
                version, python_links[0][1])
            print("return value:\t", return_value)
            return return_value

    except:
        print("There was an error. No specefic link for research.")
        return_value = "https://docs.python.org/{}/".format(version)
        return return_value
