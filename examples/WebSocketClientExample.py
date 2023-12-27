import logging
import sys
import stockMData
import json
sys.path.append('../')
from pmClient.WebSocketClient import WebSocketClient
# public access token
webSocketClient = WebSocketClient("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJtZXJjaGFudCIsImlzcyI6InBheXRtbW9uZXkiLCJpZCI6NTQ5MDc5LCJleHAiOjE2OTY0NDQxOTl9.O4ZVMCTAuTZGOAglltqS8H1J9upvfYYlm2VtVQPQwOY")

customerPreferences = []

def getInstrumentList():
    configpref = []
    with open('instrument.txt', 'r') as f:
        lines = f.read().splitlines()
        for instrumentcode in lines:
            tempDict = {
                "actionType": "ADD",
                "modeType": "QUOTE",
                "scripType": "EQUITY",
                "exchangeType": "NSE",
            }
            tempDict["scripId"] = str(instrumentcode)
            configpref.append(tempDict)
        return configpref

instrumentlist = getInstrumentList()

for pref in instrumentlist:
    customerPreferences.append(pref)


def on_open():
    # send preferences via websocket once connection is open
    webSocketClient.subscribe(customerPreferences)


def on_close(code, reason):
    # this event gets triggered when connection is closed
    print(code, reason)


def on_error(error_message):
    # this event gets triggered when error occurs
    print(error_message)

def getfilepath():
    import time
    import os
    folderpath = "/Users/suniltonger/a_sunil/code/pyPMClient/"
    timestr = time.strftime("%Y%m%d")
    resultPath = os.path.join(folderpath,timestr)
    return resultPath

filename = getfilepath()
print(filename)
def append_to_file(data):
    import json
    for item in data:
        datafilepath = filename + "_" + str(item['security_id']) +".json"
        print("writing to file: " + datafilepath)
        with open(datafilepath, 'a') as f:
            f.writelines(json.dumps(item))
            f.write("\r\n")


def on_message(arr):
    # this event gets triggered when response is received
    append_to_file(arr)
    #print(arr)


webSocketClient.set_on_open_listener(on_open)
webSocketClient.set_on_close_listener(on_close)
webSocketClient.set_on_error_listener(on_error)
webSocketClient.set_on_message_listener(on_message)

"""
set below reconnect config if reconnect feature is desired
Set first param as true and second param, the no. of times retry to connect to server shall be made  
"""
webSocketClient.set_reconnect_config(True, 5)


# this method is called to create a websocket connection with broadcast server
webSocketClient.connect()


