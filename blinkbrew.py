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

    def blink(self, name="color", value="#FF0000", times=1):
        # Using the blink1-tool commandline prog for now
        # I'd prefer to use something smaller/native like the
        # blink1raw tool in blink1/commandline but it won't
        # compile for me.  In the end it may be best to use
        # the blink1 URL API but that no worky either. *sigh*
        blink_cmd = self.settings.blink_cmd
        
        #first, turn off the blink1
        print "TURNING OFF..."
        led_off = "0,0,0"
        args_off = [blink_cmd, "--rgb", led_off]
        subprocess.call(args_off)

        # now determine the action from the published name
        action = app.settings.named_actions[name]

        if name == "color": 
            if value[0] == "#":
                color = util.hexToRGB(value)

            #create the pattern
            led_on = ",".join(str(v) for v in color)
            args_on = [blink_cmd, app.settings.named_actions[name], led_on]
        elif name == "disco":
            times = int(value)
            args_on = [blink_cmd, app.settings.named_actions[name], "1"]

        print "BLINKING %d TIMES..." % int(times)
        for i in range(times):
            subprocess.call(args_on)
            time.sleep(app.settings.default_sleep)
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
