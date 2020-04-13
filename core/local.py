#coding=utf-8

from getopt import getopt
import sys

def usage():
    print "使用方法"
    print '-h --help', 'print help hint'
    print '-m --method <method>', 'encryption method, default: aes-256-cfb'
    print '-k --password <password>', 'password'
    print '-s --server-address <address>', 'server address'
    print '-p --server-port <port>', 'server port, default: 8388'
    print '-b --local-address <address>', 'local binding address, default: 127.0.0.1'
    print '-l --local-port <port>', 'local port, default: 1080'
    print '--log-level <level>', 'log level(debug|info|warn|error|fatal)'
    print '--log-file <file>', 'log file'

try:
    opts, args = getopt(sys.argv[1:],'hm:k:s:p:b:l:::',
    ['help', 'method=','password=','server-address=','server-port=','local-address=','local-port=','log-level=','log-file='])
except Exception:
    usage()
    sys.exit(1)

config = {}
for opt_name, opt_value in opts:
    if opt_name in ('-h','--help'):
        usage()
        sys.exit(0)
    if opt_name in ('-m','--method'):
        config['method'] = opt_value
    if opt_name in ('-k','--password'):
        config['password'] = opt_value
    if opt_name in ('-s','--server-address'):
        config['server-address'] = opt_value
    if opt_name in ('-p','--server-port'):
        config['server-port'] = opt_value
    if opt_name in ('-b','--local-address'):
        config['local-address'] = opt_value
    if opt_name in ('-l','--local-port'):
        config['local-port'] = opt_value
    if opt_name in ('--log-level'):
        config['--log-level'] = opt_value
    if opt_name in ('--log-file'):
        config['--log-file'] = opt_value

print(config)

def __main__():
    pass