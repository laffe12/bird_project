# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 11:48:58 2016
@author: Adam Rosén
"""
from  scipy import *
from  pylab import *
from datetime import datetime
from dateutil import tz


#############################################################################################
### This takes a few seconds to run, but the file is of size ~ 8 MB, so I think its ok :) ###
#############################################################################################


### In this class the time_date object and counts are stored. One class contains values for one line from the text file. 
class BirdClass:
    def __init__(self, date_time, counts): # Initializing variables
       self.date_time = date_time
       self.counts = int(counts)    # Converting to int
       
       
def read_file_info():
    # Declaring time zones here instead of inside time_zone_converter to avoid calling them 200.000 + times
    from_zone = tz.gettz('UTC') 
    to_zone = tz.gettz('CET')   # We want to convert to central european time. Timezone format given in file
    
    
    data_arr=[]     # Array to store values, where each element is of typ BirdClass
    
    
    f = open('bird.txt','r')    # Opening the file in reading mode
    
    for line in f:  # Iteration through file, line by line
        
        date, time, counts = line.split() # Splitting lines and stores them in temporary variables
        
        date_time = date + " " + time   # Concatenating the date and time strings to enable the use of datetime object.
        
        cet_date_time = time_zone_converter(date_time, from_zone, to_zone)     # Calling time zone converter to convert date_time string to CET time   
        
        data = BirdClass(cet_date_time, counts) # Using data to access passing values into BirdClass. Creating one new object for every iteration. Each element in data_arr has its own memory address
        data_arr.append(data)   # Each element is of type BirdClass, containing values from each line in input file
        
    
    f.close()   # Frees memory occupied by the file

   
    return data_arr # returns the data_array


### Converts dates/times to CET 
def time_zone_converter(date_string, from_zone, to_zone):   # taking a string, from time zone and to time zone as arguments
    
    
    utc = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S.%f')    # Creates a date.time object. First arg is a string, second argument is the string format %H = 24-hour time format etc..
    utc = utc.replace(tzinfo=from_zone)     # Basically telling the object that it is of UTC time format
        
    cet_date_time = utc.astimezone(to_zone) # The conversion!
        
    return cet_date_time    # Returns date.time object


### Accessing the values in the file
data = read_file_info()
print(data[0].date_time)
print(data[1].date_time)
print(data[0].counts)
print(type(data[0].date_time))
print(type(data[0].counts))

        