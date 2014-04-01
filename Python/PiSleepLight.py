import datetime
import time

localFlags = {'red': 0, 'green': 0, 'override': 0}
localTimings = {'wakeTime': datetime.time(7,00), 'sleepTime': datetime.time(19,00), 'overrideTime': datetime.time(7,30)}

def getFlags ():
    tempFlags = {'red': 1, 'green': 0, 'override': 0}
    return tempFlags

def getTimings ():
    tempTimings = {'wakeTime': datetime.time(14,15), 'sleepTime': datetime.time(14,20), 'overrideTime': datetime.time(7,30)}
    return tempTimings

def checkStatus (tempFlags, tempTimings):
    newFlags = tempFlags

    nowDate = datetime.datetime.now()
    nowTime = nowDate.time()
    #Are we in the green zone?
    if (nowTime > tempTimings['wakeTime']) & (nowTime < tempTimings['sleepTime']):
        #we are in the green zone
        print "It's wake time"
        newFlags['green'] = 1
        newFlags['red'] = 0
    else:
        #we must therefore be in the red zone
        print "It's sleep time"
        newFlags['green'] = 0
        newFlags['red'] = 1

    #check to see if the flags have changed, if so, write back to DB
    if tempFlags <> newFlags:
        print "Updating DB with new flags"
        #insert update DB code here

    return newFlags

    
def setLights (tempFlags):
    if tempFlags['red'] == 1:
        #turn light on
        print "turning red light on"
    else:
        #turn light off
        print "turning red light off"

    if tempFlags['green'] == 1:
        #turn light on
        print "turning green light on"
    else:
        #turn light off
        print "turning green light off"

    if tempFlags['override'] == 1:
        #turn light on
        print "override on"
    else:
        #turn light off
        print "override off"

localFlags = getFlags()
localTimings = getTimings()

newTime = datetime.time(19,45)
print newTime

nowDate = datetime.datetime.now()
nowTime = nowDate.time()

print nowTime
print nowTime > newTime

print "Red: %s" % localFlags['red']
print "Green: %s" % localFlags['green']
print "Override: %s" % localFlags['override']

#main loop to go here
lastDBCheck = datetime.datetime.now()
lastStatusCheck = datetime.datetime.now()
keepLooping = True
checkDBInterval = 30
checkStatusInterval = 5

while keepLooping:
    checkDBDelta = datetime.datetime.now() - lastDBCheck
    checkStatusDelta = datetime.datetime.now() - lastStatusCheck

    if checkDBDelta.seconds >= checkDBInterval:
        print "Checking DB..."
        localFlags = getFlags()
        lastDBCheck = datetime.datetime.now()

    if checkStatusDelta.seconds >= checkStatusInterval:
        print "Checking Status..."
        checkStatus(localFlags, localTimings)
        setLights(localFlags)
        lastStatusCheck = datetime.datetime.now()
    
    time.sleep(5)
