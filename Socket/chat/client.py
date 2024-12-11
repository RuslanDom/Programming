import socket
from server import SERVER_ADDRESS


def client_run(server_address):
    socket_server = socket.socket()
    try:
        name = input('Введите ваше имя: ').encode()
        socket_server.connect(server_address)
        socket_server.send(name)
        print(f'Подключение к серверу...')
        while True:
            server_message = socket_server.recv(1024).decode()
            print(f'Сервер: {server_message}')
            client_message = input('Вы: ').encode()
            socket_server.send(client_message)
    finally:
        socket_server.close()


if __name__ == "__main__":
    client_run(server_address=SERVER_ADDRESS)
