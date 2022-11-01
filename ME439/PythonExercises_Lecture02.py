
#%% Script with Python Warm-up Challenges for ME439
#%% Note: you may need to add additional packages to your Python if you don't have them already installed: 
#%% For Example, if you're using "anaconda" or "miniconda", one or more of these may be necessary: 
#%% conda install time
#%% conda install math
#%% conda install numpy
#%% conda install matplotlib




#%%
import time 

# get time broken up into its different units
now = time.localtime()
print(now)  # print() sends things to screen

# simple way to get time (not too precise)
print(time.asctime())

#%%
# FOR loop
for ii in range(0,5):  # Notice that it stops at 4! 
    print(ii)
  
for ii in range(0,5,2):  # 'range': Return an object that produces a sequence of integers from start (inclusive) to stop (exclusive) by step
    print('The Time is {0} at sample {1}'.format(time.asctime(),ii) )  # This is Python's complicated way of formatting string output. You type the string in quotes ('  ') with ordered placeholders {0}, {1}, ... and then call the .format() method with the numbers you want as arguments.
    time.sleep(0.5)  # time.sleep puts the process to sleep for the specified number of seconds. NOTE this does not provide strict timing, because the things that happen in the rest of the loop take a little time. 
    
#%%
# WHILE loop with Delay
tstart = time.time()   # time() is current time - seconds since the beginning of the "epoch" (i.e. New Year's moment of 1970 (Unix))
while (time.time() - tstart) < 5:
    print(time.time()) #another option is time.perf_counter())  
    time.sleep(0.5)  
    
    
# CHALLENGE :   
#  
# use a While loop to increment a counter as many times as it can in 1 second

i = 0
start = time.time()
while(time.time() - start < 1):
    i+= 1
print(i)


    
#%%   MATH
import math

# Constants
math.pi  # 'pi' is a constant in the math library
math.e   # so is 'e'

#%% Trigonometry
angle = math.pi/6   # 30 degrees is pi/6 radians
print(math.sin(angle) )    # should be 1/2
print(math.cos(angle))
print(math.sqrt(3)/2  )    # for comparison

#%% Angles in Degrees
angle = 30 

print( math.sin(math.radians(angle)))


# CHALLENGE: 
# 
# use a While loop to print the x, y coordinates of a point moving around a 0.2 m circle at 1 radian per second. Print the coordinates 2 times per second. 

theta = 0
while(theta <= 2*math.pi):
    print(f"({0.2*math.cos(theta)}, {0.2*math.sin(theta)})")
    theta += 0.5
    time.sleep(0.5)


#%% LISTS vs NUMPY Arrays, and PLOTTING
import numpy  # Numerical Python - your new best friend. 

#%% Range object - NO MATH
angles_range = range(0,5,1)   # this makes a "range" object (a form of "generator"), not an actual list! 
2*angles_range  # therefore this will not work
# But if you want to generate a real list from that generator, just call list() on it: 
list(angles_range)
# Then you can repeat it using the * operator: 
2*list(angles_range)

#%% List object - NO MATH
angles_list = [0,1,2,3,4]       # how about listing it explicitly?
2*angles_list  # This gives something different: 2 copies of the list

#%% NUMPY arrays - for MATH
# One way to make a usable array is to call the numpy function to do it: 
angles_numpy_arange = numpy.arange(0,5,1)
print(angles_numpy_arange)
print(2*angles_numpy_arange)

# another way is to convert another object into an array.
angles_array = numpy.array(range(0,5,1))  # here we turn the range into an actual array of angles
print(angles_array)
print(2*angles_array)

#%% OPERATIONS: 
# if you're working with numpy arrays, use the numpy functions on them: 
print(numpy.sin(numpy.radians(angles_array)))
print(numpy.sqrt(angles_array))

#%% Summary Math:
# Summary functions like SUM exist also: 
print(numpy.sum(angles_array))


#%% Plotting and Graphs - MATPLOTLIB PYPLOT
from matplotlib import pyplot as plt    # short tutorial at https://pythonprogramming.net/matplotlib-python-3-basics-tutorial/
import numpy as np

# # Put data on the plot
# plt.plot(angles_array, numpy.sqrt(angles_array))  # plot something on a new (invisible) canvas

# # Annotating the plot
# plt.title('First Graph!')
# plt.ylabel('Square Roots')
# plt.xlabel('Numbers')

# # look at the plot
# plt.show()  # call this to make the plot actually appear

# CHALLENGE: 
# 
# Plot y = x**2 + 1 for x ranging -3 to +3, in 0.01 increments. Label the axes and give it a title. 

fig, ax = plt.subplots()
xs = np.arange(-3, 3, 0.01)
ys = xs**2 + 1

ax.plot(xs, ys)
ax.set_title("title")
ax.set_ylabel("ylabel")
ax.set_xlabel("xlabel")

plt.show()

# %%
