import os
import subprocess

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


def find_adb_path():
	pass
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

def get_adb_version():
	pass
def main():
	print("Device port", DEVICE_PORT)
	print("Device port", LOCAL_PORT)
	print("Android home", ANDROID_HOME)

	if not os.path.exists(ANDROID_HOME):
		print("Path to android sdk not found. Set it as an environment variable ANDROID_HOME")
		return
	if not os.path.exists(adb_cmd):
		print("Path to adb not found: ", adb_cmd)
		return


	print(exec_adb_cmd("devices","").communicate())


if __name__ == '__main__':
	main()