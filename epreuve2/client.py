import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVEUR_IP = '10.59.68.174'
    SERVEUR_PORT = 51000
    client.connect((SERVEUR_IP,SERVEUR_PORT))

    while True:
        data = client.recv(1024).decode('utf-8')
        data = data.split('\n')[2].split(':')[1].split('x')
        x, y = int(data[0]), int(data[1])
        
        client.send(f'{str(x*y)}'.encode('utf-8'))
        data = client.recv(1024).decode('utf-8')
        print(data)
        break

    client.close()

if __name__ == '__main__':
    main()