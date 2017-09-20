import numpy as np
import matplotlib.pyplot as plt
import time

# Question 4
# This code will show each transformation in sequence from a) -> f) and will output the original coordinates of each
# of the 5 points on the rigid body followed by their new coordinates after the transformation. The plot that displays
# this transformation is also set up to display each step from a) -> f) for 2 seconds before moving onto the next...
# IN ORDER TO DISABLE THIS AND HAVE TO MANUALLY CLOSE THE PLOT BEFORE MOVING ON TO THE NEXT:
#       replace plt.show(block = False)  with plt.show(block = True) everywhere you see !!!!!!!!!!! notation
points = np.array([[-1.0,1.0], [0.0,1.0], [1.0,0.0], [0.0,-1.0], [-1.0,-1.0]])
plt.plot(points[:,0], points[:,1], 'bX')    #Blue Xs represent beginning

# The Z-coordinate must be 1 in order to preserve the displacement when doing a transformation
rigidShape = [np.matrix([[-1.0],[1.0],[1.0]]),
              np.matrix([[0.0],[1.0],[1.0]]),
              np.matrix([[1.0],[0.0],[1.0]]),
              np.matrix([[0.0],[-1.0],[1.0]]),
              np.matrix([[-1.0],[-1.0],[1.0]])]

a = np.matrix([[1.0, 0.0, 4.0],
             [0.0, 1.0, 0.0],
             [0.0, 0.0, 1.0]])

b = np.matrix([[0.866, 0.5, 0.0],
             [-0.5,0.866,0.0],
             [0.0, 0.0, 1.0]])
# a)
print ("4. a)_________________________________")
XList1 = []
YList1 = []
count = 1
for i in rigidShape:
    print ("Point" + str(count))
    ai = a*i
    print("Original:")
    print (i)
    print("Transformation")
    print (a*i)
    #Append these to be used later to shade-in the shape demarcated by the coordinates
    XList1.append(ai[0,0])
    YList1.append(ai[1,0])
    print ("")
    plt.plot(ai[0,0],ai[1,0], 'ro')   #Red circles on points
    count = count + 1

# Fill up the space between the points in the transformed coordinate system
plt.fill(XList1,YList1)
axis = plt.gca()
axis.set_xlim([-2,6])
axis.set_ylim([-3,3])

plt.show(block = False) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
time.sleep(2)       # Show this diagram for 2 seconds
plt.close()


#==============================================================================================================
# b)
print ("4. b)_________________________________")

# Replot the points
plt.plot(points[:,0], points[:,1], 'bX')    

XList1[:] = []
YList1[:] = []
count = 1
for i in rigidShape:
    print ("Point" + str(count))
    abi =a*b*i
    print("Original:")
    print (i)
    print("Transformation")
    print (abi)
    XList1.append(abi[0,0])
    YList1.append(abi[1,0])
    print ("")
    plt.plot(abi[0,0],abi[1,0], 'ro')
    count = count + 1
# Fill up the space between the points in the transformed coordinate system
plt.fill(XList1,YList1)
axis = plt.gca()
axis.set_xlim([-2,6])
axis.set_ylim([-3,3])

plt.fill(XList1,YList1)
plt.show(block = False) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
time.sleep(2)
plt.close()

#==============================================================================================================
# c)

print ("4. c)_________________________________")

# Replot the points
plt.plot(points[:,0], points[:,1], 'bX')    

XList1[:] = []
YList1[:] = []
count = 1
for i in rigidShape:
    print ("Point" + str(count))
    bai =b*a*i
    print("Original:")
    print (i)
    print("Transformation")
    print (bai)
    XList1.append(bai[0,0])
    YList1.append(bai[1,0])
    print ("")
    plt.plot(bai[0,0],bai[1,0], 'ro')
    count = count + 1
# Fill up the space between the points in the transformed coordinate system
plt.fill(XList1,YList1)
axis = plt.gca()
axis.set_xlim([-2,6])
axis.set_ylim([-3,3])

plt.fill(XList1,YList1)
plt.show(block = False) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
time.sleep(2)
plt.close()

#==============================================================================================================

