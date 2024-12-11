import os.path
import socket
from socket import create_server

# Серверные инструкции в функцию
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        """
        Создание
        """
        server.bind(("127.0.0.1", 5000))
        # Одной строкой
        # server = create_server(("127.0.0.1", 5000))
        print("Server running")
        """
        Ожидание
        """
        server.listen(5)  # В параметр можно передать число, которое будет постановлено в очередь, остальные сброшены
        while True:
            """
            Получение запроса
            """
            client_socket, address = server.accept()

            """
            Обработка запроса
            """
            data = client_socket.recv(1024).decode('utf-8')

            """
            Ответ
            """
            message = load_page_from_get_request(data)
            client_socket.send(message)
            client_socket.shutdown(socket.SHUT_WR)
    except KeyboardInterrupt:
        server.close()
        print('SHUTDOWN THIS SHIT...')


def load_page_from_get_request(request_data: str):
    HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    HDRS_404 = 'HTTP/1.1 404 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    print(request_data)
    path = request_data.split(' ')[1]
    
    response = ''
    try:
        with open(os.path.join("views") + path, 'rb') as file:
            response = file.read()
        return HDRS.encode('utf-8') + response
    except FileNotFoundError:
        return (HDRS_404 + 'Sorry bro! No page...').encode('utf-8')

if __name__ == "__main__":
    start_server()

# http://127.0.0.1:5000/home.html