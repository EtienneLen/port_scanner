import socket

port = 7999 
address = "127.0.0.1"
closedPorts = []
openPorts = []

while True :


    print("Nouvelle tentative...")
    port = port + 1
    s = socket.socket()
    print ("Tentative de connection :  ", port)
    try :
        s.connect((address, port))
        data = s.recv(1024)
        print ("Connection réalisée :  ", port)
        openPorts.append(port)
        print(openPorts)
        break
    except  :
         print("Erreur : impossible d'obtenir une réponse")
         closedPorts.append(port)
         print(closedPorts)

      