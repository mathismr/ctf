from datetime import datetime
import threading
import socket
import base64

class Read(threading.Thread):
    # Init variables
    def __init__(self, client, infos, str1, str2, str3):
        threading.Thread.__init__(self)
        self.client = client
        self.infos = infos
        self.str1 = str(str1)
        self.str2 = str(str2)
        self.str3 = str(str3)
    
    # Main listening function 
    def run(self):
        print(f'[SERVER] STATUS > Listening to {self.infos[0]}')
        message = self.client.recv(1024).decode('utf-8')

        # Update logs on each message received, if client gets flag, if client fails.
        with open('logs.txt', 'a') as log_file:
            log_file.write(f'\n[{datetime.now()}] (SRV2) {self.infos} > MESSAGE : {message}')
            if message == self.str1:
                pass
            else: 
                self.cient.send('Mauvaise réponse >:( !'.encode('utf-8'))
                self.client.close()
            message = self.client.recv(1024).decode('utf-8')
            if message == self.str2:
                pass
            else:
                self.cient.send('Mauvaise réponse >:( !'.encode('utf-8'))
                self.client.close()
            message = self.client.recv(1024).decode('utf-8')
            if message == self.str3:
                self.client.send('Message important : Vous avez trouvé la taupe, procédez à son arrestation sur le serveur web port 8001, entrez-y le mot de passe suivant: SacréeTaupe')
                self.client.close()
            else:
                self.cient.send('Mauvaise réponse >:( !'.encode('utf-8'))
                self.client.close()
            
            

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
        str1 = base64.b64encode('Mathias a été prouvé innocent'.encode())
        str2 = 'Antoine a un alibi mais reste suspect'.encode('utf-8').hex()
        str3 = base64.b32encode('Une preuve irréfutable incrimine Eliott'.encode())
        client.send(f'\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\nBienvenue. Décodez les chaines de caractères qui vont suivre\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n'.encode('utf-8'))
        
        reading_thread = Read(client, infos, str1, str2, str3)
        reading_thread.start()
    
    server.close()

if __name__ == '__main__':
    main()