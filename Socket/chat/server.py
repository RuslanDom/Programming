import socket

SERVER_ADDRESS = ('127.0.0.1', 5000)

def server_run(server_address):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind(server_address)
        server.listen()
        print('Сервер запущен')
        connection, client_address = server.accept()
        client_name = connection.recv(1024).decode()
        print(f'Клиент с адресом: {client_address}, по имени {client_name}, присоединился!')
        while True:
            message = input('Сервер: ').encode()
            connection.send(message)
            client_message = connection.recv(1024).decode()
            print(f'{client_name}: {client_message}')

    finally:
        server.close()


if __name__ == "__main__":
    server_run(server_address=SERVER_ADDRESS)
