from __future__ import print_function
from Arduino import Arduino
import time

baud="9600"
board = Arduino(baud, port="")
board.SoftwareSerial.begin(2, 3, baud)

#function for sending
def Sending(message, number):
	print("about to send...")
	board.SoftwareSerial.write('AT+CMGF=1')
	time.sleep(2)
	print('AT+CMGF=1\n')
	board.SoftwareSerial.write('AT+CMGS=\"'+number+'\"')
	print('AT+CMGS=\"'+number+'\"\n')
	time.sleep(2)
	board.SoftwareSerial.write(message)
	time.sleep(3)
	board.SoftwareSerial.write('0x1A');
	time.sleep(1)
	board.SoftwareSerial.write('0x0D');
	board.SoftwareSerial.write('0x0A');

file = open("../../logs/log.txt", 'r')
numline=0
number=""
message=""
for line in file:
	l=line[10:].strip()
	if(line[:7]=="send to"):
		number = l
		numline+=1
	if(line[:7]=="message"):
		message = l
		numline +=1
	
	if(numline==2):
		numline=0
		Sending(message, number)
		time.sleep(10)



def kk():
	print "Hoo haa"
	x=open('aaaaaaa.txt','w')
