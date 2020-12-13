import sys
from typing import AnyStr


def getBranchName(name: AnyStr):
    if name.__contains__("refs/heads/"):
        name = name.replace("refs/heads/", "")
    remove_illegal_file_chars_in_name = ['~', '`', '\'', '"', '!', '%', ';', '']
    illegal_file_char_in_names = [':', '&', '*', '(', ')', '<', '>', '/', '[', ']', '|', '{', '}', '\\', '\t', '\n']
    split_name = name.split('/')
    if len(split_name) <= 1:
        return name
    name = split_name[len(split_name) - 2] + ':' + split_name[len(split_name) - 1]
    for illegalChar in remove_illegal_file_chars_in_name:
        name = name.replace(illegalChar, '')
    for illegalChar in illegal_file_char_in_names:
        name = name.replace(illegalChar, '.')
    return name


if __name__ == "__main__":
    print(getBranchName(sys.argv[1]))
