import re
import os 
import os.path as osp

# Scaled. Acc (mg) [  00066.65, -00013.67,  01038.09 ], Gyr (DPS) [  00007.02,  00001.52, -00000.30 ], Mag (uT) [  00000.00,  00000.00,  00000.00 ], Tmp (C) [  00025.78 ]
import scipy.io

# Read the data from the file
filepath  = "C:\\Users\\ezxtz6\\Downloads\\CoolTermWin\\1.txt"
with open(filepath, 'r') as file:
    data = file.read()

# Extract the numbers using regular expressions
numbers = re.findall(r'[-+]?\d*\.\d+|\d+', data)

# Convert the numbers to floats
numbers = [float(num) for num in numbers]

# Save the numbers to a MATLAB file
scipy.io.savemat('data.mat', {'numbers': numbers})