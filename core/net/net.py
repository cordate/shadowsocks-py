#coding=utf-8

'''
长连接，短连接，心跳
参考：https://www.cnblogs.com/xilouch/p/4618903.html
https://blog.csdn.net/pmt123456/article/details/58233999
'''
import socket
import time
# getattr(tb, 'daifu').save(os.path.join(args.savedir, xlname))

def long_connect_server():
    
    BUF_SIZE = 1024
    host = 'localhost'
    port = 8083

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(12) #接收的连接数
    client, address = server.accept()
    while True: #循环收发数据包，长连接
        data = client.recv(BUF_SIZE)
        print(data.decode())

def long_connect_client():
    host = 'localhost'
    port = 8083
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1) #在客户端开启心跳维护
    client.connect((host, port))
    while True:
        client.send('hello world\r\n'.encode())
        print('send data')
        time.sleep(1) #如果想验证长时间没发数据，SOCKET连接会不会断开，则可以设置时间长一点