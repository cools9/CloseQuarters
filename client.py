import socket


def send_message_to_ip(message , ip , port=8000):
    # Create a TCP socket
    client_socket = socket.socket ( socket.AF_INET , socket.SOCK_STREAM )

    try:
        # Connect to the specified IP address and port
        client_socket.connect ( (ip , port) )

        # Send the message
        client_socket.send ( message.encode () )

        # Receive a response (optional, depends on your use case)
        response = client_socket.recv ( 1024 ).decode ()
        print ( f"Received response from {ip}:{port}: {response}" )

    except Exception as e:
        print ( f"Error sending message to {ip}:{port}: {e}" )

    finally:
        # Close the socket
        client_socket.close ()


# Example usage:
send_message_to_ip ( "Hello, this is a custom message!" , "192.168.1.6" , 8000 )
