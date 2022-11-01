#!/usr/bin/env python

# Animation example code

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

##%%  Note: if Spyder will not animate: 
# Go into Tools--> Preferences --> IPython Console --> Graphics --> Backend --> Select "Tkinter"
# Also had to call FuncAnimation with "blit=False" (see line 151)
#


#%%  THIS IS THE ROBOT SIMULATOR Class
# Class that creates a "robot" object, with various methods for kinematics, below. 
# Call it as in the fucntion "main()": 
#   rbt = robot(width, length) 
class robot:
    # Required Method to Initialize the robot, including the arguments to the function call
    def __init__(self,wheel_width,body_length):
        self.path_world_x = np.array([])
        self.path_world_y = np.array([])
        
        self.wheel_width = wheel_width
        self.body_length = body_length

        self.set_position(0,0,0)
        self.set_velocity_bf(0,0)
        self.set_wheel_speed(0,0)  # left and right wheel speeds
        body_width_ratio = 0.8
        wheel_length_ratio = 0.4
        
        self.corners_bodyfixed_x = np.array( (wheel_width/2, wheel_width/2, body_width_ratio*wheel_width/2, body_width_ratio*wheel_width/2, -body_width_ratio*wheel_width/2, -body_width_ratio*wheel_width/2, -wheel_width/2, -wheel_width/2, wheel_width/2) )  # last corner closes the shape
        self.corners_bodyfixed_y = np.array( (body_length*(-wheel_length_ratio/2), body_length*(wheel_length_ratio/2), body_length*(wheel_length_ratio/2), body_length*(1-wheel_length_ratio/2), body_length*(1-wheel_length_ratio/2), body_length*(wheel_length_ratio/2), body_length*(wheel_length_ratio/2), body_length*(-wheel_length_ratio/2), body_length*(-wheel_length_ratio/2)) )
        self.corners_bodyfixed_xy = np.vstack( (self.corners_bodyfixed_x,self.corners_bodyfixed_y) )
        
        self.get_corners_world_xy()  # get the Earth frame XY coords of the corners. 
        
        
    # Method to set the Position of the robot, (x, y, theta)
    def set_position(self,x_center_world,y_center_world,theta):
        self.x_center_world = float(x_center_world)
        self.y_center_world = float(y_center_world)
        self.theta = float(theta)   
        
        self.path_world_x = np.append(self.path_world_x, self.x_center_world)
        self.path_world_y = np.append(self.path_world_y, self.y_center_world)
        
    # Method to set the Body-frame velocity of the robot. 
    def set_velocity_bf(self,ydot_center_bf,thetadot):
        self.xdot_ydot_center_bf = np.array([0, float(ydot_center_bf)])
        self.thetadot = float(thetadot)  
        
        self.set_velocity_world_from_bf()
        
    # Method to set the World-frame velocity based on the Body-frame velocity
    def set_velocity_world_from_bf(self):
        self.get_rotmat_body_to_world()
        xdot_ydot_center_world = np.dot( self.rotmat_body_to_world, self.xdot_ydot_center_bf )
        self.xdot_center_world = xdot_ydot_center_world[0]
        self.ydot_center_world = xdot_ydot_center_world[1]

    # Method to directly set the velocity of the robot in the World frame
    def set_velocity_world(self,xdot_center_world,ydot_center_world,thetadot):
        self.xdot_center_world = float(xdot_center_world)
        self.ydot_center_world = float(ydot_center_world)
        self.thetadot = float(thetadot)        
        
    # Method to compute a Rotation Matrix from the robot to the world
    def get_rotmat_body_to_world(self):
        self.rotmat_body_to_world = np.array([ [np.cos(self.theta), -np.sin(self.theta)],[np.sin(self.theta), np.cos(self.theta)]])
        
    # Method to compute the locations of the vertices of the robot graphic
    def get_corners_world_xy(self): 
        self.get_rotmat_body_to_world()
        
        self.corners_rotated_xy= np.dot( self.rotmat_body_to_world, self.corners_bodyfixed_xy )
        self.corners_world_x = self.x_center_world + self.corners_rotated_xy[0]
        self.corners_world_y = self.y_center_world + self.corners_rotated_xy[1]
        self.corners_world_xy = np.vstack( (self.corners_world_x,self.corners_world_y) )
        
    # Method to calculate the velocity of the robot from its wheel speeds
    def set_wheel_speed(self, left_wheel_speed, right_wheel_speed):
        self.left_wheel_speed = left_wheel_speed
        self.right_wheel_speed = right_wheel_speed
        
