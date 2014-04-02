import MySQLdb
import datetime
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.OUT)
GPIO.output(22, True)
GPIO.setup(24, GPIO.OUT)
GPIO.output(24, True)

localFlags = {'red': 0, 'green': 0, 'override': 0}
localTimings = {'wakeTime': datetime.time(1,00), 'sleepTime': datetime.time(23,00), 'overrideTime': datetime.time(7,30)}

#I'm not quite sure why I need this function??
def getFlags ():
    tempFlags = {'red': 1, 'green': 0, 'override': 0}
    return tempFlags

def getTimings ():
    tempTimings = {'wakeTime': datetime.time(20,48), 'sleepTime': datetime.time(20,50), 'overrideTime': datetime.time(7,30)}
    db = MySQLdb.connect(host="192.168.1.89", user="sleepdb", passwd="sleepdbpass", db="sleepdb")
    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor() 

    # Use all the SQL you like
    cur.execute("SELECT name, time FROM times")

    # print all the first cell of all the rows
    print "Selected %s rows" % cur.rowcount
    for row in cur.fetchall() :
        print row[0], row[1]
        dummyDate = datetime.datetime(2000,1,1,0,0) + row[1]
        dummyTime = dummyDate.time()
        tempTimings[row[0]] = dummyTime
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
        #print tempTimings
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
        #print "turning red light on"
        GPIO.output(24, False)
    else:
        #turn light off
        #print "turning red light off"
        GPIO.output(24, True)

    if tempFlags['green'] == 1:
        #turn light on
        #print "turning green light on"
        GPIO.output(22, False)
    else:
        #turn light off
        #print "turning green light off"
        GPIO.output(22, True)

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
checkDBInterval = 20
checkStatusInterval = 5

while keepLooping:
    checkDBDelta = datetime.datetime.now() - lastDBCheck
    checkStatusDelta = datetime.datetime.now() - lastStatusCheck

    if checkDBDelta.seconds >= checkDBInterval:
        print "Checking DB..."
        localTimings = getTimings()
        lastDBCheck = datetime.datetime.now()

    if checkStatusDelta.seconds >= checkStatusInterval:
        print "Checking Status..."
        localFlags = checkStatus(localFlags, localTimings)
        setLights(localFlags)
        lastStatusCheck = datetime.datetime.now()
    
    time.sleep(5)
