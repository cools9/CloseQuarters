import socket

def receive_messages(port=8000):
    # Create a TCP socket
    server_socket = socket.socket ( socket.AF_INET , socket.SOCK_STREAM )

    # Set the server address and port
    server_address = ('' , port)

    try:
        # Bind the socket to the server address and port
        server_socket.bind ( server_address )

        # Listen for incoming connections
        server_socket.listen ( 5 )

        print ( f"Server is listening for incoming messages on port {port}..." )

        while True:
            # Wait for a connection
            client_socket , client_address = server_socket.accept ()

            # Receive data from the client
            data = client_socket.recv ( 1024 )

            # Print the received message
            message = data.decode ()
            print ( f"Received message from {client_address}: {message}" )



            # Close the client socket
            client_socket.close ()

    except Exception as e:
        print ( f"Error receiving messages: {e}" )

    finally:
        # Close the server socket (this should not be reached in this loop)
        server_socket.close ()





# Example usage:
receive_messages ( 8000 )
