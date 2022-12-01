#!/usr/bin/env python

from sense_hat import SenseHat
import time, datetime

import signal
import sys


hat = SenseHat()

#function for ending the program when it it being interrupted
def signal_term_handler(signal, frame):
    hat.show_message('Program Slutter')
    sys.exit(0)
 
signal.signal(signal.SIGTERM, signal_term_handler)
signal.signal(signal.SIGINT,signal_term_handler)
 

#Colors for hour, minutes, seconds, am and pm
hour_greencolor = (0, 255, 0)
minute_bluecolor = (0, 0, 255)
second_redcolor = (255, 0, 0)
am_color=(0,255,255)
pm_color=(255,255,0)
command_color=(255,105,180)
#color for setting off
off = (0, 0, 0)

hat.clear()

#Initialize the global variable
showtime=0
flag=True
global hour1
hour1=0
global hour2
hour2=0
global min1
min1=0
global min2
min2=0
global sec1
sec1=0
global sec2
sec2=0


hat.show_message("Programmet starter")   # Message when program starts


#function to set the binary clock on Sense Hat in columns
def display_binary_column(value, row, color):
    binary_str = "{0:8b}".format(value)
    for x in range(0, 8):
        if binary_str[x] == '1':
            hat.set_pixel(row, x , color)
            
        else:
            hat.set_pixel( row, x, off)
#function to set the binary clock on sense hat in rows
def display_binary_row(value, row, color):
	binary_str = "{0:8b}".format(value)
	for x in range(0, 8):
		if binary_str[x] == '1':
			hat.set_pixel(x, row, color)
		else:
			hat.set_pixel(x, row, off)
       
#function to set the clock on Sense Hat in row and 12 hours format
def binaryclock_12format_row(event):
    global flag,hat,showtime
    showtime= 12 
    flag=True
    
    hat.clear()
    hat.set_pixel(0,0,am_color)
    print(showtime)
    #print(flag)

#function to set the clock on Sense Hat in row and 24hours format
def binaryclock_24format_row(event):
    global flag,hat,showtime
    showtime= 0
    flag=True
    
    hat.clear()
    hat.set_pixel(0,0,pm_color)
    print(showtime)
    #print(flag)

#function to change clock 24 hrs format to 12 hours format ans show in column
def time_in_12format_column(event):  
    global showtime,hat, flag
    showtime= 12 
    flag=False
    hat.clear()
    hat.set_pixel(0,0,am_color)
    print(showtime)
    #print(flag)  

#function to change clock 12 hrs format to 24 hours format ans show in column  
def time_in_24format_column():
    global showtime,hat,flag
    showtime= 0
    
    flag=False
    
    hat.clear()
    hat.set_pixel(0,0,pm_color)
    print(showtime)

#For JoyStick direction
hat.stick.direction_up = time_in_12format_column
hat.stick.direction_down =time_in_24format_column
hat.stick.direction_left= binaryclock_24format_row
hat.stick.direction_right= binaryclock_12format_row


def Main():
    global flag, showtime
    flag=True
    showtime=12
    ## Passing arguments to program from the commandsprompt
    if len(sys.argv[1::])>0:

        cmd, val =sys.argv[1].split('=')
        if cmd =='dir':
            if val == 'h':
                #hat.set_pixel(0,0,command_color)
                flag=True
            if val =='v':
                flag=False
        elif cmd=='clock-time':
            if val=='24h':
                showtime=0
            if val=='12h':
                showtime=12
    #Running until it is being interrupted
    while True:
        t = datetime.datetime.now()
        if (t.hour > 12 & showtime == 12):
            hour= t.hour-12  
        else:
            hour = t.hour

        if(flag == True):
            #display_binary to three rows
          

            display_binary_row(hour, 2, hour_greencolor)   
            display_binary_row(t.minute, 3, minute_bluecolor)
            display_binary_row(t.second, 4, second_redcolor)
            time.sleep(0.0001)


        if(flag==False):
            t = datetime.datetime.now()
            for index in range(0, 5):
                                    
                        hour1=int(hour/10)
                        print(hour1)                
                                                
                        hour2=(hour%10)
                        print(hour2)
                                    
                        min1=int(t.minute/10)
                        print(min1)
                            
                        min2=(t.minute%10)
                        print(min2)
                                    
                        sec1=int(t.second/10)
                            
                        sec2=(t.second%10)
    #display_binary to six columns
            display_binary_column(hour1, 1, hour_greencolor)   
            display_binary_column(hour2, 2, hour_greencolor) 
            display_binary_column(min1, 3, minute_bluecolor)
            display_binary_column(min2, 4, minute_bluecolor)
            display_binary_column(sec1, 5, second_redcolor)
            display_binary_column(sec2, 6, second_redcolor)
            time.sleep(0.0001)  

if __name__ == "__main__":
    Main()