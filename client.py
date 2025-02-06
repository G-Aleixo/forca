import socket, pickle

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 25831))

answer_len = int.from_bytes(sock.recv(16))
print(answer_len)


guesses = " " * answer_len

close = False
while not close:
    print("""
0: Guess a letter
1: Guess word
2: Exit""")
    option = input("Insert choice here: ")
    
    result = ""
    match option:
        case "0":
            sock.send(b"0")
            guess = input("Letter to guess: ")
            
            sock.send(guess.lower().encode())
            result = sock.recv(16)
            
            if result == "correct":
                for pos in pickle.loads(sock.recv(800)):
                    guesses[pos] = guess
        case "1":
            sock.send(b"1")
            sock.send(input("Guess word: ").lower().encode())
            
            if result == "correct":
                print("yay!")
        case "2":
            sock.send(b"2")
            sock.close()
            
            close = True
            break
    print(guesses)
    print(result)