import socket

# Citation for the following code in lines 18-22 involving server socket creation:
# Derived from the sample code for creating server sockets from the "Creating A Socket" section (second code example
# in the section) on the web page titled "Socket Programming HOWTO" on docs.python.org.
# Altered/Changed Parts:
#   - "serversocket" is called "serverSock" in this program
#   - the server socket binds to "('localhost', 4361)" instead of "(socket.gethostname(), 80)"
#   - the server socket listens for only 1 connection request instead of 5 (listen(1) instead of listen(5))
#   - Several print statements have been added.
# Why this was the best solution to my issue: It was the version of a referenced source on the project requirements
# description file (https://docs.python.org/3.4/howto/sockets.html in the file) for the most current stable release of
# Python, and it was a great and succinct example of how to set up a server socket.
# Source URL: https://docs.python.org/3/howto/sockets.html
# Author: Gordon McMillan
# Date: 6/4/2022

serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create server socket

serverSock.bind(('localhost', 4361))   # bind server socket to 'localhost' at port# 4361

serverSock.listen(1)   # listen for one connection request only

print("Listening for connection requests on 'localhost' at port# 4361!")

print("Waiting to establish connection with client...")

# Citation for the following code involving accepting a socket connection and performing actions with that connection in a "while True" loop in lines 45-85:
# Derived from/based on the third code sample from the "Creating A Socket" section on the web page titled "Socket Programming HOWTO" on docs.python.org
# which involves accepting a socket connection and performing actions with that connection in a "while True" loop.
# Altered/Changed Parts:
#   - A connection is accepted before the while loop and only the first element of the returned tuple from accept() is
#     assigned to a variable ("connection = serverSock.accept()[0]" used instead of "(clientsocket, address) = serversocket.accept()").
#   - "ct = client_thread(clientsocket)" is never used.
#   - Several additional print statements have been added.
#   - "ct.run()" is never used.
#   - Lines of code never used in the original code sample have been added. This includes lines 73 and 85.
# Why this was the best solution to my issue: It was the version of a referenced source on the project requirements
# description file (https://docs.python.org/3.4/howto/sockets.html in the file) for the most current stable release of
# Python, and it was a great and succinct example of how to accept a socket connection and perform actions with that connection.
# Source URL: https://docs.python.org/3/howto/sockets.html
# Author: Gordon McMillan
# Date: 6/6/2022

connection = serverSock.accept()[0]    # accept a connection request

print("Connection with client established at 'localhost' on port# 4361!")

print("You may now chat with the client!")

print("Server will terminate when client sends message of \"/q\".")

print("Waiting for message from client...")

while True:

# Citation for the following code involving encoding and decoding messages in a socket in lines 73-85:
# Derived from/based on the second code sample encoding and decoding strings under the "Code to convert a python string to bytes"
# section in the "Use encode():" subsection of the "How to convert Python string to bytes?" page on flexiple.com.
# Altered/Changed Parts:
#   - Added additional lines of code such as "clientMessage = connection.recv(3000)" in line 73 and "connection.send(reply)"
#     in line 85.
#   - "str_1 = "Join our freelance network"" not used.
#   - "clientMessage = clientMessage.decode()" used instead of "str_1_decoded = str_1_encoded.decode()" for decoding string.
#   - Encoded message/reply is never printed to the console.
#   - Decoded message printed to console via "print("Client: " + clientMessage)" instead of "print(str_1_decoded)".
#   - "reply = reply.encode()" used instead of "str_1_encoded = str_1.encode(encoding = 'UTF-8')" for encoding string.
#   - decode() function is used before encode() function.
# Why this was the best solution to my issue: It was one of the first search results to pop up when searching for how to
# convert a string to bytes in Python using Google search and it was the solution I felt the most comfortable with following.
# Source URL: https://flexiple.com/python-string-to-bytes/
# Date: 6/6/2022
    clientMessage = connection.recv(3000)   # receive message from client
    clientMessage = clientMessage.decode()   # decode message from client

    print("Client: " + clientMessage)

    if clientMessage == "/q":   # if client's message is "/q" then break
        break

    reply = input("Enter message to send to client: ")

    reply = reply.encode()   # encode reply message

    connection.send(reply)  # send encoded reply message to client

print("Ending server...")

serverSock.close()
