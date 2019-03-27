from threading import Thread
import socket
import os

#setting IP and port
TARGET_IP = '127.0.0.1'
TARGET_PORT = 9000

#setting socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((TARGET_IP, TARGET_PORT))
sock.listen(1) 
 
 
def Fungsi(trg_ip, trg_port): 
    print "masuk ke fungsi\n" 
    while True:
        data = conn.recv(1024)   

        if(data=="rq"):
            print "masuk ke request\n" 
            namafile = conn.recv(1024)   
            print(namafile)

            conn.send("START {}" . format(namafile))
            ukuran = os.stat(namafile).st_size
            fp = open(namafile,'rb')
            k = fp.read()
            sent=0
            for x in k:
                conn.send(x)
                sent = sent + 1
                print "\r Sent {} of {} " . format(sent,ukuran)
            conn.send("DONE")
            fp.close()
        conn.send("END") 
         
        
     

 
                

while True:
    print "waiting from client..." 
    conn,addr=sock.accept() 

    thread = Thread(target = Fungsi, args = (addr))
    thread.start()
     