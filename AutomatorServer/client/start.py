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
	output = run_command("adb forward tcp:9008 tcp:9008")
	print(output)

	s = socket.socket()         # Create a socket object
	host = "127.0.0.1"#socket.gethostname() # Get local machine name
	port = 9008                # Reserve a port for your service.
	print("host: ", host, " port: ", port)
	s.connect((host, port))
	s.sendall(b"hello")
	full_response = ""
	while True: 
		chunk = s.recv(1024)
		print(chunk, end="")
		if not chunk: 
			break
	s.close()


	print("output", output)
if __name__ == '__main__':
	main()