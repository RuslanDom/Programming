# server
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_address = ("127.0.0.1", 5000)
server.bind(server_address)
server.listen()
print("Server run...")
connection, client_address = server.accept()
try:
    while True:
        message_server = input('- ').encode()
        connection.sendall(message_server)
        message = connection.recv(1024).decode()
        print(f"{client_address}: {message}")


except KeyboardInterrupt:
    server.close()
finally:
    server.close()


