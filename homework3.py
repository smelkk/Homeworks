#1
"""
import sys

print("Python version", sys.version)
print("Version info.", sys.version_info)
"""
#2
"""
import datetime

now = datetime.datetime.now()

print("Current date and time:")
print(now.strftime("%Y-%m-%d %H:%M:%S"))
"""
#3
""""
import math

radius = input("Enter the radius: ")
area = math.pi * float(radius) ** 2

print("The area of the circle is:", area)
"""
#4
"""
filename = input("Enter a filename: ")

name, extension = filename.split(".")

print("The extension of the file is:", extension)
"""
#5
"""
color_list =["Red" , "Green" , "White" ,"Black"]
print("First and last colours are", color_list[0], "and", color_list[-1])
"""
#6
"""
exam_st_date = (11, 12, 2014)
ls=[]
for i in range(0, len(exam_st_date)):
    ls.append(exam_st_date[i])

for k in range(0,len(ls)):
    ls[k]=str(ls[k])

exams=" / ".join(ls)
print(exams)
"""
#7
"""
number=input("Enter a number: ")
number1=str(number)*2
number2=str(number)*3
s=int(number)+int(number1)+int(number2)
print(s)
"""



#16
"""
import os.path

filename = input("Enter the filename to check: ")

if os.path.exists(filename):
    print("The file", filename, "exists.")
else:
    print("The file", filename, "does not exist.")
"""
#17
"""
import struct


bitness = struct.calcsize("P") * 8

if bitness == 32:
    print("Python is running in 32-bit mode.")
elif bitness == 64:
    print("Python is running in 64-bit mode.")
else:
    print("Unable to determine the bitness of Python.")
"""
#18
"""
import platform

os_name = platform.system()

platform_name = platform.platform()

release_version = platform.release()

print("OS name:", os_name)
print("Platform name:", platform_name)
print("Release version:", release_version)
"""
#19
"""
import subprocess

if subprocess.call(["ls"]) == 0:
    print("Command executed successfully.")
else:
    print("Command failed to execute.")
"""
#20
"""
import multiprocessing

num_cpus = multiprocessing.cpu_count()

print("Number of CPUs:", num_cpus)
"""
#21
"""
import os

dir_path = os.getcwd()

file_list = os.listdir(dir_path)

print("Files in", dir_path, "directory:")
for file_name in file_list:
    if os.path.isfile(os.path.join(dir_path, file_name)):
        print(file_name)
"""
#22
"""
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
c = int(input("Enter third integer: "))

min_val = min(a, b, c)
max_val = max(a, b, c)
mid_val = (a + b + c) - min_val - max_val

print("Sorted integers:", min_val, mid_val, max_val)
"""
#23
"""
import os
import datetime

dir_path = os.getcwd()

file_list = os.listdir(dir_path)

# Creating a dictionary to store the file creation times
creation_times = {}
for file_name in file_list:
    file_path = os.path.join(dir_path, file_name)
    if os.path.isfile(file_path):
        creation_time = os.path.getctime(file_path)
        creation_times[file_name] = datetime.datetime.fromtimestamp(creation_time)

# Sorting the files by creation time
sorted_files = sorted(creation_times.items(), key=lambda x: x[1])

print('Files in', dir_path, 'sorted by creation date:')
for file_name, creation_time in sorted_files:
    print(file_name, creation_time)
"""
#24
"""
ls = [5, 8, 12, 7, 10]

fixed = 4

for num in ls:
    if num <= fixed:
        print('Not all numbers in the list are greater than', fixed)
        break
else:
    print('All numbers in the list are greater than', fixed)
"""
#25
"""
ls = ['d',1,'&','P',2,1,'d',1,'%','&']
spec = '&'
s=0
for i in ls:
    if i==spec:
        s+=1
print("The number of", spec, 'in list is',s)
"""
#26
"""
import os

path = '/users/smelk/myfile.csv'

filename = os.path.basename(path)

print('Filename:', filename)
"""
#27
"""
ls = [1,2,3,4,5]
ls.pop(0)
print(ls)
"""
#28
"""
my_input = input("Enter a number: ")

try:
    number = int(my_input)
    print("You entered the number:", number)
except ValueError:
    print("Error: You did not enter a number.")
"""
#29
"""
number = float(input("Enter a floating-point number: "))

decimals = int(input("Enter the number of decimal places to round to: "))

rounded_number = round(number, decimals)
print("The rounded number is:", rounded_number)
"""
#30
"""
string = input("Enter a string: ")
if any(char.islower() for char in string):
    print("String contains lowercase letters.")
else:
    print("String does not contain lowercase letters.")
"""
#31
"""
string = input("Enter a variable-length string: ")

# Split the string into variables
variable1, variable2, variable3 = string.split()

# Print the variables
print("Variable 1:", variable1)
print("Variable 2:", variable2)
print("Variable 3:", variable3)
"""
#32
"""
import os

home_directory = os.path.expanduser("~")
base_directory = os.path.basename(home_directory)
print(base_directory)
"""
#33
"""
value1 = True
value2 = False
int1 = int(value1)
int2 = int(value2)
print(f"{value1} is {int1}, {value2} is {int2}")
"""
#34
"""
number = 13
binary = format(number, '08b')
print(binary)
"""
#35
"""
ls=[1,3,5,6,3,2,1,4,10,-3]
max_ls=ls[0]
min_ls=ls[0]
for i in ls:
    if max_ls<i:
        max_ls=i
    if i<min_ls:
        min_ls=i
print("The minimum number is", min_ls)     
print("The maximum number is", max_ls)
"""
#36
"""
spec=8
s=0
for i in range(0,spec):
    s+=i**3
print("The sum is", s)
"""