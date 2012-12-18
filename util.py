import settings
import sys

def log(msg, skip=False):
    blinkbrew_settings = settings.Blink_Brew_Settings()
    if blinkbrew_settings.show_log:
        sys.stderr.write('%s\n' % msg)

def hexToRGB(color):
    color = color.replace("#", "")
    #print color
    split = (color[0:2], color[2:4], color[4:6])
    return [int(x, 16) for x in split]
