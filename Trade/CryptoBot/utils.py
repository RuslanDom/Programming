import time
from datetime import datetime
import json

def current_time():
    t = time.time()
    return datetime.fromtimestamp(t).strftime('%d-%m-%Y %H:%M:%S')

def writer_data_json(data, filename):
    with open(filename,'w') as f:
        json.dump(data,f, indent=4)

