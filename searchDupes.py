#!/usr/bin/python3

import time
import os.path
import sys
import json

def write_matchInfo(outputFile, matchInfo):
    encoder = json.JSONEncoder()
    with open(outputFile, 'w') as database:
            database.write(encoder.encode(matchInfo))
    print("Done writing.")
    print('')
    database.close()

def read_matchInfo(inputFile):
    print("Reading json")
    print('')
    with open(inputFile, 'r') as database:
            data = json.load(database)
    database.close()
    return data
                
def strip_info(matchInfo):
    strippedInfo = []
    for matchElement in matchInfo:
        if matchElement == None:
            print('match '+str(matchElement)+' = NONE ERORORORORORORO EROOOOR')
            continue
        strippedInfo.append(matchElement['matchId'])
    return strippedInfo
    
def main():
    parts = 10
    ids = []
    for curIndex in range(parts):
        print("Start part " + str(curIndex))
        temp = read_matchInfo("matchInfo_part_"+str(curIndex)+".json")
        print("Stripping info..")
        ids += strip_info(temp)
    write_matchInfo("clean_match_part.json", temp, curIndex)
    print("Writing it to disk..")


if __name__ == "__main__":
    main()
