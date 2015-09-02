#!/usr/bin/python

#countItems.py

#script for running through spreadsheets pulled from Google Scholar via Pulbish or Perish,
#determining the number of publications per year, and outputting that info to a separate file
#the program should iterate through a directory of csv files until finished

import csv
import re
import os
import glob
from collections import Counter

#open the first spreadsheet in the directory
#the directory with the files must be called 'data' and this script must live one dir above 'data'

path = './data/'
#get the full path on different operating systems
for infile in glob.glob( os.path.join(path, '*.*') ):
    print("current file is: " + infile)
    researcher = infile[7:]
    print 'researcher: ' + researcher


    with open(infile, 'r+') as readcsv:
        reader = csv.reader(readcsv, delimiter=',')
        yearList = [] 
        for row in reader:
            val = re.compile('\d\d\d\d')
            #print val
            if(val.match(row[3])):
                year = row[3]
                yearList.append(year)
                #print year
    outList = Counter(yearList)                       
    readcsv.close()

    path = './output/'
    glob.glob( os.path.join(path, '*.*'))
    #create an output file in csv format with the name of the input file, but put it in the output directory
    outfile =  path + researcher
    with open(outfile, 'wb') as writecsv:
        writer = csv.writer(writecsv, delimiter=',')

        for key, count in outList.iteritems():
            dYear = key
            writer.writerow([dYear, count])
    writecsv.close()



