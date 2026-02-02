# Client-Server Architecture:

### Client:
* They are the systems which invoke a commnication.
* They request for resources

### Server:
* They are powerful systems which satisfy the requests of a client
* They contain resources required for the client.

### Working:
* The client requests for a data and the server sends back to the client.

# Request-response model:
* It is the model which is used in client server architecture.
* They request recieve the required data
* The response is form server

## Working:

### Client to server:
* The client send request to the server in bytes.

## server parse
* The server parses the data received. 
* They are received in byted, converted using UTF-8 encoding etc.
* They consists of request line, header, body.
```
POST /abc/endpoint1 HTTP/1.1
Host: abc.com
Content-type:application/JSON
Content-length: 100

{body}
```
* They request line contains the method, the endpoint and the protocol version used.
    POST /abc/endpoint1 HTTP/1.1
* The next is header which has meta data.
* These meta data tell what type of data is held and who sent it and how many bytes of data is there and so on.
* The server only parses the length specified in the content-length.
* The blank line after header denotes that the header is over and the remaining is body.
* The data between server and client is communicated using string.

## server response:
* the server responses with a status code to the client.
* each status code has a meaning
```
status line
response header

response body
```
## Status codes:
* Status codes tell what is the response of a server.
There are several:
* 200 :Successfull code 
* 300 :Redirection code
* 400 :Client error
* 500 :Server error

# Stateful and stateless protocol:
 **Stateful:** 
* it is where the previous state of the request matters.
* if the response is not received, the request is sent again
* Eg : TCP,FTP etc.

**Stateless**:
* It is where the previous state of the request doesn't matter.
* Eg: HTTP, UDP, DNS etc.

## TLS/SSL:
* Both are same but TLS is the current secure socket layer. 
* They provide certificate that this domain is safe to give data and it wont be stole in middle of the transfer

## HTTPS:
* https uses TLS for secure transfer of data. 
* They do 3 way handshake which ensures the privacy of the data.
* They hash the data which is passed between client and server.

1. Client sends a message to server
2. server sned a message to client
3. client sends the encryption and decryption verison it has.
4. server recieves a TLS certificate with a public key
5. the client sends message using this public key to encrypt the data
6. the server recieves and decrypts using the private key it holds.