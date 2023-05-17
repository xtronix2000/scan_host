import paramiko
import socket
from datetime import datetime


#  PENTEST
def scan_port(ip, port):  # TCP SYN scanning
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создали TCP соединение
    client.settimeout(0.5)
    return not client.connect_ex((ip, port))  # возвращает 0 если операция прошла успешно


def read_banner(ip, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect_ex((ip, port))
    banner = client.recv(1024).decode('utf-8')
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
import paramiko
import socket
from datetime import datetime


#  PENTEST
def scan_port(ip, port):  # TCP SYN scanning
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создали TCP соединение
    client.settimeout(0.5)
    return not client.connect_ex((ip, port))  # возвращает 0 если операция прошла успешно


def read_banner(ip, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect_ex((ip, port))
    banner = client.recv(1024).decode('utf-8')
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

