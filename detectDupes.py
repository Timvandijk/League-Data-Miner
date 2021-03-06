#!/usr/bin/python3

import time
import os.path
import sys
import json
from collections import Counter

def read_matchIds(inputFile):
    print("Reading json")
    print('')
    with open(inputFile, 'r') as database:
            data = json.load(database)
    database.close()
    return data
    
def main():
    ids = []
    name = input('Name of the file?:')
    ids += read_matchIds("matchInfo_part_"+str(curIndex)+".json")
    counter = Counter(ids)
    for mId, amount in counter.items():
        if amount>1:
            print(str(mId) + " " + str(amount))

if __name__ == "__main__":
    main()
