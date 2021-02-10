import os
import sys
from fileinput import filename

def read_settings_file():
    dict = {}
    try:
        with open('settings.py') as f:
            for element in f:
                index = element.index("=")
                id = element [0:index].strip()
                if id in dict:
                    list = []
                    
                else:
                    value = element[index+1:].strip()
                dict[id] = value
    except (IOError, FileNotFoundError):
        print("'settings.py' file is not accessible")
    return dict

def read_template_file(dict, file_name):
    if False == file_name.endswith('.template'):
        print("Invalid file extension for", file_name)
        return
    try:
        with open(file_name) as f:
            out_fn = file_name[0:file_name.index('.')] + ".html"
            out = open(out_fn, "w")
            for element in f:
                index = 0
                length = len(element)
                line = ""
                while index < length:
                    if '{' == element[index] and '}' in element[index:]:
                        end = element[index:].index("}") + index
                        id = element[index + 1 : end]
                        if id in dict:
                            line = line + dict[id].strip('"')
                            index = end + 1
                        else:
                            line = line + element[index]
                            index = index + 1
                    else:
                        line = line + element[index]
                        index = index + 1
                out.write(line)
            out.close()
    except (IOError, FileNotFoundError):
        print(file_name,"is not accessible")

if __name__ == '__main__':
    dict = read_settings_file()
    if 2 != len(sys.argv):
        print("Invalid number of argument")
    else:
        read_template_file(dict, sys.argv[1])