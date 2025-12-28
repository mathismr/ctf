import threading
import random
import socket
from datetime import datetime 

class Read(threading.Thread):
    # Init variables
    def __init__(self, client, infos, ans):
        threading.Thread.__init__(self)
        self.client = client
        self.infos = infos
        self.ans = str(ans)
    
    # Main listening function 
    def run(self):
        print(f'[SERVER] STATUS > Listening to {self.infos[0]}')
        flag = 'FLAG_S0ck3tIsTo0E4sy' # Initiating flag
        message = self.client.recv(1024).decode('utf-8')

        # Update logs on each message received, if client gets flag, if client fails.
        with open('logs.txt', 'a') as log_file:
            log_file.write(f'\n[{datetime.now()}] (SRV1) {self.infos} > MESSAGE : {message}')

            if message == self.ans: # Send flag if message contains correct answer
                try:
                    print(f'[CLIENT] {self.infos} > MESSAGE : {message}')
                    self.client.send(f'Epreuve validée :o ! FLAG: {flag}'.encode('utf-8'))
                    print(f'[CLIENT] {self.infos} > DISCONNECT')
                    self.client.close()
                    log_file.write(f'\n[{datetime.now()}] {self.infos} > Epreuve validée')
                except Exception as err: # Case when client sends erros as message
                    print(f'[CLIENT] {self.infos} > ERROR : {err}')
            else: # Send a kind message and close connection when answer is not correct
                try:
                    print(f'[CLIENT] {self.infos} > MESSAGE : {message}')
                    self.client.send('Mauvaise réponse >:( !'.encode('utf-8'))
                    self.client.close()
                    log_file.write(f'\n[{datetime.now()}] {self.infos} > Echec')
                except Exception as err: 
                    print(f'[CLIENT] {self.infos} > ERROR : {err}')

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostbyname(socket.gethostname())
    port = 51000
    server.bind((host, port))
    print(f'[SERVER] STATUS > Waiting for connexion...')
    server.listen()

    while True:
        client, infos = server.accept()
        print(f"[CLIENT] {infos[0]} > CONNECTED")
        x = random.randint(35, 75)
        y = random.randint(1000, 2000)
        ans = x*y
        client.send(f'\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\nBienvenue. Résoudre l\'équation suivante:{x}x{y}\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n'.encode('utf-8'))
        
        reading_thread = Read(client, infos, ans)
        reading_thread.start()
    
    server.close()

if __name__ == '__main__':
    main()