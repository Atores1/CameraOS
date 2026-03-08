import numpy as np

red = [64,35,150]
yellow = [191,254,252]
green = [63,96,11]
dy = [0,0,0]
dg = [0,0,0]
for i in range(0,2):
    dy[i] = (yellow[i] - red[i])/127
    dg[i] = (green[i] - yellow[i])/127

print("[[" + str(red[0]) + "," + str(red[1]) + "," + str(red[2])  + "]]")

for i in range(0,127):
    print("[[" + str(round(red[0] + i*dy[0])) + "," + str(round(red[1] + i*dy[1])) + ","+str(round(red[2] + i*dy[2]))+"]]")

print("[[" + str(yellow[0]) + "," + str(yellow[1]) + "," + str(yellow[2])  + "]]")

for i in range(0,127):
    print("[[" + str(round(yellow[0] + i*dg[0])) + "," + str(round(yellow[1] + i*dg[1])) + ","+str(round(yellow[2] + i*dg[2]))+"]]")

print("[[" + str(green[0]) + "," + str(green[1]) + "," + str(green[2])  + "]]")
