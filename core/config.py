#coding=utf-8

'''
这块涉及命令行工具的处理，这里请看：
https://realpython.com/comparing-python-command-line-parsing-libraries-argparse-docopt-click/#conclusion
'''

# 用于读取ini文件，详见：https://python3-cookbook.readthedocs.io/zh_CN/latest/c13/p10_read_configuration_files.html
from configparser import ConfigParser
import os
import logging

SystemParams = {}

cfg = ConfigParser()
print('{0}/{1}'.format(os.path.dirname(os.path.dirname(__file__)), 'res/config.ini'))
cfg.read('{0}/{1}'.format(os.path.dirname(os.path.dirname(__file__)), 'res/config.ini'))
cfg.sections()

# 加密方法
if ('ENCRYPT_METHOD' in os.environ):
    SystemParams['encrypt-method'] = os.environ['ENCRYPT_METHOD']
else:
    SystemParams['encrypt-method'] = cfg.get('server', 'encrypt-method')

# 密码处理
if (os.getenv('PASSWORD') is not None):
    SystemParams['password'] = os.environ['PASSWORD']
else:
    SystemParams['password'] = cfg.get('server', 'password')

# 服务地址
if ('SERVER_ADDRESS' in os.environ):
    SystemParams['server-address'] = os.environ['SERVER_ADDRESS']
else:
    SystemParams['server-address'] = cfg.get('server', 'server-address')

# 服务端口
if (os.getenv('SERVER_PORT') is not None):
    SystemParams['server-port'] = os.environ['SERVER_PORT']
else:
    SystemParams['server-port'] = cfg.get('server', 'server-port')

# 日志级别
if ('LOGGER_LEVEL' in os.environ):
    SystemParams['logger-level'] = os.environ['LOGGER_LEVEL']
else:
    SystemParams['logger-level'] = cfg.get('server', 'logger-level')

# 日志文件名
if (os.getenv('LOGGER_FILE') is not None):
    SystemParams['logger-file'] = os.environ['LOGGER_FILE']
else:
    SystemParams['logger-file'] = cfg.get('server', 'logger-file')

if __name__ == '__main__':
    pass