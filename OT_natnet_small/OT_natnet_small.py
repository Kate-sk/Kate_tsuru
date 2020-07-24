def cb_1(one, two, three):
    #coord=[one[0].position[1], one[0].position[0],one[0].position[2]]
    #my_file = open("OT_Clover_data.txt", "a")
    #my_file.write(str(coord)+"\n")
    #temp = one[0].orientation[] * 3.14/180
    print(one[1])

import natnet

client = natnet.Client.connect(server='192.168.2.41')
#my_file = open("OT_Clover_data.txt", "w")

#client.set_callback(cb_1)
client.set_model_callback(cb_1)
#client.set_model_callback(lambda rigid_bodies, markers, timing: print(rigid_bodies))
#client.set_callback (lambda rigid_bodies, markers, timing: print(markers))
client.spin()