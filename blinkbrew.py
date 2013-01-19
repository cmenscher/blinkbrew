import websocket
import thread
import time
import settings
import util
from util import log as log
import json
import subprocess

class Blink_Brew:
    def __init__(self):
        self.settings = settings.Blink_Brew_Settings()

    def on_message(self, ws, message):
        msg = json.loads(message)
        data = msg["message"]
        print "\n\n%s\n\n" % data
        self.blink(name=data["name"], value=data["value"], times=self.settings.default_times)

    def on_error(self, ws, error):
        print error

    def on_close(self, ws):
        print "### closed ###"

    def on_open(self, ws):
        def run(*args):
            time.sleep(1)
            #ws.send("%s" % json.dumps(self.settings.spacebrew_name_message))
            ws.send("%s" % json.dumps(self.settings.spacebrew_config))
            time.sleep(1)
        thread.start_new_thread(run, ())

    def blink(self, name="flash", value="#FF0000", times=1, turn_off=True):
        print "BLINKING BLINKING BLINKING"
        # Using the blink1-tool commandline prog for now
        # I'd prefer to use something smaller/native like the
        # blink1raw tool in blink1/commandline but it won't
        # compile for me.  In the end it may be best to use
        # the blink1 URL API but that no worky either. *sigh*
        blink_cmd = self.settings.blink_cmd
        
        #determine the action from the published name
        action = app.settings.named_actions[name]

        print "NAME=%s" % name

        if name == "flash": 
            print "FLASHING COLOR: %s" % value
            if value[0] == "#":
                color = util.hexToRGB(value)

            #create the pattern
            led_on = ",".join(str(v) for v in color)
            args_on = [blink_cmd, app.settings.named_actions[name], led_on]

        elif name == "color": 
            print "SETTING COLOR: %s" % value
            if value[0] == "#":
                color = util.hexToRGB(value)

            #don't turn off the blink(1)
            turn_off = False

            #create the pattern
            led_on = ",".join(str(v) for v in color)
            args_on = [blink_cmd, app.settings.named_actions[name], led_on]

        elif name == "disco":
            print "EVERYBODY DANCE! (times=%s)" % value
            times = 1 #disco should only run once
            fade = "-m 50" #speed up the color fade to 50ms
            interval = "-t 100" #speed up the time between colors to 100ms (default=300ms)
            args_on = [blink_cmd, app.settings.named_actions[name], value, interval, fade]

        #if necessary, turn off the blink1
        if turn_off:
            print "TURNING OFF..."
            args_off = [blink_cmd, "--off"]
            subprocess.call(args_off)

        for i in range(times):
            subprocess.call(args_on)
            time.sleep(app.settings.default_sleep)
            if turn_off:
                subprocess.call(args_off);
                time.sleep(app.settings.default_sleep)


if __name__ == "__main__":
    app = Blink_Brew()
    websocket.enableTrace(True)
    uri = "%s:%s" % (app.settings.spacebrew_server, app.settings.spacebrew_server_port)
    ws = websocket.WebSocketApp(uri,
        on_message = app.on_message,
        on_error = app.on_error,
        on_close = app.on_close)

    ws.on_open = app.on_open

    ws.run_forever()
