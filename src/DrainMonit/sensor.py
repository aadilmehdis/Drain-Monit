import requests as req
import numpy as np
import time

URL = "http://127.0.0.1:8000/"

k = 1
date = 1
while(1):
    dateString = '%s-1-2019' % date
    rate = 1000 + np.random.rand(1) * 600
    DATA = {'UID':k, 'Flow_rate':rate,'Date':dateString}
    print(DATA)
    k = k + 1
    if k > 8:
        k = 1
        date = date + 1
        if date > 30:
            date = 1

    r = req.post(url = URL, data =  DATA)    
    time.sleep(15.0)

    


