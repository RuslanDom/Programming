import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

name = input("Enter your name: ")
server_socket.connect(("127.0.0.1", 5000))  # Функция на подключение к порту сервера
server_socket.send(name.encode())
socket_name = server_socket.recv(1024)
server_name = socket_name.decode()
print(f"{server_name} ready!")

while True:
    message = server_socket.recv(1024).decode()
    print(f"{server_name}: {message}")
    message = input(f"{name}: ")
    server_socket.send(message.encode())







