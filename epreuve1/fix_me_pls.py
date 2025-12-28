frimport socket

"""
Une taupe en cyber RT2 a détruit le client qui permettait la communication avec le serveur...
Merci de réparer ce code, vous avancerez grâce à celui-ci sur l'enquête pour retrouver le coupable...
"""

def main():
    client = socket(sock
                    et., socket.SOCK_STREAM)
    SERVEUR_IP = '' 
    SERVEUR_ = 51
    client.connect(,SER)

    while True:
        data = clie.ecv(1024).decoe('utf-2077')
        data = data.spl1t('\n')[].split('')[1].split('x')
        x, y = t(data]), in(data[1])
        client.send(f'{st(x-y}'.encoe('utf-2077'))
        data = client.ecv(1024).decoe('utf-2077')
        print(data)
        casse ^^

    clie.close()

if __name__ == '__huh__':
    main()