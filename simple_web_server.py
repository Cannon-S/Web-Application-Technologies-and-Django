from socket import *

def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM) ## Making an endpoint/"phone"
    try :
        serversocket.bind(('localhost',9000)) ## Open to receiving "phone calls" on port 90
        serversocket.listen(5) ## Queue up to 4 connections/"phone calls" if already busy
        while(1):
            (clientsocket, address) = serversocket.accept() ## I'm ready to accept phone calls

            rd = clientsocket.recv(5000).decode() ## Receive request and decode it into unicode
            pieces = rd.split("\n") ## Split the GET, headers, etc
            if ( len(pieces) > 0 ) : print(pieces[0]) ## Print out the request

            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World</body></html>\r\n\r\n"
            clientsocket.sendall(data.encode()) ## Encode and send the data
            clientsocket.shutdown(SHUT_WR) ## Hang up the phone

    except KeyboardInterrupt :
        print("\nShutting down...\n");
    except Exception as exc :
        print("Error:\n");
        print(exc)

    serversocket.close() ## Close endpoint

print('Access http://localhost:9000')
createServer()
    