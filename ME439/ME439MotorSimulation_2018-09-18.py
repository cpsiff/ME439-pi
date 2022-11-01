# -*- coding: utf-8 -*-
"""
Updated Sep 14 2018
@author: Peter Adamczyk
"""

import numpy as np
from matplotlib import pyplot as plt


# Global Variables
# controller variables
controller_error = 0.0
controller_error_previous = 0.0
controller_error_integral = 0.0
controller_error_derivative = 0.0

# =============================================================================
# MOTOR MODEL
# =============================================================================
class dcMotorSimulator:
    def __init__(self, kt=4.46e-3, R=3.21, J=5.26e-8, dt=0.01): # motor constant in nM/A; Resistance in Ohms; Motor Inertia in kg*m^2
        # Numbers above from Maxon motor 118587: RE 13 3 Watt motor
        self.kt = kt
        self.R = R
        self.J = J
        self.dt = dt
        self.tlast = np.nan     # "tlast" keeps a record of the last simulation time when the "update" function was called. 
        
        # Initialize the state: 0 angle (theta), 0 speed (omega), 0 acceleration (alpha)
        self.theta = 0.0
        self.omega = 0.0
        self.alpha = 0.0
        
    # Define a method for this class that updates the motor state. 
    # THIS IS A DYNAMIC SIMULATOR: 
    def update_state(self,t,Vmotor,Tload):
        if not np.isnan(self.tlast):
            # time step "dt" is how much time has elapsed between "tlast" and the present time "t"
            self.dt = t - self.tlast    
            #  
            # What does the next line do? 
            # update the angle according to speed
            #
            self.theta = self.theta + self.omega*self.dt + 1./2.*self.alpha*self.dt**2
            #  What does the next line do? 
            # update speed according to the derivative of speed
            self.omega = self.omega + self.alpha*self.dt
            
        # Now determine what "alpha" is for the next time step based on the applied voltage of the motor and the motor law. 
        # This is the rotational Newton-Euler equation: (Torque = I*alpha), incorporating the motor's electromechanical properties as well. 
        self.alpha = self.kt/(self.R*self.J)*Vmotor - self.kt**2/(self.R*self.J)*self.omega - Tload/self.J
        self.tlast = t
        

# =============================================================================
# CONTROLLER - a generic PID controller function
# =============================================================================
def pidControl(target, actual, dt):
    """
    takes a target value and an actual value, and dt, and computes PID controller output
    """
# =============================================================================
#     # MANIPULATE THESE CONSTANTS TO TUNE THE CONTROLLER
# =============================================================================
    Kp = 0.     # Proportional gain
    Ki = 1.     # Integral gain
    Kd = 0.1     # Derivative gain
    
    # We are using Global variables just so they stay in memory. 
    # NOTE they are initialized at the top of the file! 
    global controller_error, controller_error_previous, controller_error_integral, controller_error_derivative
    # Compute the error: difference between the target and the actual current state. 
    controller_error = target - actual
    #  What does the next line do? 
    # just calculates the integral by adding to the previous integral whatever the new segment is
    controller_error_integral = controller_error_integral + dt*controller_error
    #  What does the next line do? 
    # finite approximation of controller error derivative
    controller_error_derivative = (controller_error - controller_error_previous)/dt
    # We are done with the previous value of error... set that variable to the current error to remember it for next timestep. 
    controller_error_previous = controller_error
    
    # Actually compute the Motor command
    command = Kp*controller_error + Ki*controller_error_integral + Kd*controller_error_derivative
    return command



# =============================================================================
# MAIN FUNCTION (will be called automatically at bottom)
# =============================================================================
def main():
    dt = 0.01
    time_max = 5.0  # duration of simulation, in Seconds
    step_time = 1.0 # time at which a Step Function occurs
    Vnom = 6.0  # Volts, the nominal operating voltage
    Vmax = 7.4  # Volts, as in a Lithium Polymer battery
    n = np.ceil(time_max/dt).astype("int")  # number of points
    

    
