import rospy
from geometry_msgs.msg import Twist

def move_turtle():
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('move_turtle', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    move_cmd = Twist()
    rad = 0
    while not rospy.is_shutdown():
        move_cmd.linear.x = rad
        move_cmd.linear.y = 0
        move_cmd.linear.z = 0
        move_cmd.angular.x = 0
        move_cmd.angular.y = 0
        move_cmd.angular.z = 1

        pub.publish(move_cmd)
        rad += 0.005
        rate.sleep()

if __name__ == '__main__':
    try:
        move_turtle()
    except rospy.ROSInterruptException:
        pass
