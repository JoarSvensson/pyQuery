#-------------------------------------------------------------------------------
# Name:        pyQuery
#
# Author:      Joar Svensson
#
# Created:     19-08-2012
# Copyright:   (c) Joar Svensson 2012
# Licence:     GPLv3
#-------------------------------------------------------------------------------
#!/usr/bin/env python

# Import libraries
import glob, os, sys, time

# Define query function
def doQuery(query,fileSuffix,path):
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
                pass

        print ("Query executed in",time.clock() - startTime,
        "seconds, with",totalTimesFound, "results found in",
        totalFileSize/1024/1024, "Mbytes of data")

    except SyntaxError:
        pass

# Perform querying of files in given folder
try:
    doQuery(sys.argv[1],sys.argv[2],sys.argv[3])

except IndexError:
    print("Please pass three arguments, (query path filesuffix)")