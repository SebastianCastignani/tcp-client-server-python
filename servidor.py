import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
s.bind(("127.0.0.1", 7777))
s.listen(1)

print("Servidor de Chat\n")

try:
    while True:
        print("Esperando conexión del cliente...")
        sc, addr = s.accept()
        print("Cliente conectado desde:", addr)

        try:
            while True:
                recibido = sc.recv(1024)       
                if not recibido:                
                    break
                
                if recibido.strip() == b"quit":         
                    break
                print("Recibido:", recibido.decode("utf-8", errors="ignore"))

                nuestra_respuesta = "Hola cliente, yo soy el servidor"
                sc.sendall(nuestra_respuesta.encode("utf-8"))
        finally:
            sc.close()
            print("Cliente desconectado.\n")

except KeyboardInterrupt:
    print("Adiós")

finally:
    s.close()
