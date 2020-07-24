
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import time
import natnet

global ax #, x,y,z
#x ,y, z =[],[],[]

# fig parameters
fig = plt.figure()
ax = fig.add_subplot(111)
ax = p3.Axes3D(fig)

# Setting the axes properties
ax.set_xlim3d([-5, 6.0])
ax.set_xlabel('X')

ax.set_ylim3d([-5.0, 6.0])
ax.set_ylabel('Y')

ax.set_zlim3d([0.0, 3.0])
ax.set_zlabel('Z')

ax.set_title('3D Trajectory')
fig.show()
def cb_1(one, two, three):
    global ax
    print(one[0].position)
    x=one[0].position[1]
    y=one[0].position[0]
    z=one[0].position[2]
    ax.scatter(x, y, z, color='r')
    fig.canvas.draw()
    time.sleep(0.01)

client = natnet.Client.connect(server='192.168.2.41')
client.set_callback(cb_1)
client.spin()