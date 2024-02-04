#!/usr/bin/env python3

# February 1 2024 - 1:06 am
# This script was made by OtherAnon, bc he was bored

import sys
import collections

# This is the help message

help_message = "\nUsage ./freqtext.py <path_to_file> \n" \
        "This script does a frequency analysis with encrypted texts\n" \
        "doing some analysis to the text to give you details like\n" \
        "the most repeated character, pair and trio in a file. The\n" \
        "options are these:\n\n " \
        "  -l      This option gives you details about the letters\n" \
        "   -p      This option gives you details about pairs\n" \
        "   -t      This option gives you details about trios\n" \
        "   -a      This option gives you all the details of the above options\n" \
        "   -x      Print the content of the file\n" \
        "   -h      This help message\n\n" \
        "Example usage:\n" \
        "./freqtext.py encrypted_file -a -x"

args = sys.argv

if len(args) == 1:
    print("Usage ./freqtext <path_to_file>")
    exit()
elif len(args) == 2:
    print(help_message)
    exit()
else:
    file_to_read = args[1]

opening = open(str(file_to_read),"r")
file = opening.read()

print("\n"+"\033[1;35m"+"<!!!>"+"\033[0;m"+" Analysis to file", opening.name)

del args[0:2]

# Creating the abc, later this abc will be used to search the quantity of repeated letters, and this abc works with every type of abc

def create_abc():
    global total_letters
    global abc
    abc = []
    for letter in file:
        if letter not in abc and letter != "\n" and letter != " ":
            abc.append(letter)
        else: continue
    total_letters = len(abc)

# Calculing the frequency of every letter in the encrypted text

def quantity_letters():
    global listing
    listing = {}
    while len(abc) != 0:
        quanchar = 0
        for letter in file:
            if letter == abc[0]:
                quanchar += 1
        listing[abc[0]] = quanchar
        del abc[0]

# Creating the order of the output from highest to lowest

def order_letters():
    values = sorted(listing.values())
    items = listing.items()
    global to_major
    to_major = dict(sorted(items, key=lambda item:item[1], 
    reverse=True))

# For a better output

def pretty_letters():
    items = to_major.items()
    for item in items:
        print("\n-- [", item[0], "] appears", item[1], "times")
    print("\033[1;32m"+"\n[ In total this text have", total_letters,"of different characters ] --------------------------------------------"+"\033[0;m")

# Searching pairs in the file

def get_pairs():
    global total_pairs
    global all_pairs
    all_pairs = []
    pair = []
    count = 0
    pair_count = 0
    for letter in file:
        if count == 0:
            count += 1
            continue
        elif letter == '\n' or letter == ' ': continue
        elif len(pair) == 0 or len(pair) == 1:
            pair.append(letter)
        else:
            all_pairs.append(pair[::])
            del pair[::]
            pair.append(letter)
    for letter in file:
        if letter == '\n' or letter == ' ': continue
        elif len(pair) == 0 or len(pair) == 1:
            pair.append(letter)
        else:
            all_pairs.append(pair[::])
            del pair[::]
            pair.append(letter)
    total_pairs = len(all_pairs)

# At this point I got all the pairs, now I will do some changes to the all_pairs variable to be a tuple with the variable all_couples, bc some things happened when I was coding this and needed to turn the list to tuple cof the counter to work, bc doesn't work with lists, and I need the counter to have the total of repetitions of every pair, also remember that my code deletes every space and newline of the text, so it will detect a pair like "DS" or "D S", also don't judge my code please, I'm not the best programmer in python, just wanted to do this

def quan_pairs():
    global quanpairs
    global all_couples
    toup = ()
    all_couples = []
    it = iter(all_pairs)
    for pair in zip(it):
        toup = pair
        fintoup = str(toup)
        fintoup = fintoup.replace("(['", "")
        fintoup = fintoup.replace("', '","")
        fintoup = fintoup.replace("'],)","")
        all_couples.append(tuple(fintoup))
    quanpairs = collections.Counter(all_couples)

