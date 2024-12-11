import socket

""" Подключиться с помощью telnet
telnet localhost <port>
"""

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = ('127.0.0.1', 5000)
    server.bind(server_address)
    server.listen()
    print('Server run...')
    try:
        while True:
            connection, client_address = server.accept()
            print(f'Connect client: {client_address}')
            message = "Hello, Buddy...".encode()
            connection.send(message)
            buffer = b''
            while buffer[-1024:] != b'\r\n':
                client_message = connection.recv(1024)
                if not client_message:
                    break
                else:
                    buffer = buffer + client_message
            print(f"{client_address}: {buffer.decode()}")
            connection.send(buffer)  # echo фраза
    except KeyboardInterrupt:
        server.close()
    finally:
        server.close()

if __name__ == "__main__":
    main()