# =============================================================================
#     # Here we create an object of class "dcMotorSimulator"
# =============================================================================
    # This motor is based on the Maxon 119587 motor specs (default), 
    # assuming a 100:1 gear reduction (note factors on kt and J).
    motor = dcMotorSimulator(kt=4.46e-3*1.0e2, R=3.21, J=5.26e-8*1.0e4 + 0.02, dt=0.01)


    # Arrays to collect data. [Could also be used to set up pre-specified commands, e.g. by planning a sequence of "targets"]
    time_array = np.transpose(np.array(range(n),ndmin=2)*dt)    # "range" builds a row vector, so it has to be transposed to make a column vector.
    target_array = np.zeros([n,1])  # Array to accumulate values the motor will be asked to hit. 
    actual_array = np.zeros([n,1])  # Array to accumulate values the motor actually hits
    control_voltage_array = np.zeros([n,1])     # Array of control voltages
    load_torque_array = np.zeros([n,1])     # Array of load torques
    theta_array = np.zeros([n,1])       # Array of motor angles
    omega_array = np.zeros([n,1])       # Array of motor speeds
    
    
    
# =============================================================================
# # Now here's the LOOP that will RUN THE SIMULATION AND THE CONTROLLER
# =============================================================================
    for ii in range(n):
        t = ii*dt # update the time
        
# =============================================================================
# # HERE put a task to control, and a controller to compute the command for the motor   
# # # Several examples are shown; try them all, try disabling some. 
# =============================================================================
        
#        #Example: Open-Loop command: simple step in the voltage drive signal        
#        if t < step_time:
#            Vcommand = 0.0
#            Tload = 0.0
#        else:
#            Vcommand = 4.460   # Volts
#            Tload = 0.1   # Can apply a Load Torque if you want
#        target = 0.
#        actual = 0.
        
        
        #Example: Step function for Target Speed, PID Control
        # Do this many times to tune the gains Kp, Ki, Kd in the PID Controller "pidControl" above. 
        if t < step_time:
            target_omega = 0.0
        else:
            target_omega = 10.0
        # if (int(t*10) % 2 == 0):
        #     target_omega = 0
        # else:
        #     target_omega = 10
#            # Extra code for adding multiple steps
#            if t > 2.0*step_time:
#                target_omega = 5.0 # (rad/s)
#            if t > 3.0*step_time:
#                target_omega = 7.0 # (rad/s)

        # Could apply a Load Torque if desired
        Tload = 0.0   

        ## HERE the CONTROLLER actually does its work: 
        # 
        # What does the next line do? 
        # 
        target = target_omega   
        # What does the next line do? 
        #  
        actual = motor.omega    
        # Call the PID controller to get a new motor command.
        Vcommand = pidControl(target, actual, dt)
        
        
        ### Idea: do the same, but with Position (target_theta, motor.theta)
        # if t < step_time:
        #     target_theta = 0.0
        # else:
        #     target_theta = 10.0
        # target = target_theta
        # actual = motor.theta
        # Vcommand = pidControl(target, actual, dt)
        
        
        # Enhancement: Study the effect of command saturation. The motor driver cannot give a command higher than battery voltage.
        if Vcommand > Vmax:
            Vcommand = Vmax
        elif Vcommand < -Vmax:
            Vcommand = -Vmax
# =============================================================================
#         
# =============================================================================
        
        # Here apply the Voltage Command and any Load Torque to the Motor and update its dynamic state
        motor.update_state(t,Vcommand,Tload)
        
        # Harvest a record of the commands and actual motor state for plotting
        target_array[ii] = target
        actual_array[ii] = actual
        control_voltage_array[ii] = Vcommand
        load_torque_array[ii] = Tload
        theta_array[ii] = motor.theta # all motor angles
        omega_array[ii] = motor.omega # all motor speeds
# =============================================================================
# # END OF SIMULATION AND CONTROL LOOP
# =============================================================================
    
    # When the loop has finished, plot the data
    plt.figure()
    line_handles = plt.plot(time_array, np.concatenate([target_array, actual_array, control_voltage_array, load_torque_array, theta_array, omega_array], axis=1))
    plt.legend(line_handles,["Target","Actual","Vcommand","Tload","Theta","Omega"])
    plt.xlabel("Time (s)")
    plt.ylim([-10,25])
    plt.show()


# =============================================================================
# # Special Commands that interface with Python's automatically created 
# # variables to Run the Main function
# =============================================================================
if __name__ == "__main__":
    try: 
        main()
    except KeyboardInterrupt: 
        pass

