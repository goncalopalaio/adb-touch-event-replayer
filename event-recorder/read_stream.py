import os
import subprocess
import re
import time

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

def main():
	devices = get_devices()
	print(devices)

	adb = exec_adb_cmd('shell', 'getevent')
	print(adb.poll())

	while adb.poll() is None:
		try:
			line = adb.stdout.readline().decode('utf-8', 'replace').strip()
			print(time.time(),line)
			
		except KeyboardInterrupt:
			break

	
	
if __name__ == '__main__':
	main()