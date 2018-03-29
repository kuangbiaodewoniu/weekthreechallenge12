# !usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:dandan.zheng 
@file: scan.py 
@time: 2018/03/29 
"""
import socket, sys, getopt


def check_connection(ip, port):
    ip_port = (ip, port)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
    s.settimeout(0.1)
    status = s.connect_ex(ip_port)
    return status


def deal_with_params():
    host = ''
    result = []
    if '--host' not in sys.argv[1:]:
        print('Parameter Error')
        sys.exit(-1)
    if '--port' not in sys.argv[1:]:
        print('Parameter Error')
        sys.exit(-1)
    try:
        options, args = getopt.getopt(sys.argv[1:], "", ["host=", "port="])
        for name, value in options:
            if name == '--host':
                host = value
            if name == '--port':
                port = value
                if '-' in port:
                    ports = port.split('-')
                    min_port = int(ports[0])
                    max_port = int(ports[1])+1
                    result = [i for i in range(min_port,max_port)]
                else:
                    result = [int(port)]
        return {'host':host, 'port': result}
    except getopt.GetoptError:
        print('Parameter Error')
        sys.exit(-1)


def do_check():
    ip_port = deal_with_params()
    print (ip_port)
    ports = ip_port['port']
    ip = ip_port['host']
    for port in ports:
        status = check_connection(ip, port)
        if status == 0:
            print (str(port)+' open')
        else:
            print (str(port) + ' closed')


if __name__ == '__main__':
    do_check()
