from core import scan_port, read_banner, get_config, ping
from _datetime import datetime
import os


ports = [443]  # [21, 22, 23, 25, 68, 80, 88, 110, 115, 119, 123, 139, 143, 161, 162, 220, 389, 443, 3306, 3389, 8080]
hosts = ['10.1.201.57', '10.1.201.58', '10.1.201.213']

open_p = dict()
'''start_time = datetime.now()
for host in hosts:
    open_p[host] = []
    for port in ports:
        if scan_port(host, port):
            open_p[host].append(port)
end_time = datetime.now()
print('Ended in: {}'.format(end_time - start_time))
for d in open_p.items():
    print(d)
'''
# ---------------------------------------------------------------------------------------------------------
'''start_time = datetime.now()
for host in hosts:
    open_p[host] = ''
    for port in ports:
        try:
            open_p[host] = read_banner(host, port).rstrip()
        except Exception as e:
            open_p[host] = e
end_time = datetime.now()
print('Ended in: {}'.format(end_time - start_time))
for d in open_p.items():
    print(d)'''
# ----------------------------------------------------------------------------------------------------------------
#  print(get_config('10.1.201.213', 'ainur', '1q2w3e', 'uname -api'))
print(ping('10.1.201.58'))
