#-------------------------------------------------------------------------------
# Name:        pyQuery.py
#
# Author:      Joar Svensson
#
# Created:     2012-08-19
# License:     GPLv3
#
# Download: git@github.com:JoarSvensson/pyQuery.git
#
# Usage: python pyQuery.py "John Doe" *.txt C:\TestFolder
#        The search string is case sensitive
#
#-------------------------------------------------------------------------------
#!/usr/bin/env python

# Import libraries
import glob, os, sys, time

# Define query function
def main(query,fileSuffix,path):
    try:
        print("Executing query.. please wait")
        startTime = time.clock()
        totalFileSize = 0
        totalTimesFound = 0
        os.chdir(path)
		
        for fileName in glob.glob(fileSuffix):
            fileSize = os.path.getsize(fileName)
            totalFileSize = totalFileSize + fileSize
            infile = open(fileName,"r")
            text = infile.read()
            infile.close()

            if (query in text):
                timesFound = text.count(query)
                totalTimesFound = totalTimesFound + timesFound
                index = text.find(query)
                print(query, "was found", timesFound, "times,",
                "first time at index:", index, "in file", fileName)

            else:
                print(query, "was not found!")

        print ("Query executed in",time.clock() - startTime,
        "seconds, with",totalTimesFound, "results found in",
        totalFileSize/1024/1024, "Mbytes of data")

    except SyntaxError, error:
        print(error)

# Perform querying of files in given folder

if __name__ == "__main__":
    try:
        main(sys.argv[1],sys.argv[2],sys.argv[3])

    except IndexError:
        print("Please pass three arguments, (query filesuffix path)")
