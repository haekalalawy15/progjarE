import socket
import os
import sys

save_path ='D:\Tugas 3\Client'

 
request1="x"
UPLOAD="x"

TARGET_IP = "127.0.0.1"
TARGET_PORT = 9000

command = sys.argv[1] 
requestfile = sys.argv[2] 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TARGET_IP, TARGET_PORT)) 


try:
    print("masuk ke try") 
    while True:  
        print("masuk ke try") 
        sock.send(command)
        print("inidata") 

        if(command=="rq"):
            print("masuk ke rq")
            sock.send(requestfile)
            print(requestfile)
            while True:
                data = sock.recv(1024) 
                print("ini data")
                print(data)
                if(data[0:5]=="START"):
                    print "full data ",data
                    file_name=os.path.join(save_path,data[5:])

                    print "Menerima ",data[5:]
                    fp = open(file_name,'wb+')
                    ditulis = 0
                elif(data[0:4]=="DONE"):
                    fp.close()
                elif(data[0:3]=="END"):
                    break
                else:
                    print "Blok ", len(data), data[0:10]
                    fp.write(data)      
     
     
finally:
    print >> sys.stderr, 'closing socket'
    sock.close()



       
    
             


