# client
import socket

server_socket = socket.socket()
server_address = ("127.0.0.1", 5000)
server_socket.connect(server_address)


try:
    while True:
        message = input("I: ").encode()
        server_socket.sendall(message)
        message_server = server_socket.recv(1024).decode()
        print(f"Server: {message_server}")

except KeyboardInterrupt:
    server_socket.close()
finally:
    server_socket.close()









