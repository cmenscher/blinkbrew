class Blink_Brew_Settings:
    def __init__(self):
	    self.name = "blinkbrew"
	    self.show_log = True
	    self.blink_cmd = "/usr/local/bin/blink1-tool"
	    self.named_actions = {
	    	"color": "--rgb",
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
	            "description": "This service will listen for a Hex color value or a named color pattern for a blink1 and will display accordingly.",
	            "subscribe": {
	                "messages": [
	                    {
	                        "name": "disco",
	                        "type": "number"
	                    },
	                    {
	                        "name": "color",
	                        "type": "string"
	                    }
	                ]
	            }
	        }
	    }
