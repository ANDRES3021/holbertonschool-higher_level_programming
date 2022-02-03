#!/usr/bin/python3
"""append lines"""


def append_after(filename="", search_string="", new_string=""):
    """append"""
    with open(filename, "r") as myfile:
        lines = myfile.readlines()
    myfile.close()

    with open(filename, "w") as writefile:
        """append conditional"""
        for line in lines:
            if search_string in line:
                line = line + new_string
            writefile.write(line)
