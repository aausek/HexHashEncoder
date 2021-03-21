import csv
import hashlib
import binascii
from binascii import hexlify
from io import StringIO
from datetime import datetime
import os
import time
import pandas as pd
import itertools
import threading
import time
import sys

now = datetime.now()
today_date = now.strftime("%m-%d-%Y")
today_date2 = now.strftime("%m-%d-%Y" + " %H:%M:%S")
print('')
print('')
print('-------------------------Welcome to the master automation machine---------------------------------')
print('')
print('')
time.sleep(1)
print("-------------------------Today is:", today_date2, "-----------------------------")
print('')
print('')

# Declare and define path variables
inputPath = '/Users/aausek/Desktop/CODE/excel-automation/INPUT/'
outputPath = '/Users/aausek/Desktop/CODE/excel-automation/OUTPUT/'

# time.sleep(1)

# Function definition
def readWriteFn(client, inputFile, outputFile, cleanFile):

    # Check client name
    print("Loading " + client)  
    
    # Read and write files
    if os.path.isfile(inputFile) == True:
            # Read input file 'csvfile'
            data = pd.read_csv(inputFile)
            # creates new file with duplicated data dropped
            data[~data.duplicated(subset=['Email'])].to_csv(outputFile, index=False)
            with open(outputFile) as csvfile: 
                with open(cleanFile, "a") as output:
                    reader = csv.DictReader(csvfile, quotechar='"', delimiter=",", quoting=csv.QUOTE_ALL, skipinitialspace=True)
                    # Define new columns for hashed/hexed data in output file
                    fieldnames = reader.fieldnames + ['TA1', 'TA2']
                    writer = csv.DictWriter(output, fieldnames)
                    # writes column names
                    writer.writeheader()
                    # writes data to each row
                    for i, r in enumerate(reader):        
                        # all data in HashString column replaced with hashed version of data
                        r['TA1'] = hashlib.md5((r['HashString']).encode('utf-8')).hexdigest()
                        # all data in HexString column replaced with ascii hex version of data
                        r['TA2'] = r['HexString'].encode().hex()
                        # writes data to new file
                        writer.writerow(r)
                    # prints to terminal to verify duplicates are gone and that hash/hex formulas worked
                    # print(data)
                    # time.sleep(1)
                    print("Success " + client + " done\n")
                    time.sleep(1)                
                    # os.remove(inputFile)

                    # Removing input files with duplicates
                    os.remove(outputFile)
    else:
        # time.sleep(1)
        print("Nothing for " + client + " today :( \n")
        # time.sleep(1)
        # print("Loading next client ...")

# Calling function with parameters
readWriteFn("Name", inputPath + 'Name.csv', outputPath + today_date + 'Name.csv', outputPath + today_date + 'Name clean.csv')
readWriteFn("Name", inputPath + 'Name.csv', outputPath + today_date + 'Name.csv', outputPath + today_date + 'Name clean.csv')
readWriteFn("Name", inputPath + 'Name.csv', outputPath + today_date + 'Name.csv', outputPath + today_date + 'Name clean.csv')
readWriteFn("Name", inputPath + 'Name.csv', outputPath + today_date + 'Name.csv', outputPath + today_date + 'Name clean.csv')   

# Confirms removal of all input files
print("Removing input files...\n")