#### Put in Equations (i) and (ii) here based on self.left_wheel_speed, self.right_wheel_speed, and self.wheel_width
        v_center_y_bf = 0
        omega = 0
        
        self.set_velocity_bf(v_center_y_bf, omega)  # Body-fixed velocity of the robot. 
        
        
    # Method to update the state of the robot using a simple Euler integration. 
    def update_state(self, dt):
        # *****
        # Program some rules for updating the state: 
        # *****
        self.set_velocity_world_from_bf()  # convert the body-frame velocity of the robot into world-frame coordinates. 
        
        self.x_center_world += dt * self.xdot_center_world   # simulates constant velocity toward +x
        self.y_center_world += dt * self.ydot_center_world   # simulates constant velocity toward +y
        self.theta += dt * self.thetadot      # simulates constant rotational speed (+z rotation)
        
        # this updates the record of the path the robot has traveled. 
        self.path_world_x = np.append(self.path_world_x, self.x_center_world)
        self.path_world_y = np.append(self.path_world_y, self.y_center_world)
        
        self.get_corners_world_xy()
        

#%% Function to update the robot and path drawing. 
# It works by keeping "objects" in the graph, and updating the data with "setdata"        
# Note the first line, which actually performs an integration step and updates the robot's state! 
def update_drawing(num, rbt,rbtline,pathline, dt) :
    rbt.update_state(dt)
    rbtline.set_data(rbt.corners_world_x,rbt.corners_world_y)
    pathline.set_data(rbt.path_world_x, rbt.path_world_y)
    print("{} {}".format(rbt.x_center_world,rbt.y_center_world))
    return rbtline, pathline

    
#%%  # Define a "main" function that includes the script we actually want to execute. 
def main(): 
    # *** Here is the code that executes the actual program    
    # Create a robot and set its position. 
#### Measure your Robot, put in its parameters, and define its start pose
    robot0 = robot(0.100,0.150)  # Parameters are the wheel width and body length. 
    robot0.set_position(0.1,0.05,0) # This function magically sets the robot in the pose you specify (x, y, theta)
    robot0.set_velocity_bf(0.05,0.05) # This function magically sets the robot's velocity: linear (forward) and angular (right hand rule)
#### Once you have updated the function "set_wheel_speed" above, you can call that instead: 
    # robot0.set_wheel_speed(wheelspeedleft, wheelspeedright)
    
    fig1= plt.figure()
    
    robot0line, = plt.plot([], [], 'r-')
    robot0path, = plt.plot([],[], 'b--')
    plt.axis('equal')   # Note for some reason this has to come before the "xlim" and "ylim" or an explicit axis limits command "plt.axis([xmin,xmax,ymin,ymax])"
    plt.xlim(-1, 1)
    plt.ylim(-1, 2)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Robot Test')
    
#### Play with what happens if your simulation time-step (dt) is larger or smaller
    dt = 0.1   # seconds
    
    # In this strange simulator, the animation object itself is controlling the time-stepping and calling other functions. This is how it's set up. 
    # Look up "FuncAnimation" to see how it works! 
    # Hint: at "interval" of dt it calls the function "update_drawing" with the arguments in "fargs"
    line_ani = animation.FuncAnimation(fig1, update_drawing, frames=1, fargs=(robot0, robot0line, robot0path, dt), interval= (dt*1000), repeat=True, blit=False)
    plt.show()
    
    return line_ani # If the animation function is not returned, it will be destroyed when the function exits and therefore will not animate. 



#%% Alternative manual way to animate, without "FuncAnimation". Much slower! 
#    import time
#    for ii in range(0,100,1) :
#        update_drawing(ii, robot0, robot0line, robot0path)
#        plt.show()
#        plt.draw()
#        fig1.canvas.draw()
#        time.sleep(dt)
#        

#%%  This is where the program will actually start running - the first non-"define" statements! 
import traceback # This library allows you to print exceptions (errors) that occur. see "traceback.print_exc()" below.  
if __name__=="__main__":
    try:
        ani = main()

    except Exception:
        traceback.print_exc() 
