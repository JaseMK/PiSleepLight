PiSleepLight
============

A small project to build a traffic light system for my toddler son's bedroom so he 
knows when it's time to wake up and when it's time to stay in bed.

The main application is a Python program, running on a Raspberry PI, using the GPIO pins to drive a 
series of coloured LEDs. The current system status along with all system settings and timings are held in a 
MYSQL DB (also stored on the Raspberry Pi, although not necessarily so).

The DB can also be viewed and updated via a set of PHP/Javascript pages (again, rnning on a local
Apache/PHP server, although technically could be hosted anywhere that has access to yhe DB), 
intended to be used on a smart phone. Other smartphone features include things such as a 
'lie-in' function, snooze buttons and so on.

