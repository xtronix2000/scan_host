import paramiko
import socket
import json
from datetime import datetime


ports = [0, 20, 21, 22, 23, 25, 53, 67, 68, 80, 88, 443, 161, 162, 3389, 7070]


#  PENTEST
def port_state(ip, port):  # TCP SYN scanning
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создали TCP соединение
    client.settimeout(0.5)
    return not client.connect_ex((ip, port))  # возвращает 0 если операция прошла успешно


def read_banner(ip, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect_ex((ip, port))
    banner = client.recv(1024).decode('utf-8')
    client.close()
    return banner


#  AUDIT
def get_config(host, login, password, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port=22, username=login, password=password, timeout=3)
    (stdin, stdout, stderr) = client.exec_command(command)
    config = stdout.read().strip().decode('ASCII')
    client.close()
    return config


with open('hosts.json', 'r') as f:
    hosts = json.load(f)

"""for p in ports:
    status = scan_port('192.168.202.82', p)
    print(f'Port {p} is {status}')"""

print(read_banner('192.168.202.82', 22))


