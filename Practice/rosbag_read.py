import os, fnmatch
import rosbag
from msg_pkg.msg import actual
import numpy as np
import scipy.io

files_name = []
print("Find full file names")

for root, dirs, files in os.walk('bag_folder/'):
    for name in files:
        if fnmatch.fnmatch(name, '*.bag'):
            files_name.append(name)

print(files_name)

print('bag_folder/'+files_name[0])

bag = rosbag.Bag('bag_folder/'+files_name[0])

print(bag)

topics = []
time = []
data = []

time_secs = []
time_nsecs = []

actual_LIFT_torque = []
actual_LIFT_position = []
actual_LIFT_velocity = []

actual_PAN_pos = []

actual_WHEEL_torque = []
actual_WHEEL_velocity = []

data = []

for idx, (topic, msg, t) in enumerate(bag.read_messages(topics=['/actual'])):
    topics.append(topic)
    t.to_time()
    time.append(t)
    time_secs.append(msg.stamp.secs)
    time_nsecs.append(msg.stamp.nsecs)
    actual_LIFT_torque.append(msg.act_LIFT_torque)
    actual_LIFT_velocity.append(msg.act_LIFT_vel)
    actual_LIFT_position.append(msg.act_LIFT_pos)
    actual_PAN_pos.append(msg.act_PAN_pos)
    data.append(msg)

dictionary = {"secs":time_secs,
    "nsecs":time_nsecs,
    "act_LIFT_torque":actual_LIFT_torque,
    "actual_LIFT_pos":actual_LIFT_position,
    "actual_LIFT_velocity":actual_LIFT_velocity}

os.mkdir('mat_folder')

mat = scipy.io.savemat('mat_folder/'+'test.mat',dictionary)

bag.close()