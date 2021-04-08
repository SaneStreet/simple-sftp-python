# import the socket library
import socket

# define a variable to the socket connection
s = socket.socket()
# prompt the user for a host name
host = input(str("Enter host address of sender : "))
# use the port no. 8080
port = 8080

# connect to the socket with the hostname and port no.
s.connect((host, port))
print("Connected .. ")

# prompt the user for a filename
# to receive data from to a new file (.txt)
filename = input(str("Enter a filename  for incoming file : "))
file = open(filename, 'wb') # make it writeable and in bytes
file_data = s.recv(1024) #read the file in bytes
file.write(file_data) # write the data to the new file
file.close() # close the file
print("File received successfully!")