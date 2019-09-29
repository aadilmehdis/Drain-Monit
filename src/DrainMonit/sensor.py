import requests as req
import numpy as np
import time
from time import gmtime, strftime

URL = "http://127.0.0.1:8000/sensor_data"

id = 1
while(1):

    date = strftime("%Y-%m-%d %H:%M:%S", gmtime()).split(' ')[0]
    rate = 1000 + np.random.rand(1) * 600
    DATA = {'UID':id, 'flow_rate':rate,'date':date}
    print(DATA)
    r = req.post(url = URL, data =  DATA)

    id = (id + 1) % 9
    if id == 0 :
        id = 1

    time.sleep(15.0)
