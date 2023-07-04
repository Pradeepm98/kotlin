import socket
import threading

def handle_client(client_socket, address):
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            print(f"Received from {address}: {data}")

            # Send the received message back to the client
            client_socket.sendall(data.encode('utf-8'))
        except Exception as e:
            print(f"Error handling client {address}: {e}")
            break

    print(f"Client disconnected: {address}")
    client_socket.close()

def start_server():
    host = '127.0.0.1'
    port = 3000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print("Chat server started on {}:{}".format(host, port))

    while True:
        client_socket, address = server_socket.accept()
        print(f"Client connected: {address}")

        threading.Thread(target=handle_client, args=(client_socket, address)).start()

    server_socket.close()

if __name__ == '__main__':
    start_server()
