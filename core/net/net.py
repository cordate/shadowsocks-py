#coding=utf-8

'''
长连接，短连接，心跳
参考：https://www.cnblogs.com/xilouch/p/4618903.html
https://blog.csdn.net/pmt123456/article/details/58233999
'''
import socket
import time
import threading
import SocketServer
# getattr(tb, 'daifu').save(os.path.join(args.savedir, xlname))

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        cur_thread = threading.current_thread()
        response = "{}: {}".format(cur_thread.name, data)
        self.request.sendall(response)

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

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

'''
异步socket的实现，参见：https://blog.csdn.net/fireroll/article/details/41826803
https://www.cnblogs.com/snailrun/p/3805188.html

SocketServer介绍：https://docs.python.org/2/library/socketserver.html

另外还有一个实现：https://docs.python.org/zh-cn/3/library/asyncore.html
'''
def async_connect_server():
    HOST, PORT = "localhost", 0

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address

    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
    print "Server loop running in thread:", server_thread.name

    server.serve_forever()
    #server.shutdown()
