# python ./app.py -t ./texts/Beginners-Luck.txt -s ./texts/Beginners-Luck_sub.txt -i true
# python ./app.py -t ./texts/Beginners-Luck.txt -s ./texts/Beginners-Luck_sub.txt
# python ./app.py -t ./texts/example.txt -s ./texts/example_sub.txt -i true
# python ./app.py -t ./texts/example.txt -s ./texts/example_sub.txt

import argparse
import shutil
import sys
import os

from src.libs.timing import *
from src.libs.kmp import *
from src.libs.bmx import *
from src.libs.rabin_karp import *
from src.libs.aho import *
from src.libs.lib_find import *
from src.libs.modDirectSearch import *


def createFolder(directory):
    '''
    This function create a directory.

    :param directory: path to the directory
    :return: None
    '''
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)

        shutil.rmtree(directory, ignore_errors=True)
        os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


def runapp(folder, text, substring) -> None:
    '''
    Function to run functions from substrings.py

    :param folder: path to folder containing images
    :param text: path to text file
    :param substring: path to substring file
    :return: None
    '''
    f = open(text, "r")
    txt = f.read()
    f.close()

    fs = open(substring, "r")
    sub = fs.read()
    sub = sub.split('\n')[0].split(' ')[0]
    fs.close()

    i1 = modDirectSearch(txt, sub)
    i2 = kmp(txt, sub)
    i3 = bmx(txt, sub)
    i4 = rabin_karp(txt, sub)
    i5 = aho_find_all(txt, sub)
    i6 = lib_find(txt, sub)

    if i5 == []:
        i5 = -1

    global timedict

    with open(folder + 'result.txt', 'w') as result:
        result.write(f"modDirectSearch: {i1}, {timedict['modDirectSearch']}\n\n"
                     f"kmp: {i2}, {timedict['kmp']}\n\n"
                     f"bmx: {i3}, {timedict['bmx']}\n\n"
                     f"rabin_karp: {i4}, {timedict['rabin_karp']}\n\n"
                     f"aho_find_all: {i5}, {timedict['aho_find_all']}\n\n"
                     f"lib_find: {i6}, {timedict['lib_find']}\n")

    return


if __name__ == '__main__':
    if len(sys.argv) >= 3:
        ap = argparse.ArgumentParser()
        ap.add_argument("-t", "--text", required=True, help="Path to text")
        ap.add_argument("-s", "--substring", required=True, help="Path to substring")

        args = vars(ap.parse_args())

        # Text
        text = args["text"]

        # Substring
        substring = args["substring"]

        # Create new directory
        folder = './result/'
        createFolder(folder)

        # Call to action
        runapp(folder, text, substring)

    else:
        print("Error. Please check your arguments.")
        sys.exit(1)