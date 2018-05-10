#!/usr/bin/python
import subprocess
import socket

def run_command(cmd):
	"""given shell command, returns communication tuple of stdout and stderr"""
	return subprocess.Popen(cmd, 
							stdout=subprocess.PIPE, 
							stderr=subprocess.PIPE, 
							stdin=subprocess.PIPE, shell=True).communicate()
	
def main():
	s = socket.socket()
	host = "127.0.0.1"
	port = 9008
	#print("host: ", host, " port: ", port)
	s.connect((host, port))
	s.sendall(b"hello")
	full_response = ""
	while True: 
		chunk = s.recv(1024)
		print(chunk, end="")
		if not chunk: 
			break
	s.close()

if __name__ == '__main__':
	main()