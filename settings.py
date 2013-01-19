class Blink_Brew_Settings:
    def __init__(self):
	    self.name = "blinkbrew"
	    self.show_log = True
	    self.blink_cmd = "/usr/local/bin/blink1-tool"
	    self.named_actions = {
	    	"flash": "--rgb",
	    	"disco": "--random",
	    }
	    self.default_times = 3
	    self.default_sleep = 0.5
	    self.spacebrew_server = "ws://localhost"
	    self.spacebrew_server_port = 9000
	    self.spacebrew_name_message = {"name": [{"name": self.name}]}
	    self.spacebrew_config = {
	        "config": {
	            "name": self.name,
	            "description": "This service subscribes to a series of events to make the ThingM blink(1) boogie.",
	            "subscribe": {
	                "messages": [
	                    {
	                        "name": "disco",
	                        "type": "number"
	                    },
	                    {
	                        "name": "flash",
	                        "type": "string"
	                    }
	                ]
	            }
	        }
	    }
