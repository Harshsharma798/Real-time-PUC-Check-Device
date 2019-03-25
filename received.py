import os
import  socket

serv=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serv.bind(('',12345))
serv.listen(5)


def accept_frame():
    print 'Waiting for Connection'
    conn, addr=serv.accept()

    with open('examples/TEST.png','wb') as img:
        while True:
            data1=conn.recv(1024)
            if not data1:
                break
            img.write(data1)

    print 'received, Yay...!'
#text=conn.recv(1024)

accept_frame()
os.system('python3 classify.py --model 101.model --labelbin mlb.pickle --image examples/TEST.png')


#conn.close()

#print text


