import socket
from response import Response

SERVER = ('127.0.0.1', 3000)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind(SERVER)
server_socket.listen()

client_socket, CLIENT = server_socket.accept()
print(f'{CLIENT}가 연결됨')

res = Response()
res.body = "Hello, world!"
res.header.headers['Connection'] = 'Keep-Alive'
res.header.headers['Keep-Alive'] = 'timeout=5, max=100'

msg = res.str()

if ('\r\n' not in msg):
    msg = msg.replace('\n', '\r\n')

print(f'"""{msg}"""')

while True:
    data = client_socket.recv(1024)
    if not data: break

    print(f'"""{data.decode()}"""')
    client_socket.sendall(msg.encode())

client_socket.close()
server_socket.close()