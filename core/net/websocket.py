#coding=utf-8

from flask import Flask 
from flask_socketio import SocketIO, emit
import random
 
app = Flask(__name__)

# 连接建立
@socketio.on('connect', namespace='/ss5')
def test_connect():
    while True:
        socketio.sleep(5)
        t = random_int_list(1, 100, 10)
        emit('server_response',
                      {'data': t},
                      namespace='/ss5')

# 连接断开
@socketio.on('disconnect', namespace='/chat')
def test_disconnect():
    print('Client disconnected')

# 收到客户端的消息（未命名事件）
@socketio.on('message')
def handle_message(message):
     print('received message: ' + message)

# 未命名事件接收json消息
@socketio.on('json')
def handle_json(json):
      print('received json: ' + str(json))
 
def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list
 
if __name__ == '__main__':
    socketio.run(app, debug=True)
