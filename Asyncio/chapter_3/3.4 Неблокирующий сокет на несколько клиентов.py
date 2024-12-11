import socket



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("127.0.0.1", 5000)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(server_address)
server.listen()
server.setblocking(False)  # Неблокирующий режим серверного сокета
connections = []

try:
    while True:
        try:
            connection, client_address = server.accept()
            connection.setblocking(False)  # Неблокирующий режим для сокета выделенного для клиента
            connections.append(connection)
            print(f"Подключился клиент: {client_address}")
        except BlockingIOError:
            pass

        for connection in connections:
            try:
                buffer = b''

                while buffer[-1024:] != b'\r\n':
                    client_message = connection.recv(1024)
                    if not client_message:
                        break
                    else:
                        buffer = buffer + client_message

                print(f"{buffer.decode()}")
                connection.send(buffer)
            except BlockingIOError:
                pass
except KeyboardInterrupt:
    server.close()
finally:
    server.close()






