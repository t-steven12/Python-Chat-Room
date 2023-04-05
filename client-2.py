import socket

# Citation for the following code for setting up client sockets in lines 17-19:
# Derived from the sample code for creating client sockets from the "Creating A Socket" section (first code example
# in the section) on the web page titled "Socket Programming HOWTO" on docs.python.org.
# Altered/Changed Parts:
#   - "s" is called "clientSock" in this program
#   - the client socket connects to "('localhost', 4361)" instead of "("www.python.org", 80)"
# Why this was the best solution to my issue: It was the version of a referenced source on the project requirements
# description file (https://docs.python.org/3.4/howto/sockets.html in the file) for the most current stable release of
# Python at the time, and it was a great and succinct example of setting up client sockets.
# Source URL: https://docs.python.org/3/howto/sockets.html
# Author: Gordon McMillan
# Date: 6/4/2022


clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # client socket is made

clientSock.connect(('localhost', 4361))   # socket connects to "localhost" at port# 4361

print("Connected to server at 'localhost' on port# 4361!")

print("You may now chat with the server!")

print("Enter \"/q\" to quit.")

# Citation for the following code involving performing actions with a socket connection in a "while True" loop in lines 42-71:
# Derived from/based on the third code sample in the "Creating A Socket" section on the web page titled "Socket Programming HOWTO"
# on docs.python.org which involves accepting a socket connection and performing actions with that connection in a "while True" loop.
# Altered/Changed Parts:
#   - "(clientsocket, address) = serversocket.accept()" is never used.
#   - "ct = client_thread(clientsocket)" is never used.
#   - "ct.run()" is never used.
#   - Only the "while True:" line from the sample code is used for this program. All code inside the "while True:"
#     loop of this file differs from that of the sample code.
# Why this was the best solution to my issue: It was the version of a referenced source on the project requirements
# description file (https://docs.python.org/3.4/howto/sockets.html in the file) for the most current stable release of
# Python at the time, and it was a great and succinct example of perform actions with a socket in a while loop.
# Source URL: https://docs.python.org/3/howto/sockets.html
# Author: Gordon McMillan
# Date: 6/6/2022
while True:

    # Citation for the following code involving encoding and decoding messages to send via socket in lines 59-71:
    # Derived from/based on the second code sample encoding and decoding strings under the "Code to convert a python string to bytes"
    # section in the "Use encode():" subsection of the "How to convert Python string to bytes?" page on flexiple.com.
    # Altered/Changed Parts:
    #   - Added additional lines of code such as "clientSock.send(message)" in line 63 and "replyFromServer = clientSock.recv(3000)"
    #     in line 68.
    #   - "str_1 = "Join our freelance network"" not used.
    #   - "message = message.encode()" used instead of "str_1_encoded = str_1.encode(encoding = 'UTF-8')" for encoding string.
    #   - Encoded message is never printed to the console.
    #   - Decoded message printed to console via "print("Server: " + replyFromServer)" instead of "print(str_1_decoded)".
    #   - "replyFromServer = replyFromServer.decode()" used instead of "str_1_decoded = str_1_encoded.decode()" for decoding string.
    # Why this was the best solution to my issue: It was one of the first search results to pop up when searching for how to
    # convert a string to bytes in Python using Google search and it was the solution I felt the most comfortable with following.
    # Source URL: https://flexiple.com/python-string-to-bytes/
    # Date: 6/6/2022
    message = input("Enter message to send to server: ")

    message = message.encode()   # message to server are encoded as bytes

    clientSock.send(message)  # encoded message is sent to server

    if message.decode() == "/q":   # break happens when sent message is "/q"
        break

    replyFromServer = clientSock.recv(3000)   # receive reply message from server
    replyFromServer = replyFromServer.decode()    # decode server reply message

    print("Server: " + replyFromServer)

print("Ending client...")

clientSock.close()   # close client socket
