#coding=utf-8

import json
import websocket

def on_message(self, message):   # 第一个参数必须传递
　　print(message)


def on_error(self, error):
　　print(error)


def on_close(self):
　　print("### closed ###")


def on_open(self):
　　def run():
　　　　for i in range(3):  # 可以死循环发送
　　　　　　ws.send(json.dumps({1: "123123"}))
　　　　# ws.close()  # 发送完毕, 可以不关闭

　　thread.start_new_thread(run, ())  # 启动线程执行run()函数发送数据


if __name__ == "__main__":

　　while True:
　　　　try:
　　　　　　websocket.enableTrace(True)  # True 默认在控制台打印连接和信息发送接收情况
　　　　　　ws = websocket.WebSocketApp("ws://192.168.130.164:8765/api/v1/data/",
　　　　　　　　on_open=on_open,  # 连接后自动调用发送函数, 
　　　　　　　　on_message=on_message,  # 接收消息调用
　　　　　　　　on_error=on_error,
　　　　　　　　on_close=on_close)
　　　　　　ws.run_forever()  # 开启长连接

　　　　# except KeyboardInterrupt: # 会被ws内部捕捉
　　　　　　# print(123)
　　　　　　# break
　　　　except Exception as e: # ws 断开 或者psycopg2.OperationalError
　　　　　　logger.warning("ws 断开 或者psycopg2.OperationalError, {}: {}".format(type(e), e))
　　　　　　continue