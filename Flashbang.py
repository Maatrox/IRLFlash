import win32gui
import turtle
from pyfirmata2 import *
import time
# ^ Imports for required libraries
board = Arduino("COM4") #Set board and COM port

pin = 5 #Set digital pin that is controlling relay

def flashbang(length): #Function to turn on and off relay
   board.digital[pin].write(1) # 1 - HIGH - ON
   board.pass_time(length) # Time to keep light on
   board.digital[pin].write(0) # 0 - LOW - OFF

def get_colour(i_x, i_y): #Function for checking colour at certain pixel
    #turtle.home() DEBUG to allow physical representation of colour of pixel
    #turtle.dot(100, 'black') DEBUG makes an initial black dot as IDE has white BG
    long_colour = 0 #Set colour value to 0
    while long_colour != 16777215: #While colour is not white - Loop
        i_desktop_window_id = win32gui.GetDesktopWindow() #Gets window
        i_desktop_window_dc = win32gui.GetWindowDC(i_desktop_window_id) #gets context
        long_colour = win32gui.GetPixel(i_desktop_window_dc, i_x, i_y) #gets pixel at coordinates
        #Red =  long_colour & 255 DEBUG for convert to hexadecimal for turtle
        #Green = (long_colour >> 8) & 255 DEBUG for convert to hexadecimal for turtle
        #Blue =   (long_colour >> 16) & 255 DEBUG for convert to hexadecimal for turtle
        #print("#{:02x}{:02x}{:02x}".format(Red,Green,Blue)) DEBUG prints hexadecimal colour code
        #turtle.dot(100, "#{:02x}{:02x}{:02x}".format(Red,Green,Blue)) DEBUG turtle colour dot of hexadecimal
        time.sleep(.300) #3MS sleep to keep program running smoothly (gives it a cheeky nap to collect its thoughts)
    print('FLASHBANGED') #On Loop finish print flashbanged
    flashbang(3) #On loop finish call flashbang function with length
    get_colour(960, 540) #Recalls function to restart program
        #print (long_colour)
        
    
get_colour(960, 540) #Initial call to start program
