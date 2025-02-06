import threading
import server

serv = server.Server("batata", 5, "localhost", 25831)

serv.accept_clients()

input()