import pandas as pd
import time
import natnet

def cb_1(one, two, three):
    print('local_time', time.time())
    for i in range(len(two)):
        print('marker_id',two[i].marker_id, two[i].position, end = ',')
    print('\n')
    #print ('local_time', time.time(), '\n', 'optitrack_data', two[0].position, 'optitrack_time', three.timestamp)

#start listening Optitrack
client = natnet.Client.connect(server='192.168.2.41')
client.set_callback(cb_1)
client.spin()