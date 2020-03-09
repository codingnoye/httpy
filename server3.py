import socket

SERVER = ('127.0.0.1', 3000)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind(SERVER)
server_socket.listen()

client_socket, CLIENT = server_socket.accept()
print(f'{CLIENT}가 연결됨')

body = "Hello, World!"

msg = f"""HTTP/1.1 200 FINE
Content-Type: text/plain; charset=UTF-8
Content-Encoding: UTF-8
Content-Length: {len(body)}

{body}"""

if ('\r\n' not in msg):
    msg = msg.replace('\n', '\r\n')

while True:
    data = client_socket.recv(1024)
    if not data: break

    print(f'"""{data.decode()}"""')
    client_socket.sendall(msg.encode())

client_socket.close()
server_socket.close()