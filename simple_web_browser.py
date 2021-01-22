import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) ## Making an endpoint/ socket.socket("Make a phone")
mysock.connect(('data.pr4e.org', 80)) ## mysock.connect("Dial the phone")
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode() ## GET protocol:webserver/document HEADER return\newline\return\newline compressIntoUTF-8
mysock.send(cmd) ## Browser/"phone" sends GET request

## Receive data until the socket is closed
while True:
    data = mysock.recv(512) ## Receive UTF-8 compressed data
    if len(data) < 1: ## If the data returns nothing
        break
    print(data.decode(),end='') ## Convert the data to Unicode and print it

mysock.close() ## Officially close the connection/"phone call" on this end