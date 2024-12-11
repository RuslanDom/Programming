import socket


serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.connect(('127.0.0.1', 5000))
print(f"Присоединился к серверу...")
try:
    while True:
        message = input('I am say... ').encode()
        serv_socket.sendall(message)
        get_message = serv_socket.recv(1024).decode()
        print(f"Server: {get_message}")

except KeyboardInterrupt:
    print('Соединение закрыто!')
finally:
    serv_socket.close()