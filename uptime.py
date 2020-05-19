import os
import time

server_ip = input('Enter server IP : ')

while (True):
    rep = os.system('ping ' + server_ip)
    if rep == 0:
        print("server is up")
    else:
        print("LOST CONNECTION TO SERVER!!!")
        f = open("uptime.txt", "a")
        f.write("\nConnection to " + server_ip + " lost at this time: " + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
        f.close()
        time.sleep(5)