# For better output for the pairs

def pretty_pairs():
    pairs_out = str(quanpairs)
    pairs_out = pairs_out.replace("({('","\n++ [ ")
    pairs_out = pairs_out.replace("', '","")
    pairs_out = pairs_out.replace("'):"," ] appears")
    pairs_out = pairs_out.replace(", ('", " times\n\n++ [ ")
    pairs_out = pairs_out.replace("})"," times")
    pairs_out = pairs_out.replace("Counter","")
    print(pairs_out,"\033[1;32m"+"\n\n[ The total of pairs in this text are", total_pairs,"pairs ] --------------------------------------------"+"\033[0;m")

# Same proccess like the functions from the pairs, but adding one more skip to the letters in the text to found more trios

def get_trios():
    global total_trios
    global all_trios
    all_trios = []
    trio = []
    count = 0
    trio_count = 0
    for letter in file:
        if count == 0:
            count += 1
            continue
        elif letter == '\n' or letter == ' ': continue
        elif len(trio) == 0 or len(trio) == 1 or len(trio) == 2:
            trio.append(letter)
        else:
            all_trios.append(trio[::])
            del trio[::]
            trio.append(letter)
    count = 0
    for letter in file:
        if count != 2:
            count += 1
            continue
        elif letter == '\n' or letter == ' ': continue
        elif len(trio) == 0 or len(trio) == 1 or len(trio) == 2:
            trio.append(letter)
        else:
            all_trios.append(trio[::])
            del trio[::]
            trio.append(letter)
    for letter in file:
        if letter == '\n' or letter == ' ': continue
        elif len(trio) == 0 or len(trio) == 1 or len(trio) == 2:
            trio.append(letter)
        else:
            all_trios.append(trio[::])
            del trio[::]
            trio.append(letter)
    total_trios = len(all_trios)

def quan_trios():
    global quantrios
    global all_threesomes
    toup = ()
    all_threesomes = []
    it = iter(all_trios)
    for trio in zip(it):
        toup = trio
        fintrio = str(toup)
        fintrio = fintrio.replace("(['", "")
        fintrio = fintrio.replace("', '","")
        fintrio = fintrio.replace("'],)","")
        all_threesomes.append(tuple(fintrio))
    quantrios = collections.Counter(all_threesomes)

def pretty_trios():
    trios_out = str(quantrios)
    trios_out = trios_out.replace("({('","\n>>> [ ")
    trios_out = trios_out.replace("', '","")
    trios_out = trios_out.replace("'):"," ] appears")
    trios_out = trios_out.replace(", ('", " times\n\n>>> [ ")
    trios_out = trios_out.replace("})"," times")
    trios_out = trios_out.replace("Counter","")
    print(trios_out,"\033[1;32m"+"\n\n[ The total of trios in this text are", total_trios,"trios ] --------------------------------------------"+"\033[0;m")

# Reading the input from the user

if "-a" in args or "-l" in args:
    create_abc()
    quantity_letters()
    order_letters()
    pretty_letters()
if "-a" in args or "-p" in args:
    get_pairs()
    quan_pairs()
    pretty_pairs()
if "-a" in args or "-t" in args:
    get_trios()
    quan_trios()
    pretty_trios()
if "-x" in args:
    print("\033[1;36m"+"\n=== File content:\n"+"\033[0;m")
    print(file)
elif "-h" in args:
    print(help_message)
    exit()
if len(args) == 0 or "-a" not in args and "-l" not in args and "-p" not in args and "-t" not in args and "-h" not in args and "-x" not in args:
    print("\033[1;31m"+"\n<XXX>"+"\033[0;m"+" Error! The option does not exist")

# In the trios errors could occur such as the script fails to detect a repetition of a trio, it can fail for 1 or 2 repetitions that do not detect but it serves at least to give you a help what are the most repeated trios

opening.close()

# If I said something wrong, it is why I do not speak english natively and may have some failures
