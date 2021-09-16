#!/usr/bin/env python3
import socket
import time

#define address & buffer size
HOST = "" # can do HOST = "localhost", but "" defaults to "localhost"
PORT = 8001
BUFFER_SIZE = 1024

# the purpose of the echo server is to echo back whatever was originally sent to it
# in the lab, we try sending a string to it
# if you send a string to the echo server, it recieves that string and sends it back
def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        #QUESTION 3
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #check documentation as to which one lets you reuse address
        
        #bind socket to address
        s.bind((HOST, PORT))
        #set to listening mode
        s.listen(2)
        
        #continuously listen for connections
        while True:
            conn, addr = s.accept()
            #print connection information to terminal (Step 4)
            print("Connected by", addr)
            
            #to echo: recieve data, wait a bit, then send it back
            full_data = conn.recv(BUFFER_SIZE)
            time.sleep(0.5)
            conn.sendall(full_data)
            conn.close() #make sure to close the connetion!

if __name__ == "__main__":
    main()
