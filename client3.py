import socket, time
from wsgiref.handlers import format_date_time

#SERVER = ('example.com', 80)
SERVER = ('localhost', 3000)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(SERVER)
print(f'{SERVER}에 연결함')

msg = f"""GET / HTTP/1.1
Host: {SERVER[0]}
Date: {format_date_time(time.time())}
Accept: text/html

"""

if ('\r\n' not in msg):
    msg = msg.replace('\n', '\r\n')

client_socket.sendall(msg.encode())

data = client_socket.recv(1024)
print(f'{SERVER}: {data.decode()}')

client_socket.close()