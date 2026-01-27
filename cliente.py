import socket

socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_cliente.connect(("127.0.0.1", 7777))

try:
    mensaje = input(">> ")
    socket_cliente.sendall(mensaje.encode("utf-8"))
    
    if mensaje != "quit":
        recibido = socket_cliente.recv(1024)
        if not recibido:
            print("Servidor cerró la conexión.")
        else:
            print("Recibido:", recibido.decode("utf-8", errors="ignore"))

    print("Adiós")

finally:
    socket_cliente.close()