"""
The purpose of this program is to generate a log file with the following characteristics:
There's exactly one syslog message on each line. The messages are in the "old"
(BSD) syslog format (that is, consisting of PRI, HEADER and MSG) as defined by
the standard.

Every message adheres to the standard and all the messages come from the same year.

The produced file may be very large (dozens of gigabytes). 
"""

import random
import string



my_file = open("input.txt","w+") 
for i in range(123456789):
    priority_value = random.randint(0,23)*8+random.randint(0,7)
    Mmm = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    month = random.choice(Mmm)
    day = random.randint(1,28)
    if day < 10:
        day = " "+str(day)
    else:
        day = str(day)
    TIMESTAMP_w_s = str(month)+" "+str(day)+" 0"+str(random.randint(0,9))+":0"+ str(random.randint(0,9))+":"
    secs = random.randint(10,59)
    msg_tag = "su:"
    msg_content = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(random.randint(0,6)))
    HOSTNAME = random.choice(Mmm)
    my_file.write("<"+str(priority_value)+">"+str(TIMESTAMP_w_s)+str(secs)+" "+str(HOSTNAME)+" "+msg_tag+" "+str(msg_content))
    my_file.write("\n")
my_file.close()