# d)
print ("4. d)_________________________________")
# Replot the points
plt.plot(points[:,0], points[:,1], 'bX')   

XList1[:] = []
YList1[:] = []
count = 1
for i in rigidShape:
    print ("Point" + str(count))
    bi = b*i
    print("Original:")
    print (i)
    print("Transformation")
    print (bi)
    #Append these to be used later to shade-in the shape demarcated by the coordinates
    XList1.append(bi[0,0])
    YList1.append(bi[1,0])
    print ("")
    plt.plot(bi[0,0],bi[1,0], 'ro')   #Red circles on points
    count = count + 1

# Fill up the space between the points in the transformed coordinate system
plt.fill(XList1,YList1)
axis = plt.gca()
axis.set_xlim([-2,6])
axis.set_ylim([-3,3])

plt.show(block = False) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
time.sleep(2)       # Show this diagram for 2 seconds
plt.close()


#==============================================================================================================
# e)

print ("4. e)_________________________________")

# Replot the points
plt.plot(points[:,0], points[:,1], 'bX')    

XList1[:] = []
YList1[:] = []
count = 1
for i in rigidShape:
    print ("Point" + str(count))
    abi =a*b*i
    print("Original:")
    print (i)
    print("Transformation")
    print (abi)
    XList1.append(abi[0,0])
    YList1.append(abi[1,0])
    print ("")
    plt.plot(abi[0,0],abi[1,0], 'ro')
    count = count + 1
# Fill up the space between the points in the transformed coordinate system
plt.fill(XList1,YList1)
axis = plt.gca()
axis.set_xlim([-2,6])
axis.set_ylim([-3,3])

plt.fill(XList1,YList1)
plt.show(block = False) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
time.sleep(2)
plt.close()

#==============================================================================================================
# f)

print ("4. f)_________________________________")

# Replot the points
plt.plot(points[:,0], points[:,1], 'bX')    

XList1[:] = []
YList1[:] = []
count = 1
for i in rigidShape:
    print ("Point" + str(count))
    bai =b*a*i
    print("Original:")
    print (i)
    print("Transformation")
    print (bai)
    XList1.append(bai[0,0])
    YList1.append(bai[1,0])
    print ("")
    plt.plot(bai[0,0],bai[1,0], 'ro')
    count = count + 1
# Fill up the space between the points in the transformed coordinate system
plt.fill(XList1,YList1)
axis = plt.gca()
axis.set_xlim([-2,6])
axis.set_ylim([-3,3])

plt.fill(XList1,YList1)
plt.show(block = False) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
time.sleep(2)
plt.close()

# This section below was used in order to compute the homogenous transformation matrix from Pittsburgh to GreenWhich
'''
from numpy.linalg import inv

GreenwhichInclination = np.matrix([[np.cos(-51*np.pi/180), 0, np.sin(-51*np.pi/180), 0],
                 [0, 1, 0, 0],
                 [-np.sin(-51*np.pi/180), 0, np.cos(-51*np.pi/180), 0],
                 [0, 0, 0, 1]])

extension2Surface = np.matrix([[1, 0, 0, 0],
                 [0, 1 , 0, 0],
                 [0, 0, 1, -6000],
                 [0, 0, 0, 1]])

extension2Core = np.matrix([[1, 0, 0, 0],
                 [0, 1 , 0, 0],
                 [0, 0, 1, 6000],
                 [0, 0, 0, 1]])


pitInclination = np.matrix([[np.cos(40.5*np.pi/180), 0, np.sin(40.5*np.pi/180), 0],
                 [0, 1 , 0, 0],
                 [-np.sin(40.5*np.pi/180), 0, np.cos(40.5*np.pi/180), 0],
                 [0, 0, 0, 1]])

pitMeridian = np.matrix([[1, 0, 0, 0],
                 [0, np.cos(80*np.pi/180) , -np.sin(80*np.pi/180), 0],
                 [0, np.sin(80*np.pi/180), np.cos(80*np.pi/180), 0],
                 [0, 0, 0, 1]])


H = extension2Core * pitInclination * pitMeridian * GreenwhichInclination * extension2Surface
print (H)
'''

