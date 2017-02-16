
#!/usr/local/bin/python3.4

import socket, subprocess, sys
import threading
from datetime import datetime

tcount = 10

def scanWorker(ip, ports, results):
   for octet in range(len(results)):
      for p in ports:
         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         s.connect_ex((ip,int(p))) == 0 and results[octet].append("{0} open on {1}".format(ip,p))
         s.close()
      ip = ip[:ip.rindex('.') + 1] + str(int(ip[ip.rindex('.') + 1:]) + 1)
   return results

def chunkTasks(start_ip, stop_ip):
   global tcount
   tasks = []
   start_octet = start_ip[start_ip.rindex('.') + 1:]
   stop_octet = stop_ip[stop_ip.rindex('.') + 1:]
   distance = int(stop_octet) - int(start_octet)
   distance += 1
   if tcount > distance:
      tcount = distance
      chunk = '1.0'
   else:
      chunk = str(distance / tcount)

   for t in range(tcount):
      tasks.append([[] for x in range(int(chunk[0]))])

   if chunk[-1] != '0':
      tasks.append([[] for x in range(int(chunk[-1]))])


   return tasks


if len(sys.argv) != 3:  #only take in 3 arguments, never thought of this....
   print("{0} target_range (e.g. 192.168.0.1-22) port1,port2,port3,...".format(sys.argv[0]))
   sys.exit(0)

t_start = datetime.now()

ips = sys.argv[1]

start_ip = ips[:ips.index('-')]   
  #this is super cool too, first you take the index of '-' in this case it's 11 if using a 192.168.0.1-22
  #then you take the a splice of that argument removing everything off but index 0 - 11 leaving you with 
  #192.168.0.1

end_ip = start_ip[:start_ip.rindex('.') + 1] + ips.split('-')[-1]
  #this one is crazy elegant
  #first he utilize the start_ip variable to extract the network portion of the ip. 
  #he does it by intead of using a regular str.range and giving it an index of where to start becayse 
  #you can easily do str.index('.', 8) but he did it even better, why write more code? he took 
  #the reverse index of '.' and shifted over one to extract the network range. beautiful.
  #with the network range he simply took the original argument supplied by the user and split the ip range
  #into a list of two items with '-' as the delimiter. then simply used the last item as his new octet and 
  #combined it with his network. 
  
ports = sys.argv[2].split(',')

tasks = chunkTasks(start_ip,end_ip)
socket.setdefaulttimeout(2)

threads =[[] for i in range(tcount)]

r_octal,r_base = start_ip[start_ip.rindex('.') + 1:], start_ip[:start_ip.rindex('.') + 1]

for i in range(len(threads)):
   base = r_base + r_octal
   threads[i] = threading.Thread(target=scanWorker, args=(base, ports, tasks[i]))
   threads[i].start()
   r_octal = str(int(r_octal) + len(tasks[i]))
for i in range(len(threads)):
   threads[i].join()

for item in tasks:
   for ips in item:
      for k in range(len(ips)):
         print(ips[k])

t_end = datetime.now()

complete = t_end - t_start

print("Scan finished in {0}".format(complete))
portScan.py
Open with
Displaying portScan.py.
