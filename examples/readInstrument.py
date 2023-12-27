
import csv


def readInstrumentFile():
    # opening the CSV file
    with open('equity_security_master.csv', mode ='r')as file:

        # reading the CSV file
        csvFile = csv.reader(file)

        # displaying the contents of the CSV file
        for lines in csvFile:
            print(lines[0] + " : " + lines[1])

readInstrumentFile()

