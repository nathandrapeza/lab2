#!/usr/bin/enc python3
import socket, time, sys
from multiprocessing import Process

#define global address and buffer size
HOST = "localhost"
PORT = 8001
BUFFER_SIZE = 1024

# get_remote_ip:
def get_remote_ip(host):
    print(f'Getting IP for {host}')
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print("Hostname coult not be resolved. Exiting.")
        sys.exit()

    print(f"IP address of {host} is {remote_ip}")
    return remote_ip

# handle_request() method
def handle_request(addr, conn):
    print("Connecte by", addr)

    full_data = conn.recv(BUFFER_SIZE)
    conn.sendall(full_data)
    try:
        conn.shutdown(socket.SHUT_RDWR)
    except:
        pass
    conn.close

def main():

    HOST = "localhost"
    PORT = 8001
    BUFFER_SIZE = 1024
    extern_host = 'www.google.com'
    extern_port = 80

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_start:
        proxy_start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        proxy_start.bind((HOST, PORT))
        proxy_start.listen(1)

        while True:
            #connect proxy_start
            conn, addr = proxy_start.accept()
            #information about connection:
            print("Connected by", addr)

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:
                # get remote ip of google, connect proxy_end to it
                remote_ip_google = get_remote_ip(extern_host)
                proxy_end.connect((remote_ip_google, extern_port))
                        
                # send data (not in pseudocode but is point of this program)
                #is taken care of by handle_request

                #multiprocessing:
                p = Process(target=handle_request, args=(addr,conn))
                p.daemon = True
                p.start()
                print("Started process", p)

                # does not specify to sned recieved data back to client?

            # closing connection
            conn.close()

if __name__ == "__main__":
    main()
