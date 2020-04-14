#coding=utf-8

# 包引入
import logging
import socket

# 最大连接数
MAX_CONNECTIONS = 50000

# TCP运行类型
TCP_RELAY_TYPE_LOCAL = 1
TCP_RELAY_TYPE_SERVER = 2

# TCP地址类型
ADDRESS_TYPE_IPV4 = 0x01
ADDRESS_TYPE_DOMAIN_NAME = 0x03
ADDRESS_TYPE_IPV6 = 0x04
ADDRESS_TYPE = {
	1: 'IPV4',
	3: 'DOMAIN_NAME',
	4: 'IPV6'
}

# 版本号
VERSION = 0x05

# 方法验证
METHOD_NO_AUTHENTICATION_REQUIRED = 0x00
METHOD_GSSAPI = 0x01
METHOD_USERNAME_PASSWORD = 0x02
METHOD_NO_ACCEPTABLE_METHODS = 0xff

# 命令类型
CMD_CONNECT = 0x01
CMD_BIND = 0x02
CMD_UDP_ASSOCIATE = 0x03
CMD = {
	1: 'CONNECT',
	2: 'BIND',
	3: 'UDP_ASSOCIATE'
}

# 返回结果类型码
REPLIE_SUCCEEDED = 0x00
REPLIE_GENERAL_SOCKS_SERVER_FAILURE = 0x01
REPLIE_CONNECTION_NOT_ALLOWED_BY_RULESET = 0x02
REPLIE_NETWORK_UNREACHABLE = 0x03
REPLIE_HOST_UNREACHABLE = 0x04
REPLIE_CONNECTION_REFUSED = 0x05
REPLIE_TTL_EXPIRED = 0x06
REPLIE_COMMAND_NOT_SUPPORTED = 0x07
REPLIE_ADDRESS_TYPE_NOT_SUPPORTED = 0x08

# Stage
STAGE_INIT = 0
STAGE_ADDR = 1
STAGE_UDP_ASSOC = 2
STAGE_DNS = 3
STAGE_CONNECTING = 4
STAGE_STREAM = 5
STAGE_DESTROYED = -1
STAGE = {
	[-1]: 'STAGE_DESTROYED',
	0: 'STAGE_INIT',
	1: 'STAGE_ADDR',
	2: 'STAGE_UDP_ASSOC',
	3: 'STAGE_DNS',
	4: 'STAGE_CONNECTING',
	5: 'STAGE_STREAM'
}

# 服务状态码类型
const SERVER_STATUS_INIT = 0
const SERVER_STATUS_RUNNING = 1
const SERVER_STATUS_STOPPED = 2

# 全局连接信息
globalConnectionId = 1
connections = {}

class TCPRelay(object):
    def __init__(self, config, isLocal):
        self.config = config
        self.isLocal = isLocal
        self.server = None
        self.status = SERVER_STATUS_INIT
        self.config = require('./config.json')
        if (config) {
            self.config = Object.assign(this.config, config)
        }
        self.logger = None
        self.logLevel = 'error'
        self.logFile = None
        self.serverName = None
    
    def initLogger(self):
        self.logger = logging

    def initServer(self):
        port = self.isLocal ? config.localPort : config.serverPort
        address = self.isLocal ? config.localAddress : config.serverAddress
        server = None
        if self.isLocal:
            self.server = socket.socket(af, socktype, proto)
            server = self.server
            # local启动socket服务，用于上层的ss5服务
            pass
        else:
            # 服务端启动websocker服务，用于加密信道的传输
            pass
