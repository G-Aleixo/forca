import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 25831))

sock.send(b"0")
sock.send(input().encode())
print(sock.recv(800))

sock.send(b"2")
sock.close()