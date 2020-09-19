# C:\Users\colet\Desktop\print-timestamps.py
# others are in:
# C:\Program Files\obs-studio\data\obs-plugins\frontend-tools\scripts
# Python 3.6.8 in C:\Users\colet\AppData\Local\Programs\Python\Python36

import time
import obspython as obs

# event handlers? 

# how abut just try to run something simple
print(time.time()) # where can I see logging? 42:50
# why no log? Wrong Python version, and not pointing to correct folder
print("heloo wordl")

obs.script_log(obs.LOG_WARNING, "Error opening URL cole '")