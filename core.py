import paramiko
import socket
import os
import platform
import pyping


def ping(ip: str):
    key = '-n' if platform.system().lower() == 'windows' else '-c'
    nul = 'nul' if platform.system().lower() == 'windows' else '/dev/null'
    return os.system(f'ping {key} 1 {ip} > {nul} 2>&1') == 0


def scan_port(ip: str, port: int):  # TCP SYN scanning
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:  # создали TCP соединение
        client.settimeout(0.5)
        return not client.connect_ex((ip, port))


def read_banner(ip: str, port: int):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:  # создали TCP соединение
        client.connect_ex((ip, port))
        banner = client.recv(1024).decode('utf-8')
    return banner


def get_config(host: str, login: str, password: str, command: str):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port=22, username=login, password=password, timeout=3)
    (stdin, stdout, stderr) = client.exec_command(command)
    config = stdout.read().strip().decode('ASCII')
    client.close()
    return config

