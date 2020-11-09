import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('Iniciando en {} puerto {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('Esperando por una conexión...')
    connection, client_address = sock.accept()
    try:
        print('Conexión desde ', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(32)
            print('Recibido {!r}'.format(data))
            if data:
                print('Enviando datos de vuelta al cliente')
                connection.sendall(data)
            else:
                print('Sin datos desde', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()