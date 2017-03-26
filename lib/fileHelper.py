from time import strftime
import os.path
import dateutil.parser
from datetime import datetime, timedelta

TEMPLOG_DIR = "/home/pi/homebrewTemps/temperatureLogs"
DATE_FORMAT = "%Y%m%d"
ISO_FORMAT = "%Y-%m-%dT%H:%M:%S"

#get file data as lines method
def get_temps(hours):
    lines = []
    filename = get_filename()
    if not does_file_exist(filename):
        return lines #break out. file has not been created yet today.
    
    with open(filename) as file:
        for line in file:
            if is_line_comment(line):
                continue
            if should_include_line(line, hours):
                lines.append(line.replace("\n", ""))
            
    return lines

def log_temps(tempTuple):
    fileName = get_filename()
    fileExists = does_file_exist(fileName)
    with open(fileName, "a+") as file:
        if not fileExists:
            file.write("#format: Date/Time, OutsideTemp, InsideTemp\n")
        data = strftime(ISO_FORMAT) + "," + str(tempTuple[0]) + "," + str(tempTuple[1]) + "\n"

        file.write(data)
    
def get_filename():
    return TEMPLOG_DIR + "/" + strftime(DATE_FORMAT) + ".txt"

def does_file_exist(filename):
    return os.path.isfile(filename)

def is_line_comment(line):
    return line.startswith('#')

def should_include_line(line, numHours):
    #method to determine whether or not to include line given passed in numHours
    #line should be comma delimted, date in ISO format as first item
    loggedDate = line.split(',')[0]
    parsedDate = dateutil.parser.parse(loggedDate)
    dateDiff = datetime.now() - parsedDate
    return (dateDiff.seconds/3600) <= numHours
