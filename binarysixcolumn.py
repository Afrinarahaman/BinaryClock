#!/usr/bin/env python

from sense_hat import SenseHat
import time, datetime

hat = SenseHat()


hour_greencolor = (0, 255, 0)
minute_bluecolor = (0, 0, 255)
second_redcolor = (255, 0, 0)

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

#hat.show_message("Programmet starter")   # Message when program starts




#hat.stick.direction_down = time_in_24format
#function to set the binary clock on Sense Hat
def display_binary1(value, row, color):
    binary_str = "{0:8b}".format(value)
    for x in range(0, 8):
        if binary_str[x] == '1':
            hat.set_pixel(row, x , color)
            
        else:
            hat.set_pixel( row, x, off)

def display_binary(value, row, color):
	binary_str = "{0:8b}".format(value)
	for x in range(0, 8):
		if binary_str[x] == '1':
			hat.set_pixel(x, row, color)
		else:
			hat.set_pixel(x, row, off)
       

def binaryclock_sixcolumn(event):
    global flag
    flag=False 
    print(flag)

def time_in_12format():  
    global showtime,hat, flag
    showtime= 12 
    flag=False
    hat.clear()
    print(showtime)
    print(flag)    


#For JoyStick direction
hat.stick.direction_up = time_in_12format

while True:
    t = datetime.datetime.now()
   
    if(flag== True):
         #display_binary
        
        display_binary(t.hour, 2, hour_greencolor)   
        display_binary(t.minute, 3, minute_bluecolor)
        display_binary(t.second, 4, second_redcolor)
        time.sleep(0.0001)

    if(flag==False):
        t = datetime.datetime.now()
        for index in range(0, 5):
                                  
                    hour1=int(t.hour/10)
                    print(hour1)                
                                              
                    hour2=(t.hour%10)
                    print(hour2)
                                 
                    min1=int(t.minute/10)
                    print(min1)
                        
                    min2=(t.minute%10)
                    print(min2)
                                
                    sec1=int(t.second/10)
                          
                    sec2=(t.second%10)
#display_binary til 6 coloner
        display_binary1(hour1, 1, hour_greencolor)   
        display_binary1(hour2, 2, hour_greencolor) 
        display_binary1(min1, 3, minute_bluecolor)
        display_binary1(min2, 4, minute_bluecolor)
        display_binary1(sec1, 5, second_redcolor)
        display_binary1(sec2, 6, second_redcolor)
        time.sleep(0.0001)  

