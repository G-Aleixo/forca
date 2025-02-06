import socket, threading

class Server:
    def __init__(self, answer: str, max_clients: int, address: str, port: int) -> None:
        self.answer = answer
        self.max_clients = max_clients
        
        self.guessed = []
        
        self.clients = []

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((address, port))
        
    def accept_clients(self):
        self.server_socket.listen()
        client_socket, addr = self.server_socket.accept()
        print(addr)
        self.clients.append(client_socket)
        
        threading.Thread(target=self.handle_clients, args=(client_socket,)).start()
        
    def handle_clients(self, client_socket: socket.socket):
        guess = ""
        
        while True:
            typ = client_socket.recv(1).decode()
            if typ == "0": # Guess letter
                guess = client_socket.recv(8).decode()
                print(guess)
                if guess[0].lower() in self.guessed:
                    client_socket.send("repeated".encode())
                elif guess[0].lower() in self.answer:
                    client_socket.send("correct".encode())
                else:
                    client_socket.send("incorrect".encode())
            elif typ == "1":
                guess = client_socket.recv(800).decode()
                if guess == self.answer:
                    client_socket.send("correct".encode())
                else:
                    client_socket.send("incorrect".encode())
            elif typ == "2":
                client_socket.close()
                self.clients.remove(client_socket)
                break