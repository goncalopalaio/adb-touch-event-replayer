import os
import subprocess
import re
import time
import socket

END = "|"
SEP = ","

DEVICE_PORT = int(os.environ.get('UIAUTOMATOR_DEVICE_PORT', '9008'))
LOCAL_PORT = int(os.environ.get('UIAUTOMATOR_LOCAL_PORT', '9008'))
ANDROID_HOME = os.environ.get('ANDROID_HOME', '/Users/goncalopalaio/Library/Android/sdk')

adb_filename = "adb.exe" if os.name == 'nt' else "adb"
adb_cmd = os.path.join(ANDROID_HOME, "platform-tools", adb_filename)

adb_server_host = 'localhost'
adb_server_port = '5037'

adbHostPortOptions = []
if adb_server_host not in ['localhost', '127.0.0.1']:
	adbHostPortOptions += ["-H", adb_server_host]
if adb_server_port != '5037':
	adbHostPortOptions += ["-P", adb_server_port]

def exec_adb_cmd(*args):
	# TODO use device serial
	# if serial:
	# 	if " " in serial: serial="'%s'" % serial
	# ["-s", serial] + list(args)

	line = [adb_cmd] + adbHostPortOptions + list(args)
	if os.name != "nt":
		line = [" ".join(line)]
	print("cmd: ", line)
	return subprocess.Popen(line, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def exec_now(*args):
	return exec_adb_cmd(*args).communicate()

def exec_now_formatted(*args):
	res = exec_now(*args)
	out = [] 
	for f in res:
		out.append(f.decode('utf-8', 'replace').strip())
	return out

def get_devices():
	d = exec_now_formatted("devices")
	return d

def connect_to_socket(port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = s.connect_ex(('127.0.0.1', port))
	
	return s, result == 0

def find_forward_list():
	forwarded_port_list = exec_now_formatted("forward", "--list")[0]
	forwarded_port_list = forwarded_port_list.split("\n")

	out = []
	for f in forwarded_port_list:
		f = f.split(" ")
		if not f or f[0] == '':
			continue
		out.append((f[0], f[1], f[2]))
	return out

def find_local_port(device_serial, device_port):
	# Get a port that is already forwarded
	forward_list = find_forward_list()
	print("Forward list: ", forward_list)

	for serial, local_port, remote_port in forward_list:
		if serial == device_serial and remote_port == 'tcp:%d' % device_port:
			return int(local_port[4:]), True

	local_port = LOCAL_PORT
	while connect_to_socket(local_port)[1]:
		local_port += 1
	return local_port, False

def find_device_serial():
	devices = exec_now_formatted("devices")[0]
	print("Device list: ", devices)

def main():
	device_serial = "66e13a08"
	device_port = DEVICE_PORT
	local_port, already_forwarded = find_local_port(device_serial, device_port)
	print("Local port: ", local_port)
	socket, is_listening = connect_to_socket(local_port)
	print("Are you there? ", is_listening)
	if not is_listening:
		
		find_device_serial()

		if not already_forwarded:
			print("Will try to forward the port")
			res = exec_adb_cmd("forward", "tcp:%d" % local_port, "tcp:%d" % device_port).wait()
			print("Forward result:", res, "success" if res == 0 else "failure")

		print("Now, Are you there? ", connect_to_socket(local_port)[1])

	try:
		socket.send(("runprogram"+SEP+"name_of_program"+END).encode())
		while True:
			response = socket.recv(8192)
			if not response:
				break
			print("Response:", response)
			
	except KeyboardInterrupt as e:
		pass
	finally:
		socket.close()
if __name__ == '__main__':
	main()