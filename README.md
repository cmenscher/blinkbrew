blinkbrew
=======================

This is a Python script for the ThingM blink(1) device (http://blink1.thingm.com/).  The script will connect to a Spacebrew server (http://spacebrew.cc) in order to subscribe to published Spacebrew events and trigger the blink(1) to, uh, blink.

Be sure you have the Python "websocket-client" (https://github.com/liris/websocket-client) library installed.  You can do this either via "python setup.py install" or "pip install websocket-client".