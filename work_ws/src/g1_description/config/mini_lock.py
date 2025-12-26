#!/usr/bin/env python
import rospy, time, os
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

rospy.init_node('mini_lock', anonymous=True)
pub = rospy.Publisher('/joint_trajectory', JointTrajectory, queue_size=1)
time.sleep(1.0)

# 三段角度：低/中/高（只改肩肘，其余保持 URDF 默认）
poses = [
    {   # 低
        'left_shoulder_pitch_joint':  0.0,
        'left_shoulder_roll_joint':   0.0,
        'left_shoulder_yaw_joint':    0.0,
        'left_elbow_joint':           0.0,
        'right_shoulder_pitch_joint': 0.0,
        'right_shoulder_roll_joint':  0.0,
        'right_shoulder_yaw_joint':   0.0,
        'right_elbow_joint':          0.0
    },
    {   # 中
        'left_shoulder_pitch_joint':  0.3,
        'left_shoulder_roll_joint':   0.0,
        'left_shoulder_yaw_joint':    0.0,
        'left_elbow_joint':          -0.6,
        'right_shoulder_pitch_joint': 0.3,
        'right_shoulder_roll_joint':  0.0,
        'right_shoulder_yaw_joint':   0.0,
        'right_elbow_joint':         -0.6
    },
    {   # 高
        'left_shoulder_pitch_joint':  0.6,
        'left_shoulder_roll_joint':   0.0,
        'left_shoulder_yaw_joint':    0.0,
        'left_elbow_joint':          -1.2,
        'right_shoulder_pitch_joint': 0.6,
        'right_shoulder_roll_joint':  0.0,
        'right_shoulder_yaw_joint':   0.0,
        'right_elbow_joint':         -1.2
    }
]

def send(pos_dict, name):
    jt = JointTrajectory()
    jt.joint_names = list(pos_dict.keys())
    p = JointTrajectoryPoint()
    p.positions = [pos_dict[j] for j in jt.joint_names]
    p.time_from_start = rospy.Duration(1.5)
    jt.points.append(p)
    pub.publish(jt)
    time.sleep(2.5)                       # 等稳定
    os.system(f"import -window gazebo /tmp/{name}.png")
    rospy.loginfo(f"Saved {name}.png")

for i, p in enumerate(poses):
    send(p, f"scene_{i}")

rospy.signal_shutdown("Scan done")
